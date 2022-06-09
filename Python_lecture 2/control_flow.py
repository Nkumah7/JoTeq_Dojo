# Boolean Datatypes - True, False

# Relational operators:
# Equals: ==
# Not equals: !=

# 1. Relational Operators
variable1 = 1 + 1
variable2 = 2
name1 = "joseph"
name2 = "Joseph"
# print(variable1 == variable2)
# print(name1 == name2)

num1 = 4
num2 = 7 
# print(num1 != num2) # True is when the condition is met

# print('10' == 10)

bool_one = 5 != 7
# print(bool_one)
bool_two = 1 + 1 != 2
# print(bool_two)

# Syntax
# if (condition is true/met):
    # execute code
    
    
# If statement
# is_raining = True
# if is_raining:
#     print("bring an umbrella")

# if 7 == "7":
#     print(7 + 7)

# if 100 != 5 * 20:
#     print("Hurray Python!!!")

# 2. Relational Operators
# greater than - >
# greater than or equal to - >=
# less than - <
# less than or equal to - <=

# print(10 < 20)

# num_of_alcohol_bottles_wanted = 10 
# num_of_bottles_bought = 8

# if num_of_bottles_bought < num_of_alcohol_bottles_wanted:
#     print("Guy, why you no buy ten")

# num_of_bottles_bought += 2
# if num_of_bottles_bought >= num_of_alcohol_bottles_wanted:
#     print("Yes ooo!!")

# 3. Boolean operators
# and - It is only True when all conditions are True
# or - It is True when 1 condition out of all conditions is True
# not - the opposite of the condition

# and
# print((2 + 2 > 3) and (1 + 1 == 2))
# print(("Lionel" == "lionel") and (4 == 2 * 2) and (7 * 2 == 13 + 1))

# print(not((2 + 2 == 1) or (5 * 15 == 20 + 40) or ("7" == 7) or (7 ** 2 == 7 * 7)))

# print(not(5 * 5 == 25))
team_height = 178.0
team_body_type = 'slim'
jo_height = 189.0
jo_body_type = 'slim'

# if jo_height >= team_height and jo_body_type == team_body_type:
#     print("You have the needed requirements")
    
jo_body_type = 'fat'
muscles = True
curry_height = 175.0
# if jo_height >= team_height and jo_body_type == team_body_type:
#     print("You have the needed requirements")

# if curry_height != team_height or muscles:
#     print("Come for tryouts and we will test you")


# 4. Else
# Syntax
# if (condition is true/met):
    # execute code
# else:
    # execute code
    
# if jo_height < team_height:
#     print("We cannot use your height in our team")
# else:
#     print("Welcome to the team")
    
# if not(jo_body_type == 'fat'):
#     print("Y")
# else:
#     print("X")

# 5. Else if
# Syntax
# if (condition1 is true/met):
    # execute code and stop if elif block
# elif (condition1 is false and condition2 is true/met):
    # execute code and stop if elif block
# elif (condition1 and condition2 are false and condition3 is true/met):
    # execute code and stop if elif block
# else:
#   execute code

required_number_of_tropies_won = 1
required_number_of_goals = 20

messi_trophies = int(input("Number of trophies Messi won: "))
messi_goals = int(input("Number of goals Messi scored: "))
ronaldo_trophies = int(input("Number of trophies Ronaldo won: "))
ronaldo_goals = int(input("Number of goals Ronaldo scored: "))

if messi_trophies >= required_number_of_tropies_won and messi_goals >= required_number_of_goals:
    print("The Ballon d'or goes to Messi")
elif ronaldo_trophies >= required_number_of_tropies_won and ronaldo_goals >= required_number_of_goals:
    print("the Ballon d'or goes to Ronaldo")
elif ronaldo_trophies >= required_number_of_tropies_won or ronaldo_goals >= required_number_of_goals:
    print("the Ballon d'or goes to Ronaldo")
elif messi_trophies >= required_number_of_tropies_won or messi_goals >= required_number_of_goals:
    print("The Ballon d'or goes to Messi")
else:
    print("None of them gets the Ballon d'or this year")







