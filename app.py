numbers = [12,54,11,76,34,199,59,23,65,89,100,99,101,45,32,34]
print(numbers)

def filter_greater_than_hundred(numbers): 
    return filter(lambda n: n>100, numbers)
 
print(list(filter(lambda n: n > 100,numbers)))