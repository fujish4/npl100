def n_gram(target, n):
    result = []
    for i in range(len(target) - n + 1):
        result.append(target[i:i+n])
    return result
 
target1 = "paraparaparadise"
target2 = "paragraph"
 
set_t1 = set(n_gram(target1, 2))
set_t2 = set(n_gram(target2, 2))
 
print(set_t1)
print(set_t2)
print(set_t1 | set_t2)
print(set_t1 & set_t2)
print(set_t1 - set_t2)