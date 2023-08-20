from random import randint as generate_number, choice
import calculator
from person import Person
from decouple import config

print(generate_number(2, 5))
print(calculator.addition(1, 6))
print(calculator.multiplication(10, 6))

my_friend = Person('Jim', 19)
print(my_friend)

print(config('DATABASE_URL'))

commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
# Bye Sensei!
