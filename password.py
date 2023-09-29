import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
prluzunluk = (int(input("parola kaç karakter?")))
sifre = ""
for i in range(prluzunluk):
    sifre += random.choice(karakter)

print (sifre)
