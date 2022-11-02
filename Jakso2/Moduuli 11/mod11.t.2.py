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

class Sahkoauto(Auto):

    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteri,huippunopeus)

    def kulje(self,tunnit):
        super().kulje(tunnit)

    def kiihdytä(self, muutosnopeus):
        super().kiihdytä(muutosnopeus)


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteri, huippunopeus, bensatankin_koko):
        self.bensatakin_koko = bensatankin_koko
        super().__init__(rekisteri,huippunopeus)

    def kulje(self,tunnit):
        super().kulje(tunnit)

    def kiihdytä(self,muutosnopeus):
        super().kiihdytä(muutosnopeus)

Autot = []


auto = Sahkoauto(f"ABC-15", 180, 52.5)
auto2= Polttomoottoriauto(f"ACD-123", 165,32.3)

Autot.append(auto)
Autot.append(auto2)

auto.kiihdytä(60)
auto.kulje(3)
auto2.kiihdytä(60)
auto2.kulje(3)
for i in Autot:
    print(f"Auton rekisteri on {i.rekisteri} huippunopeus on {i.huippunopeus} km/h, tämän hetkinen nopeus {i.nopeus}, kuljettu matka {i.kuljettumatka}.")


