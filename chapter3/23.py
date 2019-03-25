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

pattern = re.compile(r"(==+)(.*?)==+", re.MULTILINE + re.VERBOSE)
result = pattern.findall(extractUK())

for line in result:
    level = len(line[0]) - 1
    print('{}{}({})'.format('\t' * (level - 1), line[1], level))