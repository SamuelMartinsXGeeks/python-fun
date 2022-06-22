# importing the required module
from itertools import count
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
                lst.append(car)
                dictionary[key] = lst
            else:
                dictionary[key] = list([car])
        return dictionary


f = open('cars.json', encoding='UTF-8')
data = json.load(f)

carList = CarCollection()

for car in data:
    newCar = Car(car['Name'], car['Miles_per_Gallon'],
                 car['Cylinders'], car['Cylinders'], car['Displacement'],
                 car['Weight_in_lbs'], car['Acceleration'], car['Year'], car['Origin'])
    carList.add(newCar)

sorted_by_year = carList.sorted_list_by('year')
sorted_by_cylinders = carList.sorted_list_by('cylinders')

# x axis values
x = sorted_by_year.keys()
# corresponding y axis values
y = []

y_weight = []
y_cylinders = []

for key in sorted_by_year.keys():
    average_horsepower = 0
    average_weight_lbs = 0
    average_cylinders = 0
    for car in sorted_by_year[key]:
        average_horsepower += car.horsepower
        average_weight_lbs += car.weight_lbs
        average_cylinders += car.cylinders
    cnt = len(sorted_by_year[key])
    average_horsepower /= cnt
    average_cylinders /= cnt
    average_weight_tons = (0.45359237 * average_weight_lbs/cnt)/1000
    y.append(average_horsepower)
    y_weight.append(average_weight_tons*170)
    y_cylinders.append(average_cylinders * 50)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y, label="Avg. Horse Power")
ax1.plot(x, y_weight, label="Avg. Weight")
ax1.plot(x, y_cylinders, label="Avg. Cylinders")
ax1.set_title(
    "Blue: Horsepower\nOrange: Weight\nGreen: Cylinders")

x = sorted(sorted_by_cylinders.keys())
y = []

cyl_mpg_keys = sorted(sorted_by_cylinders)
for key in cyl_mpg_keys:
    average_mpg = 0
    cnt = 0  # incremented manually, some cars do not have mpg data
    for car in sorted_by_cylinders[key]:
        if car.miles_per_gallon is None:
            continue
        average_mpg += car.miles_per_gallon
        cnt += 1
    # convert mpg to l/100km
    average_liter_per_100km = 235.215/(average_mpg/cnt)
    y.append(average_liter_per_100km)

ax2.plot(x, y, 'tab:red')
ax2.set_title("Cylinders vs L/100 Km")

# function to show the plot
plt.legend()
plt.show()
