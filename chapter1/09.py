import random
 
def Typoglycemia(target):
    result = []
    for word in target.split():
        if len(word) <= 4:
            result.append(word)
        else:
            result.append(word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1])
    return ' '.join(result)
 
# 対象文字列の入力
target = input('文字列を入力してください--> ')
 
# タイポグリセミア
result = Typoglycemia(target)
print('変換結果:' + result)