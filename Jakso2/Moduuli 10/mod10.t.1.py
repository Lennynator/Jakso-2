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


h1=Hissi(1,5)
h1.siirrykerrokseen(4)