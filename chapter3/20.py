import gzip
import json

with gzip.open("jawiki-country.json.gz") as f:
    for line in f:
        l = json.loads(line)
        if l["title"] == "イギリス":
            print(l["text"])
            break
