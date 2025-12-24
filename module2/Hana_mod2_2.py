def encrypt_string(word:str):
    encrypted=""
    enc=[]
    for h in word:
        enc.append(str(ord(h)))
    return ",".join(enc)

print(encrypt_string("Hana"))

#I encrypted my name into integer numbers
#so 72 represents H,97 as A,N as 110,97 as A .