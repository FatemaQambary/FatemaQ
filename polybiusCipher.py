#polybius cipher encryption
plaintxt=input("please enter ur plaintxt: ")

def play(plaintxt):
    for i in plaintxt:
        row=(int((ord(i)-ord("a"))/5))+1
        col=(int((ord(i)-ord("a"))%5))+1
        print(row,col)
print(play(plaintxt))

#polybius cipher decryption
ciphertxt=input("please enter ur plaintxt: ")

def decrypt(ciphertxt):
    for i in ciphertxt:
        row=(int((ord(i)-ord("a"))/5))+1
        col=(int((ord(i)-ord("a"))%5))+1
        print(row,col)
print(decrypt(ciphertxt))
