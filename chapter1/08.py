def cipher(target):
    result = ''
    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result
 
before = input()
after = cipher(before)
decryption = cipher(after)
 
print(before)
print(after)
print(decryption)