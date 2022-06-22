# from module_name import module
from datetime import datetime
import random
from decimal import Decimal
from calculator import add

# Datetime
# print(datetime.now().month)

# Random
random_fruits = ["apple", "banana", "pineapple", "mango", "orange"]
# print(random.choice(random_fruits))

# print(random.randint(1, 100))

# List Comprehension
# lst = list(range(1, 100))
# new_list = []
# for x in lst:      
#     if x % 2 == 0: 
#         x += 5       
#         new_list.append(x)
    
# print(new_list)
# # list = [operation | for temporary variable in list | (condition)]
# new_list_2 = [x + 5 for x in lst if x % 2 == 0]
# print(new_list_2)


# rand_numbers = []

# for _ in range(101):
#     rand_number = random.randint(1, 101)
#     rand_numbers.append(rand_number)
    
# print(rand_numbers)

# rand_list = [random.randint(1, 100) for x in range(101)]
# print(rand_list)

cost_of_kolanut = Decimal('0.10')
cost_of_maggi = Decimal('0.35')

# print(cost_of_kolanut + cost_of_maggi)

print(add(2, 3))