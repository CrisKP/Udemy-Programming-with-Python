# Required arguments (throw error if not passed in)
def calculate(x, y):
    return x + y

print(calculate(10, 20))

# Keyword arguments
def person_info(name, age):
    print('Name: {}'.format(name))
    print('Age: {}'.format(age))

person_info(age=30, name='Jack')

# Default arguments
def person_info(name, age='35'):
    print('Name: {}, Age: {}'.format(name, age))

person_info(age=30, name='Jack')
person_info(name='Jack')

# Variable-length arguments (defined here by the * before the arg name)
def print_scores(score, *scores):
    print('Test scores are:')
    print(score)
    for i in scores:
        print(i)

print_scores(10)
print_scores(20, 30, 40, 50)
