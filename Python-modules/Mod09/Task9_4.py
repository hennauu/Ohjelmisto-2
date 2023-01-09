#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
#Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
#Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
#Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
#Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Car:
    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed_now = 0
        self.journey = 0

    def accelerate(self, speed_change):
        self.speed_now = self.speed_now + speed_change
        if self.speed_now < 0:
            self.speed_now = 0
        elif self.top_speed < self.speed_now:
            self.speed_now = self.top_speed

    def drive(self, hours):
       self.journey = self.journey + hours * self.speed_now

cars = []

for i in range(10):
    cars.append(Car("ABC-" + str(i+1), random.randint(100, 200)))


done = False
while not done:
    for i in cars:
        i.accelerate(random.randint(-10, 15))
        i.drive(1)
        if i.journey >= 10000:
            done = True


for car in cars:
    print(f"Auton {car.reg} huippunopeus: {car.top_speed} km/h, nykyinen nopeus {car.speed_now} km/h, "
          f"kuljettu matka: {car.journey} km.")