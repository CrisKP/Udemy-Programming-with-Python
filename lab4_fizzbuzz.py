# If a number is divisible by 3 and 5, print FizzBuzz, if it's only divisible by 3 print Fizz, if it's only divisible by 5 print Buzz. Otherwise, print the number.

for n in range(1, 101, 1):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
