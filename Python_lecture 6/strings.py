# print(9 == "9")
# print(type(9), type("9"))


# lst = ["Joseph", "Okenna", "Jo", "Ronaldo"]
# pop vs remove
# pop removes element index-wise
# lst.pop(2)

# remove deletes using the element itself
# lst.remove("Jo")
# print(lst)

# hobby = "Playing games"
# print(hobby[6], hobby[7], hobby[-5])
# print(hobby[3:])
# print(hobby[3:9])
# print(hobby[-10:])

# Concatenating Strings
# first_name = "Joseph"
# surname = "Okoli"

# full_name = f"{first_name} {surname}"
# print(full_name)

# Example
# def main():
#     first_name = input("First Name: ")
#     last_name = input("Last Name: ")
#     print(password_generator(first_name, last_name))
    
# def password_generator(first_name, last_name):
#     x = first_name[0:3]
#     y = last_name[-3:]
#     return x + y

# main()

# hobby = "Playing games"
# # print(len(hobby))

# # print(hobby[len(hobby)-1])

# # print(hobby[len(hobby)-10:]) 

# def main():
#     first_name = input("First Name: ")
#     last_name = input("Last Name: ")
#     number = input("Number: ")
#     username = account_name(first_name, last_name, number)
#     print(username)
    
# def account_name(x, y, number="7"):
#     first = x[0*len(x):5]
#     last = y[0*len(y):5]
#     return f"{first}{last}{number}"

# main()

# Strings are immutable - they cannot be changed

# name = "Okenna"
# new_name = name[0:5] + "e"
# print(new_name)

# Escape Characters

# pete_edochie_saying1 = 'A man who swallows a whole coconut has complete trust in his anus'
# pete_edochie_saying2 = "A man who swallows a whole coconut has complete trust \
# in his anus"

# # complete_saying = 'According to Pete Edochie "A man who swallows a whole coconut has complete trust in his anus"'
# complete_saying = "According to Pete Edochie \"A man who swallows a whole coconut has complete trust in his anus\""
# print(complete_saying)    

# Iterating through Strings
# word = input("Input word: ")
# def print_each_alphabet(word):
#     for alphabet in word:
#         print(alphabet)
        
# print_each_alphabet(word)

# def main():    
#     print(f"New password: {get_password()}")
    
# def get_password():
#     while True: 
#         word = input("Enter New Password: ")
#         if len(word) < 8:
#             return word
#         print("Input a password less than 8")
        
# main()
    
# print("e" in "Jamaica")
# print("e" in "Nigeria")
    
# String Methods
# string_name.string_method(arguments)

# lower(), upper() and title()
# word = "cHillInG"
# to_lowercase = word.lower()
# to_uppercase = word.upper() 
# to_title = word.title()
# print(f"Lowercase: {to_lowercase}\nUppercase: {to_uppercase}\nTitle: {to_title}")

# split()
# string_name.split(delimiter)
# sentence = "I am the best"
# print(sentence.split())
# names = "Joseph, Okenna"
# splitted_name = names.split(",")

# # 'delimiter'.join(list)
# joined_name = '....'.join(splitted_name)
# print(joined_name)

# strip
# word = "!!!       Welcome to JoTeq Dojo !!!!!!!"
# # print(word.strip())
# print(word.strip("!"))

# replace
# name = "Okenna Okoli   "
# replaced_space = name.replace(" ", "...")
# print(replaced_space)

sentence = "Nigeri is best country in the world"
print(sentence.replace("Nigeri", "Nigeria"))

# find()
print(sentence.find("best"))