target1 = "パトカー"
target2 = "タクシー"
ans = ""

for a, b in zip(target1, target2):
    ans += a + b

print(ans)