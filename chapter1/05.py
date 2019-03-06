def n_gram(target, n):
    result = []
    for i in range(len(target) - n + 1):
        result.append(target[i:i+n])
    return result

target = "I am an NLPer"
print(n_gram(target.split(), 2))
print(n_gram(target, 2))
