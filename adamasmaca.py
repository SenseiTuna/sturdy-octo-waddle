import random
from wordlist import word_list

kelime = random.choice(word_list)

goruntu = "_"*len(kelime)
print(goruntu)

can = 7

while can > 0:
    harftahmin = str(input("Bir harf tahmin ediniz: \n").lower())
    i = 0
    a = 0
    while i < len(kelime):
        if harftahmin == kelime[i]:
            listgoruntu = list(goruntu)
            listgoruntu[i] = harftahmin
            goruntu = "".join(listgoruntu)
            i += 1
            if goruntu == kelime:
                print("Kazandınız! Şu canla kazandınız: ",can)
                can = 0
                break
        else:
            i += 1
            a += 1
            if a == len(kelime):
                can -= 1
                print("Yanlış tahmin yaptınız, kalan canınız: ", can)
                if can == 0:
                    print("Kaybettiniz! Asıl kelime: ", kelime)
                    break
    print("Son denemeniz: ", goruntu)