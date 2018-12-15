import json
from pathlib import Path

RESOURCES_PATH = Path.cwd().parent/"resources"
ARTIST_PATH = RESOURCES_PATH/"artist.json"


def dict_to_line_set(d):
    return 'SET "name:{}" "area:{}"'.format(d['name'], d['area'])


def dict_to_namelist(d):
    return 'RPUSH namelist "{}"'.format(d['name'])


def io_write_chunk(path_namelist, path_name_area, name_area_list):
    with path_namelist.open(mode='a', encoding='utf8', newline="\r\n") as g, \
        path_name_area.open(mode='a', encoding='utf8', newline="\r\n") as h:
        for line in name_area_list:
            g.write(dict_to_namelist(line) + '\n')
            h.write(dict_to_line_set(line) + '\n')


def main():
    print("Reading JSON file...")

    with ARTIST_PATH.open(encoding="utf8") as f:
        count = 0
        page = 1
        namelist = "namelist-{}.txt".format(str(page).zfill(3))
        name_area = "name-to-area-{}.txt".format(str(page).zfill(3))
        chunk = []

        for line in f:

            j = json.loads(line)
            if "name" not in j.keys():
                continue

            item = {'name': j['name'], 'area': j['area'] if 'area' in j.keys() else '---'}
            chunk.append(item)

            count += 1
            if count % 100000 == 0:
                io_write_chunk(RESOURCES_PATH / namelist, RESOURCES_PATH / name_area, chunk)
                chunk = []
                page += 1
                namelist = "namelist-{}.txt".format(str(page).zfill(3))
                name_area = "name-to-area-{}.txt".format(str(page).zfill(3))
                print(f"Processed {count} lines...")

        # write residue
        io_write_chunk(RESOURCES_PATH / namelist, RESOURCES_PATH / name_area, chunk)

    print(f"Finished with {count} lines")


if __name__ == "__main__":
    main()
