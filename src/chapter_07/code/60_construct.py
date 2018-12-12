import json

ARTIST_PATH = "../resources/artist.json"
NAMELIST_PATH = "../resources/namelist.txt"
NAME_TO_AREA_PATH = "../resources/name-area.txt"


def dict_to_line_set(d):
    if "name" not in d.keys():
        return ""

    if "area" in d.keys():
        return 'SET "name:{}" "area:{}"'.format(d['name'], d['area'])
    else:
        return 'SET "name:{}" "area:{}"'.format(d['name'], "---")


def dict_to_namelist(d):
    if "name" not in d.keys():
        return ""

    return 'RPUSH namelist "{}"'.format(d['name'])


def main():
    print("Reading JSON file...")

    count = 0
    with open(ARTIST_PATH, encoding="utf8") as f,\
        open(NAMELIST_PATH, mode='a', encoding='utf8', newline="\r\n") as g, \
        open(NAME_TO_AREA_PATH, mode='a', encoding='utf8', newline="\r\n") as h:
        for line in f:
            # if count > 10:
            #    break
            j = json.loads(line)
            g.write(dict_to_namelist(j) + '\n')
            h.write(dict_to_line_set(j) + '\n')
            count += 1
            if count % 100000 == 0:
                print(f"Processed {count} lines...")

    print(f"Finished with {count} lines")


if __name__ == "__main__":
    main()
