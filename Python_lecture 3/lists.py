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
# joseph 