class Julkaisu:

    def __init__(self,nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkisun nimi: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self,nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan on kirjoittanut {self.kirjoittaja}")
        print(f"Kirjassa on {self.sivumaara} sivua.")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja on{self.paatoimittaja}")

julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6","Rosa Liksom",200))
julkaisut.append(Lehti("Aku Ankka"," Aki Hyyppä"))

for t in julkaisut:
    t.tulosta_tiedot()


