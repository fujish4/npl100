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


pattern1 = re.compile(r'^\{\{基礎情報(.*?)^\}\}$', re.MULTILINE + re.VERBOSE + re.DOTALL)
contents = pattern1.findall(extractUK())

print(contents)

pattern2 = re.compile(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))''', re.MULTILINE + re.VERBOSE + re.DOTALL)
fields = pattern2.findall(contents[0])
