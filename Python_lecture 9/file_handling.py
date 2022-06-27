# name = input("What is your name? ").strip()

# file = open("names.txt", "w")
# file.write(name)
# file.close()
# with open("names.txt", "w") as file:
#     file.write(name)

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
    
# with open("names.txt") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line.rstrip())

# with open("names.txt") as file:
#     for line in file:
#         print(line.rstrip())
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello {name}")

# names.sort()
# for name in names:
#     print(f"hello {name}")

with open("info.csv") as file:
    for line in file:
        name, age = line.split(",")
        print(f"{name} is {age.strip()} years old")
