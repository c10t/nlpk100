import requests

SAVE_FILE = "./resources/artist.json.gz"
GET_URL = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz"

r = requests.get(GET_URL)

with open(SAVE_FILE, mode='wb') as f:
    f.write(r.content)
