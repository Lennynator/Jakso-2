import random

from tabulate import tabulate

Autot=[]


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



class Kisa:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat
        print(f"Tervetuloa kisaan {nimi}. Kilpailin pituus on {pituus} ja siihen osallistuu {osallistujat} autoa. Kisa alkakoon!")

        for i in range(osallistujat):
            auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
            Autot.append(auto)

    def tunti_kuluu(self):
        self.tunnit = 0
        for i in Autot:
            i.kiihdytä(random.randint(-10, 15))
            i.kulje(1)
        self.tunnit += 1
        if self.tunnit%10 == 0:
            self.tulosta_tilanne()




    def tulosta_tilanne(self):
        tuloste = []
        for i in Autot:
            tuloste.append([i.rekisteri, i.kuljettumatka, i.nopeus, i.huippunopeus])
        print(tabulate(tuloste, ['Rekkari', 'matka', 'nopeus', 'huiput']))

    def kilpailu_ohi(self):
        for n in Autot:
            if n.kuljettumatka > self.pituus:
                print(f"Voittaja oli auto {n.rekisteri}")
                print(f"Huippunopeus oli {n.huippunopeus}")
                self.tulosta_tilanne()
                return True




k=Kisa("Suuri Romuralli",8000,10)

while not Kisa.kilpailu_ohi(k):
    k.tunti_kuluu()
    k.kilpailu_ohi()




