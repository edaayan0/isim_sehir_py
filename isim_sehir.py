# 4 soru olacak, her biri 25 puan
# her doğru soru +25 puan, yanlış sorular 0 puan
import random
import string
letter=random.choice(string.ascii_uppercase)
isim=input(f"{letter} harfi ile başlayan bir isim girin:")
sehir=input(f"{letter} harfi ile başlayan bir şehir girin:")
bitki=input(f"{letter} harfi ile başlayan bir bitki girin:")
esya=input(f"{letter} harfi ile başlayan bir eşya girin:")
puan=0
cevap= [isim,sehir,bitki,esya]

for girdi in cevap:
    if girdi[0].capitalize()==letter:
        puan += 25


print("Toplam Skorunuz: "+ str(puan))
