# class Student:
#     name = "Okenna"
    
#     def club(self):
#         print(f"{self.name} is part of the Okoli band")

    
# student1 = Student()
# student1.club()
# # student2 = Student()
# print(type(student1))
# print(type("Okenna"))

# class Circle:
#     pi = 3.142
    
#     # def area(self, radius):
#     #     return self.pi * radius ** 2
#     def __init__(self, radius):
#         print(self.pi * radius ** 2)

    
# circle1 = Circle(24)
# circle2 = Circle(12)
# print(circle)
# cone_area = circle.area(24)
# print(cone_area)

class Student:
    def __init__(self, name, age, height):
        self.name = name 
        self.age = age
        self.height = height
        self.grades = []
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
        
    def exam(self):
        i = 0        
        while i < 4:
            grade = int(input("Grade: "))
            self.grades.append(grade)
            i += 1
        return sum(self.grades)/len(self.grades)
        
        
# # print(Student("Okenna", 50, 185))
# print(Student("Okenna"))

student1 = Student("Okenna", 50, 185)
print(student1)
# student2 = Student("Joseph", 90, 190)
# print(student1.name, "Okoli")
# print(f"{student2.name} is {student2.age} years old")
# print(student1.exam())

# Inheritance
# Polymorphism
# Abstraction
# Encapsulation