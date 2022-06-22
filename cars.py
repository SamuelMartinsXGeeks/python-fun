import json
from string import capwords


class Car:

    name = ""
    miles_per_gallon = 0
    cylinders = 0
    displacement = 0
    horsepower = 0
    weight_lbs = 0
    acceleration = 0
    year = 0
    origin = 0

    def __init__(self, name, miles_per_gallon, cylinders, displacement,
                 horsepower, weight_lbs, acceleration, year, origin):
        self.name = capwords(name)
        self.miles_per_gallon = miles_per_gallon
        self.cylinders = cylinders
        self.displacement = displacement
        self.horsepower = horsepower
        self.weight_lbs = weight_lbs
        self.acceleration = acceleration
        self.year = year
        self.origin = capwords(origin)

    def __repr__(self):
        return f"Vehicle '{self.name}'"


class CarCollection:

    def __init__(self):
        self.cars = list([])

    def add(self, new_car: Car):
        self.cars.append(new_car)

    def __repr__(self):
        car_count = len(self.cars)
        return f"Collection of {car_count} vehicles"

    def sort(self, attribute):
        if not hasattr(Car, attribute):
            return f"No such attribute '{attribute}'"

        # filtered = filter(lambda v: getattr(v, attribute) >
        #                   minimum_horsepower, self.cars)
        filtered = sorted(self.cars, key=lambda c: getattr(c, attribute))
        text = ""
        for car in filtered:
            text += f"{car.name} @ {getattr(car, attribute)} {capwords(attribute)}\n"
        return text


f = open('cars.json', encoding='UTF-8')
data = json.load(f)

carList = CarCollection()

for car in data:
    newCar = Car(car['Name'], car['Miles_per_Gallon'],
                 car['Cylinders'], car['Cylinders'], car['Displacement'],
                 car['Weight_in_lbs'], car['Acceleration'], car['Year'], car['Origin'])
    carList.add(newCar)

print(carList.sort("cylinders"))
print(carList.sort("displacement"))
