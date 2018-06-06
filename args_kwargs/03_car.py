class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

def BlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'
