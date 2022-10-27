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



auto = Auto("ABC-123",142)
auto.kiihdytä(60)
auto.kulje(1.5)
print(f"Auton rekisteri on , {auto.rekisteri} huippunopeus on {auto.huippunopeus} km/h, tämän hetkinen nopeus {auto.nopeus} ja kuljettu matka {auto.kuljettumatka}.")


