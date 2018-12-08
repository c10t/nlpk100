import os
import gzip

FILE_PATH = './resources/artist.json.gz'
SAVE_PATH = './resources/artist.json'

with gzip.open(FILE_PATH, 'rb') as f:
    content = f.read()
    with open(SAVE_PATH, 'wb') as j:
        j.write(content)
