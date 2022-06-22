# importing the required module
from operator import indexOf
import matplotlib.pyplot as plt

import json
from string import capwords
from datetime import datetime

from numpy import array


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
        self.year = datetime.strptime(year, '%Y-%m-%d').year
        self.origin = capwords(origin)

    def __repr__(self):
        return f"{self.name}"


class CarCollection:

    cars = list([])

    def __init__(self):
        self.cars = list([])

    def add(self, new_car: Car):
        self.cars.append(new_car)

    def __repr__(self):
        car_count = len(self.cars)
        return f"Collection of {car_count} vehicles"

    def sorted_list_by(self, attribute):
        if not hasattr(Car, attribute):
            return f"No such attribute '{attribute}'"
        dictionary = {}
        for car in self.cars:
            key = str(getattr(car, attribute))
            if key in dictionary:
                lst = list(dictionary[key])
                list(dictionary[key]).append(car.name)
                dictionary[key] = list(dictionary[key]).append(car.name)
            else:
                dictionary[key] = list([car.name])
        return dictionary


f = open('cars.json', encoding='UTF-8')
data = json.load(f)

carList = CarCollection()

for car in data:
    newCar = Car(car['Name'], car['Miles_per_Gallon'],
                 car['Cylinders'], car['Cylinders'], car['Displacement'],
                 car['Weight_in_lbs'], car['Acceleration'], car['Year'], car['Origin'])
    carList.add(newCar)

print(carList.sorted_list_by('year'))

# # x axis values
# x = [1, 2, 3]
# # corresponding y axis values
# y = [2, 4, 1]

# # plotting the points
# plt.plot(x, y)

# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')

# # giving a title to my graph
# plt.title('My first graph!')

# # function to show the plot
# plt.show()
