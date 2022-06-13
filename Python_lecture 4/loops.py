names = ["Jo", "Okenna", "Joseph", "Cristiano", "Lionel", "Neymar", "Mbappe", "Kane"]

# 1. Syntax 
# for (temporary variable) in (collection):
    # execute code - action that will be taken on each element of the list
# x ="Joseph"
count = 0
# for x in names: 
#     print(x + " Nkumah")

# 2. Using range
count_male = 0
count_female = 0
for _ in range(4):
    gender = input("What is your gender? ")
    if gender == "male":
        count_male += 1
    elif gender == "female":
        count_female += 1
    
print(f"Male: {count_male}  Female: {count_female}")
print("Male: " + str(count_male) + "   Female: " + str(count_female))
    
# 3. While
# Syntax
# while (conditinal statement is true):
#   execute code

# count = 0
# while count < 5:
#     print(count)
# #     count += 1

# countdown = 10
# while countdown >= 0:
#     print(countdown)
#     countdown -= 1
# print("Space, we dey come!!!")

# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1
    
# 4. infinite loops
# numbers = [4, 5, 18, 19, 40 ,30]

# for num in numbers:
#     numbers.append(7)
#     print(numbers)



    
