class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirrykerrokseen(self, kohdekerros):
        if kohdekerros < self.alinkerros or kohdekerros > self.ylinkerros:
            print("Kerrosta ei ole")
            return
        while self.kerros < kohdekerros:
            self.kerros_ylos()
        while self.kerros > kohdekerros:
            self.kerros_alas()
            return

    def kerros_alas(self):
        self.kerros -=1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

class Talo:
    def __init__(self, alinkerros, ylinkerros, lkm):
        self.alinkerros = alinkerros
        self.hissit = []
        for luku in range(lkm):
            self.hissit.append(Hissi(alinkerros,ylinkerros))
        print(f"Talossa on {lkm} hissiä.")

    def aja_hissia(self, numero, kohdekerros):
        print(f"Ajetaan hissillä {numero}")
        self.hissit[numero-1].siirrykerrokseen(kohdekerros)

talo1=Talo(1,5,3)

talo1.aja_hissia(1,4)
talo1.aja_hissia(2,2)
talo1.aja_hissia(3,5)


