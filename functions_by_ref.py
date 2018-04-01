# Parameters are passed by referenced

vehicle = ['Dodge', 'Challenger']
def display_car(car):
    print('You have a', car[0], car[1])
    car[0] = 'Chevy'
    car[1] = 'Camaro'

display_car(vehicle)
print(vehicle[0], vehicle[1])
print(vehicle)
