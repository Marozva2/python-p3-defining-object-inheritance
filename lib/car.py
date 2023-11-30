from vehicle import Vehicle


class Car(Vehicle):
    '''A class representing a car, inheriting from Vehicle.'''

    def __init__(self, wheel_size: int, wheel_number: int):
        '''Initialize a new Car instance.'''
        super().__init__(wheel_size, wheel_number)

    def go(self):
        '''Simulate the car's movement.'''
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    def fill_up_tank(self):
        '''Simulate filling up the car's tank.'''
        return super().fill_up_tank()
