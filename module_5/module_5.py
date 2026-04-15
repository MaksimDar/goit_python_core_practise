# from collections import namedtuple

# Point = namedtuple('Point', ["name", 'y'])
# p = Point(11, y=22)
# print(p.name)
# print(p.y)

# import collections

# # Створення іменованого кортежу Person
# Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# # Створення екземпляра Person
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# # Виведення різних атрибутів іменованого кортежу
# print(person.first_name)       
# print(person.post_index) 
# print(person.age)        
# print(person[3])         

# import collections

# student_marks = [3,4,4,5,6,6,5,4,3,2,1,4]

# mark_counts = collections.Counter(student_marks)
# print(mark_counts)
# print(mark_counts.most_common(2))

########## defaultdict
# import collections
# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

#### alternative to the previous example:
# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)
# print(grouped_words)
# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))


######## deque work


# from collections import deque

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]

# # Ініціалізація черги завдань
# task_queue = deque()

# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")

##### decimal, getcontext().prec
# from decimal import Decimal, getcontext

# getcontext().prec = 7
# print(Decimal("44") / Decimal("567"))

####### yield

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3

# from typing import Callable

# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def apply_operation(a: int, b: int, operation: Callable[[float, float], int]) -> int:
#     return operation(a, b)

# # Використання
# result_add = apply_operation(5.4, 3.3, add)
# result_multiply = apply_operation(5.4, 3.3, multiply)

# print(result_add, result_multiply)

# from typing import Callable

# def power(exponent: int):
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання
# square = power(2)
# cube = power(3)

# print(square(4)) 
# print(cube(4))


# from typing import Callable, Dict

# # Визначення функцій
# def add(a: int, b: int) -> int:
#     return a + b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def power(exponent: int) -> Callable[[int], int]:
#     def inner(base: int) -> int:
#         return base ** exponent
#     return inner

# # Використання power для створення функцій square та cube
# square = power(2)
# cube = power(3)

# # Словник операцій
# operations: Dict[str, Callable] = {
#     'add': add,
#     'multiply': multiply,
#     'square': square,
#     'cube': cube
# }

# # Використання операцій
# result_add = operations['add'](10, 20)  # 30
# result_square = operations['square'](5)  # 25

# print(result_add)  
# print(result_square)  

# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function

# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()

########### currying
# def add(a):
#     def add_b(b):
#         return a + b
#     return add_b

# # Використання:
# add_5 = add(5)
# result = add_5(10)
# print(result)

# def apply_discount(price: float, discount_percentage: int) -> float:
#     return price * (1 - discount_percentage / 100)

# # Використання
# discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
# print(discounted_price)

# discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
# print(discounted_price)

# from typing import Callable

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Каррінг в дії
# ten_percent_discount = discount(10)
# twenty_percent_discount = discount(20)
# # print(ten_percent_discount)
# # Застосування знижок
# discounted_price = ten_percent_discount(500)  # 450.0
# print(discounted_price)

# discounted_price = twenty_percent_discount(500)  # 400.0
# print(discounted_price)

####### advanced curring with creating a dict function
# from typing import Callable, Dict

# def discount(discount_percentage: int) -> Callable[[float], float]:
#     def apply_discount(price: float) -> float:
#         return price * (1 - discount_percentage / 100)
#     return apply_discount

# # Створення словника з функціями знижок
# discount_functions: Dict[str, Callable] = {
#     "10%": discount(10),
#     "20%": discount(20),
#     "30%": discount(30)
# }

# # Використання функції зі словника
# price = 500
# discount_type = "20%"

# discounted_price = discount_functions[discount_type](price)
# print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

####### Using decorators 
# def logger(func):
#     def inner(x: int, y: int) -> int:
#         print(f"Викликається функція: {func.__name__}: {x}, {y}")
#         result = func(x, y)
#         print(f"Функція {func.__name__} завершила виконання: {result}")
#         return result

#     return inner
# @logger
# def complicated(x: int, y: int) -> int:
#     return x + y
# print(complicated(2, 3))

########### COMPREHENSIONS
####List comprehensions

# even_sq = [x**4 for x in range(1,8) if x % 2 == 0]
# print(even_sq)

##### Set comprehensions
# items = [1,2,2,3,4,5,6,6,4,3]
# even_sq = {item**2 for item in items}
# print(even_sq)

#### Dictionary comprehensions
# items = [1,2,2,3,4,5,6,6,4,3]
# sq_dict = {f'{x}': x**2 for x in items if x % 2 != 0}
# print(sq_dict)

#### lambda functions:
# multiplication =lambda x,y,z: print(x*y*z)
# multiplication(4,5,6)

# nums = [1, 2, 3, 4, 5]
# nums_sorted = sorted(nums, key=lambda x: -x)
# print(nums_sorted)

### map in lambda

# num_1 = [1,2,3,4,5]
# num_2 = [6,5,4,3,2]
# multiply_nums = list(map(lambda x,y: x*y,num_1,num_2))
# print(multiply_nums)
##+++++======> analogy to comprehensions

# num_1 = [1,2,3,4,5]
# squared = [x**2 for x in num_1]
# print(squared)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)


















