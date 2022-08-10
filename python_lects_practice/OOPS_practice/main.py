from cmath import nan
from car_class import car


# audiq7 = car()

# audiq7.mileage = 30
# audiq7.year = 2020
# audiq7.make = 325


# print(audiq7.make, audiq7.year)
# print(type(audiq7))

nano = car(10, 2020, 325, 's1pro')
audi = car(23, 2001, 674, 'Q7')

print(nano.mileage)
print(type(nano.mileage), type(audi.mileage))

print("Age of nano is " + str(nano.age(2022)) + " years")