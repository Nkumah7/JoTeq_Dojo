# x = 5
# try:
#     print(x + 5)
# except NameError:
#     print("Please check if the variable is defined properly")
# except TypeError:
#     print("Please check the values you entered")
# except:
#     print("Error")
# else:
#     "No Errors!"
# finally:
#     print("Error handling is done")


# print(x + '5')
# print(x)

# try:
#     age = int(input("How old are you? "))    
# except ValueError:
#     print("Age is not a number")
# else: 
#     print(f"{age} is old enough to get married")  

# while True:
#     try:
#         age = int(input("How old are you? "))
#     except ValueError:
#         print("Age is not a number")
#     else:
#         break
    
# print(f"{age} is old enough to get married")

def main():
    even_nums = [x for x in range(0, get_even_numbers("Input a number: ")) if x % 2 == 0]
    print(even_nums)

def get_even_numbers(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass 
        # else:
        #     # break
        #     return x
        
main()
         