import gzip
import json
import re

fileName = "jawiki-country.json.gz"

def extractUK():
    with gzip.open(fileName) as f:
        for line in f:
            l = json.loads(line)
            if l["title"] == "イギリス":
                return l["text"]

pattern = re.compile(r"File:(.*?)\|", re.MULTILINE + re.VERBOSE)
result = pattern.findall(extractUK())

for line in result:
    print(line)