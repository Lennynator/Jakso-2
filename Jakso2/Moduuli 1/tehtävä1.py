class Auto:

    matkajanopeusalussa = 0

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri=rekisteri
        self.huippunopeus=huippunopeus
        self.tämänhetkinennopeus=Auto.matkajanopeusalussa
        self.kuljettumatka=Auto.matkajanopeusalussa




auto = Auto("ABC-123","142 km/h")

print(f"Auton rekisteri on {auto.rekisteri:}, huippunopeus on {auto.huippunopeus:}, tämän hetkinen nopeus {auto.tämänhetkinennopeus:} ja kuljettu matka {auto.kuljettumatka}.")



