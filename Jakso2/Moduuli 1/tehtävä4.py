import random

from tabulate import tabulate
class Auto:

    matkajanopeusalussa = 0

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = Auto.matkajanopeusalussa
        self.kuljettumatka = Auto.matkajanopeusalussa

    def kiihdytä(self, muutosnopeus):
        self.nopeus = self.nopeus + muutosnopeus
        self.kuljettumatka = self.kuljettumatka + muutosnopeus
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettumatka = self.kuljettumatka * tunnit

Autot=[]

kisa = True

for i in range(10):
    auto = Auto(f"ABC-{i+1}",random.randint(100,200))
    Autot.append(auto)

while kisa:
    for i in Autot:
        i.kiihdytä(random.randint(-10, 15))
        i.kulje(1)
        if i.kuljettumatka > 10000:
            print(f"Voittaja oli auto {i.rekisteri}")
            print(f"Huippunopeus oli {i.huippunopeus}")
            kisa = False


tuloste = []
for i in Autot:
    tuloste.append([i.rekisteri,i.kuljettumatka,i.nopeus,i.huippunopeus])

print(tabulate(tuloste,['Rekkari','matka','nopeus','huiput']))