import codecs

neg = './resources/rt-polaritydata/rt-polarity.neg'
pos = './resources/rt-polaritydata/rt-polarity.pos'

with codecs.open(pos, mode='r', encoding='utf-8', errors='ignore') as f:
    print(f'rt-polarity.pos: {len(f.readlines())} lines')

with codecs.open(neg, mode='r', encoding='utf-8', errors='ignore') as f:
    print(f'rt-polarity.neg: {len(f.readlines())} lines')

with open('./resources/sentiment.txt') as f:
    pos_count = 0
    neg_count = 0
    for line in f.readlines():
        if line.startswith('+1'):
            pos_count += 1
        if line.startswith('-1'):
            neg_count += 1

print(f'pos: {pos_count} / neg: {neg_count}')
