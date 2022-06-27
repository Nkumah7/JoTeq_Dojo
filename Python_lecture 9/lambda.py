# Lambda Function - A small anonymous function

def add(a, b):
    return a + b

# print(add(1, 2))
# Syntax
# lambda arguments: expression
add = lambda a, b: a + b
# print(add(1, 2))

# sub = lambda a, b, c: a - b - c
# print(sub(4, 6, 7))

# def mul(n):
#     return lambda a: a * n

# # mul_2 = mul(2)
# print(mul(2)(3))

# lst = [2, 4, 6, 7, 9]
# lambda_lst = map(lambda a: a * 2 , lst)
# print(list(lambda_lst))