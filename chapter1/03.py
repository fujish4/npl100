target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = target.rstrip(',.').split()

ans = [len(i) for i in words]

print(ans)