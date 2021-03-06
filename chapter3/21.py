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

pattern = re.compile(r"\[\[Category:.*\]\]", re.MULTILINE + re.VERBOSE)

for line in extractUK().split("\n"):
    if pattern.match(line):
        print(line)
