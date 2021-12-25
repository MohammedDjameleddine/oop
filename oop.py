class Rectangel(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class Vehicle(object):
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

class Vehicle(object):
    pass

class Bus(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
