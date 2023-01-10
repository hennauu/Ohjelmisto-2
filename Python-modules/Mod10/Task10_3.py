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


class House:
  def __init__(self, low_floor, high_floor, elevators):
    self.low_floor = low_floor
    self.high_floor = high_floor
    self.elevators = elevators
    self.elevators = [Elevator(low_floor, high_floor) for i in range(elevators)]

  def move_elevator(self, elenum, desfloor):
    self.elevators[elenum - 1].move(desfloor)


  def alarm(self):
        for elevator in self.elevators:
            elevator.move(self.low_floor)


house1 = House(1, 5, 2)
house1.move_elevator(2, 4)
house1.alarm()