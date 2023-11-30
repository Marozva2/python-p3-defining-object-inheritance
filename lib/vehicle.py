class Vehicle:
    '''A class representing a generic vehicle.'''

    def __init__(self, wheel_size: int, wheel_number: int):
        '''Initialize a new Vehicle instance.'''
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        '''Simulate the vehicle's movement.'''
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        '''Simulate filling up the vehicle's tank.'''
        return "filling up!"
