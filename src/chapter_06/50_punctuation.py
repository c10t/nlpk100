def split_to_sentences(line):
    eos = {".", ";", ":", "?", "!"}

    if eos & set(line) == set():
        return [line]

    sentences = []
    sentence = ""
    for i, _ in enumerate(line):
        sentence += line[i]
        if line[i] in eos:
            if len(line) <= i + 2:
                sentences.append(sentence.lstrip())
                break
            if line[i + 1] == " " and line[i + 2].isupper():
                sentences.append(sentence.lstrip())
                sentence = ""

    return sentences


def main():
    file_path = './resource/nlp.txt'

    with open(file_path, encoding='utf-8') as nlp:
        for line in nlp.readlines():
            if len(line.strip()) < 2:
                continue
            for s in split_to_sentences(line):
                print(s)


if __name__ == '__main__':
    main()