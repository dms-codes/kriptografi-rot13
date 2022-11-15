import string

plaintext = 'SELAMAT DATANG DI KELAS KRIPTOGRAFI'

def encrypt(plaintext):
    ciphertext = ''
    for p in plaintext:
        if p == ' ': c = ' '
        else:
            index = string.ascii_uppercase.index(p)
            if index > 12:
                index = index - 13
            else: index = index + 13
            c = string.ascii_uppercase[index]
        ciphertext += c
    return ciphertext

ciphertext = encrypt(plaintext)
print(ciphertext)
print(encrypt(ciphertext))
