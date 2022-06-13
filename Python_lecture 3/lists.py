# 1. Introduction to Lists
basketball_team_heights = [189, 185, 178, 160]
# print(basketball_team_heights)
basketball_team_names = ["LeBron", "Curry", "Joseph", "Thompson"]
# print(basketball_team_names)
list_mixture = [True, "String", 7, 9.5, [40, "Python"]]
# print(list_mixture)
empty = []

# 2. List Methods
# a. Append Method
basketball_team_heights.append(195)
# basketball_team_heights.append(180)
# print(basketball_team_heights)
# empty.append([1, 2, 4, 5, 7])
# empty.append(True)
# print(empty)

# 3. Plus(+)

# team = basketball_team_heights + basketball_team_names + list_mixture
# numbers = [1, 3, 5, 100, 500] + [4.0]
# print(team)
# print(numbers)

# 4. Accessing List Elements
# Python lists are zero-indexed
# Positive indexing
# print(f"{basketball_team_names[0]}'s height is {basketball_team_heights[0]}")

# Negative index
# print(list_mixture[-1])
# print(f"{basketball_team_names[3]}'s height is {basketball_team_heights[-2]}")

# 5. Modifying List elements
basketball_team_names.append("Brown")
# print(basketball_team_names, basketball_team_heights, sep=" -> ")
basketball_team_heights[-2] = 190
basketball_team_names[3] = "Bryan" 
# print(basketball_team_names, basketball_team_heights, sep=" -> ")

# 6. Shrinking a List: Remove
basketball_team_names.remove("Curry")
# print(basketball_team_names)

# 7. Two-Dimensional (2D) Lists
joseph_cars = [
    ["Toyota Corolla", 2020], 
    ["Honda Civic", 2016], 
    ["Bugatti", 2021],
    ["Benz", 2022]
    ]
# print(joseph_cars)
joseph_cars.append(["Toyota Corolla", 2019])
# print(joseph_cars)

# 8. Accessing 2D Lists
# Access row (Horizontal) ----
print(joseph_cars[0])
print(joseph_cars[-1])

# Access column (Vertical) |||| 
print(joseph_cars[0][0])
print(joseph_cars[0][-1])
print(joseph_cars[-2][0])
print(joseph_cars[-2][-1])

# Class work
"""You wife doesn't like the car you got for her. Change the car you got for her to a new
model. As you were buying a new car for your wife, you sited a new Honda Civic 2021 model
and decided to upgrade. Upgrade your Honda Civic 2016 model to 2021.
"""

joseph_cars[-1] = ["Nissan", 2022]
joseph_cars[1][1] = 2021


# Chapter 2
# Python List Methods

# 1. insert() method
mixed_list = ["Jo", 7, "Joseph Okoli", 9, True, [3,5,6]]
# print(mixed_list)
mixed_list.insert(3, "Nkumah")
mixed_list.insert(5, 75.3)
# print(mixed_list)

# 2. pop() method
removed_element = mixed_list.pop()
# print(removed_element)
# print(mixed_list)

removed_index = mixed_list.pop(3)
# print(removed_index)
# print(mixed_list)

# Consecutive Lists: Range
numbers = range(10)
# x = list(numbers)
# print(list(numbers))

# 3. The power of range 
# two inputs
# range_list = range(start, end) - the end is (end-1)
num = range(2, 101)
# print(list(num))

# three inputs
# range_list = range(start, end, increment)
num2 = range(2, 101, 10)
# print(list(num2))

num3 = range(100, 1, -2)
# print(list(num3))

# Length of a list
new_list = range(10, 1001, 5) 
new_version = list(new_list)
# print(len(new_version))

# 4. Slicing Lists
# Positive slicing
names = ["Jo", "Okenna", "Joseph", "Cristiano", "Lionel", "Neymar", "Mbappe", "Kane"]
# names[start:end] - end-1
footballer_names = names[3:7]
# print(footballer_names)

non_footballer_names = names[:3] # [beginning:3]
footballer_names = names[3:] # [3:end]
# print(non_footballer_names)

# Negative slicing
neg_footballer_names = names[-5:-1] #[-4:end]
neg_non_footballer_names = names[-6:]
# print(neg_footballer_names)
# print(neg_non_footballer_names)

# Counting in a List
num = [5, 8, 9, 4, 9, 7, 10, 7, 9]
freq_num_of_9 = num.count(9)
# print(freq_num_of_9)

# 5. Sorting Lists
names.sort()
num.sort()
# print(names)
# print(num)

names.sort(reverse=True)
# print(names)

sorted_footballer_names = sorted(footballer_names)
print(footballer_names)
print(sorted_footballer_names)
