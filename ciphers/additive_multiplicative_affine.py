def additive_cipher(s, key):
    s = ''.join(s.split())
    return ''.join([chr((((ord(i) - 97) + key) % 26) + 65) for i in s])

def multiplicative_cipher(s, key):
    s = ''.join(s.split())
    return ''.join([chr((((ord(i) - 97) * key) % 26) + 65) for i in s])

def affine_cipher(s, key):
    s = ''.join(s.split())
    return ''.join([chr((((ord(i) - 97) * key[0] + key[1]) % 26) + 65) for i in s])
    
print(additive_cipher("this is an exercise", 20))
print(multiplicative_cipher("this is an exercise", 15))
print(affine_cipher("this is an exercise", (15, 20)))
