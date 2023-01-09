#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
#Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
#Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
#metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
#Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
#Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    def __init__(self, low_floor, high_floor):
        self.low_floor = low_floor
        self.high_floor = high_floor
        self.floor = low_floor

    def move(self, floor):
        if floor >= self.low_floor and floor <= self.high_floor:
            while self.floor < floor:
                self.up()
            while self.floor > floor:
                self.down()


    def up(self):
        if (self.floor < self.high_floor):
            self.floor += 1
            print(f"Hissi on kerroksessa {self.floor}")

    def down(self):
        if (self.floor > self.low_floor):
            self.floor -= 1
            print(f"Hissi on kerroksessa {self.floor}")


e = Elevator(1, 5)
e.move(3)
e.move(1)
e.move(5)
e.move(100)
e.move(1)