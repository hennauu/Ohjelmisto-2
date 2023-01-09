#Tehtävä 3
#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
#Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
#Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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


car1 = Car("ABC-123", 142)

car1.journey = 2000
car1.accelerate(60)
car1.drive(1.5)
print(car1.journey)