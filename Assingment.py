# 9)
# tab = ["apple", "banana", "cherry"]
# print(len(tab))
# 10)
# a = [1, 2, 3, 4, 5]
# tab = sum(a)
# print(tab)
# 11)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# numbers = int(input("Pick a number: "))
# new_list = []
# for item in a:
#     if
# item < numbers:
# new_list.append(item)
# print(new_list)
# 12)
#
# Assignment  # 4
# Make
# a
# calculator
# using
# Python
# with addition, subtraction, multiplication, division and power.
# # This function adds two numbers
#
#
#     def add(x, y):
#         return x + y
#
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break
#     else:
#         print("Invalid Input")
# Write
# a
# program
# to
# check if there is any
# numeric
# value in list
# using
# for loop.
#
# tab = [1, 2.5, False]
# for i in tab:
#     if type(i) in (int, float):
#         print("yes")
# else:
#     print("no")
# Write
# a
# Python
# script
# to
# add
# a
# key
# to
# a
# dictionary.
#
# # Initialize an empty dictionary
# D = {}
#  
# L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
#  
# # Loop to add key-value pair
# # to dictionary
# for i in range(len(L)):
#           # If the key is already
#           # present in dictionary
#           # then append the value
#           # to the list of values
#         if L[i][0] in D:
#                 D[L[i][0]].append(L[i][1])
#          
#           # If the key is not present
#           # in the dictionary then add
#           # the key-value pair
#          else:
#             D[L[i][0]] = []
#             D[L[i][0]].append(L[i][1])
#              
#     print(D)
#
#     Write
#     a
#     Python
#     program
#     to
#     sum
#     all
#     the
#     numeric
#     items in a
#     dictionary.
#     my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
#     print(sum(my_dict.values()))
#     Write
#     a
#     program
#     to
#     identify
#     duplicate
#     values
#     from list.
#
#     mylist = ["a", "b", "a", "c", "c"]
#     mylist = list(dict.fromkeys(mylist))
#     print(mylist)
#     Write
#     a
#     Python
#     script
#     to
#     check if a
#     given
#     key
#     already
#     exists in a
#     dictionary.
#      Adict = {'Mon': 3, 'Tue': 5, 'Wed': 6, 'Thu': 9}
#     print("The given dictionary : ", Adict)
#     check_key = "Wed"
#     if check_key in Adict
#         keys(): print(check_key, "is Present.")
#     else:
#         print(check_key, " is not Present.")
