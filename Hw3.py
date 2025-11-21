class TransportVehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self):
        return f"The {self.__class__.__name__} is moving at {self.speed} km/h."
class Moped(TransportVehicle):
    pass
class SportsCar(TransportVehicle):
    def __init__(self, speed, seats=2):
        super().__init__(speed)
        self.seats = seats
class Bus(TransportVehicle):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.capacity = capacity
moped = Moped(50)
sports_car = SportsCar(250)
bus = Bus(80, 50)

print(moped.move())
print(sports_car.move(), f"(Seats: {sports_car.seats})")
print(bus.move(), f"(Capacity: {bus.capacity})")
