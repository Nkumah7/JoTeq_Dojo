import statistics
# Syntax
# def name_of_function():
    # code 
    
# def greeting():
#     print("How fa")
#     x = 10
#     y = 5
#     print(x - y)
    
# greeting()
# name = input("What is your name? ")
# print(name)

# def add():
#     x = 5
#     y = 10
#     print(x + y)
 
   
# print("JoTeq Dojo is the best!!!")
# add()

# Parameters and Arguments
# def name(name):
#     print(name)

# name("Joseph")
# name("Okenna")

# def greeting(name):
#     print(f"Hi {name}")
    
# name = input("What is your name? ")
# greeting("Okenna")
# greeting("Joseph")
# greeting()

# destination = "UK"
# Multiple Parameters
# def greeting(name, greet, city="Anambra"):
#     destination = "UK"   
#     print(f"{greet} {name}, and welcome to {city}")
    
# # name  = input("Your name please: ")
# greeting(city="Accra", name=name, greet="Akwaba")
# greeting("Jo", "Boss", "Abuja")
# greeting(name, "Nno")
# greeting(name, "Nnakwana", "Jos")

# Variable Access
# print(destination)

# Function to calculate grade
# Function to call get_grade() function
# def main():
#     print(avg())

# # Function to get student grade  
# def get_grades():
#     grades = []
#     name = input("Name: ")
#     while True: 
#         grade = int(input("Grade: "))
#         grades.append(grade)
#         if len(grades) == 4:
#             return grades
        
# def avg():
#     # g = 0
#     # grades = get_grade()
#     # for grade in grades:
#     #     g += grade
#     # return g / len(grades)
#     return statistics.mean(get_grades())
         

# main()

def calculator():
    num1 = int(input("Input a number: "))
    num2 = int(input("Input second number: "))
    print(add(num1, num2))
    print(sub(num1, num2))    

def add(x, y):
    addition = x + y
    return addition

def sub(x, y):
    subtraction = x - y
    return subtraction
    
calculator()     
        
    
    
    