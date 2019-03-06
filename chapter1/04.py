target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = target.strip('.,').split()
result = {}

for (i, word) in enumerate(words, 1):
    if i in num:
        result[word[:1]] = i
    else:
        result[word[:2]] = i

print(result)