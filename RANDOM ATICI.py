import random


print("""

welcome to laugmeter how many words did you laugh:


""")

alf=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","u","ü","v","y","z"]

ks=input("randomunuz için karakter sayısı giriniz:")



yenirandom=list()


while True:

 harf=random.choice(alf)
 yenirandom.append(str(harf))
 hs=str(len(yenirandom))
 if(hs!=ks):
   continue
 else:
    break




print(*yenirandom,sep='')

print(*alf,sep='')
















