#Tehtävä 2
#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
#Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
#Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
#Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
#Tulosta tämän jälkeen auton nopeus.Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
#Kuljettua matkaa ei tarvitse vielä päivittää.


class Car:
    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed_now = 0
        self.journey = 0

    def accelerate(self, speed_change):
        if self.top_speed >= speed_change + self.speed_now > 0:
         self.speed_now = self.speed_now + speed_change
        elif speed_change + self.speed_now > self.top_speed:
            self.speed_now = self.top_speed
        else:
            self.speed_now = 0


driving_car = Car("ABC-123", 142)

driving_car.accelerate(30)
print(f"Auton nopeus 1. kiihdytyksen jälkeen: {driving_car.speed_now:d} km/h")

driving_car.accelerate(70)
print(f"Auton nopeus 2. kiihdytyksen jälkeen: {driving_car.speed_now:d} km/h")

driving_car.accelerate(50)
print(f"Auton nopeus 3. kiihdytyksen jälkeen: {driving_car.speed_now:d} km/h")

driving_car.accelerate(-200)
print(f"Auton nopeus jarrutuksen jälkeen: {driving_car.speed_now} km/h")