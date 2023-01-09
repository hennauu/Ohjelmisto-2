#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
#Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
#Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
#Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
#Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
#Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
#Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Car:
    def __init__(self, reg, top_speed):
        self.reg_number = reg
        self.top_speed = top_speed
        self.speed = 0
        self.odometer = 0

    def accelerate(self, delta_speed):
        if self.top_speed >= delta_speed + self.speed > 0:
            self.speed = self.speed + delta_speed
        elif delta_speed + self.speed > self.top_speed:
            self.speed = self.top_speed
        else:
            self.speed = 0

    def drive(self, hours):
        self.odometer += self.speed * hours

class ElectricCar(Car):
    def __init__(self, reg, top_speed, capacity_kwh):
        self.capacity_kwh = capacity_kwh
        super().__init__(reg, top_speed)

class IceCar(Car):
    def __init__(self, reg, top_speed, gastank_litre):
        self.gastank_litre = gastank_litre
        super().__init__(reg, top_speed)


#    def print_info(self):
#        print(f"Auton rekisterinumero: {self.reg_number}, auton huippunopeus: {self.top_speed} km/h, "
#              f"auton nopeus: {self.speed}, auton kuljettu matka: {self.odometer} km.")


electric_car = ElectricCar("ABC-15", 180, 52.5)
ice_car = IceCar("ACD-123", 165, 32.3)

electric_car.accelerate(80)
ice_car.accelerate(40)

electric_car.drive(3)
ice_car.drive(3)

print(f"Sähköauton matkamittarilukema on {electric_car.odometer} km.")
print(f"Polttomoottoriauton matkamittarilukema on {ice_car.odometer} km.")