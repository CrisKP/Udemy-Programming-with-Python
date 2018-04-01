# Print number in range and if it is even or odd.

for num in range (1, 21):
    if num % 2 == 0:
        print(num, 'Even')
    else:
        print(num, 'Odd')

# --------------------------------------------

for num in range (1, 21):
    if num % 2 == 0:
        print('{} {}'.format(num, 'Even'))
    else:
        print('{} {}'.format(num, 'Odd'))
