##### Decimal
# from decimal import Decimal

# first_value = 0.2 + 0.4 - 0.5 + 0.2
# print(first_value)

# second_value = Decimal('0.2') + Decimal('0.4') - Decimal('0.5') + Decimal('0.2')
# print(second_value)

#### getcontext
# from decimal import Decimal, getcontext

# value = Decimal('2') / Decimal('3')
# print(value)

# print(round((2/3),5))
# getcontext().prec = 5
# second_value = Decimal('2') / Decimal('3')
# print(second_value)
# second_value = Decimal('1') / Decimal('3')
# print(second_value)
# second_value = Decimal('4') / Decimal('3')
# print(second_value)
# second_value = Decimal('140') / Decimal('3')
# print(second_value)

# getcontext().prec = 3
# second_value = Decimal('140') / Decimal('3')
# print(second_value)

### ROUND_HALF_UP, ROUND_HALF_EVEN

# from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_HALF_EVEN

# number = Decimal('1.453')
# print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))
# print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))
# print(Decimal('3.14567934').quantize(Decimal('1.0000')))

# print(int(number))
# print(float(number))


####### use real numbers
from decimal import Decimal

number_one = 1.37
number_two = 1.5

first = Decimal.from_float(number_one)
print(first)
second = Decimal.from_float(number_two)
print(second)

first_str = Decimal(str(number_one))
print(first_str)
second_str = Decimal(str(number_two))
print(second_str)