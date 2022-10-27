import random

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

for i in range(10):
    auto = Auto(f"ABC-{i+1}",random.randint(100,200))
    Autot.append(auto)

for i in Autot:
    while not i.kuljettumatka == 1000:
        for i in Autot:
            i.kiihdytä(random.randint(-10,15))
            i.kulje(1)

for i in Autot:
    print(f"Auton rekisteri on {i.rekisteri:}, huippunopeus on {i.huippunopeus:} km/h, tämän hetkinen nopeus {i.nopeus:} ja kuljettu matka {i.kuljettumatka}.")
