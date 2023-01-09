#Tehtävä 1
#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
#Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
#Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
#Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
#Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, reg, top_speed, speed_now, journey):
        self.reg = reg
        self.top_speed = top_speed
        self.speed_now = speed_now
        self.journey = journey


new_car = Car("ABC-123", 142, 0, 0)
print("Auton ominaisuudet")
print(f"Rekisterinumero: {new_car.reg:s}")
print(f"Huippunopeus: {new_car.top_speed:d} km/h ")
print(f"Tämänhetkinen nopeus: {new_car.speed_now:d} km/h")
print(f"Kuljettu matka: {new_car.journey:d} km")