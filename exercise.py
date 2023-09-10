import re

""" Task 1: Basic Function
Write a Python function that takes two integers as input and returns their sum."""

# def sum_generator():
#     a = int(input('Enter any integer: '))
#     b = int(input('Enter any integer: '))
#     c = a + b
#     return c

# print(f'The sum of the input integers : {sum_generator()}')

#------------------------------------------------------------

# def addition(a, b):
    
#     sum = a + b
    
#     return sum

# first_num = int(input('Enter first integer: '))


# second_num = int(input('Enter second integer: '))

# print(addition(first_num, second_num))


"""Task 2: Function with Conditional Logic

Write a function that takes an integer as input and 
returns "Even" if the number is even and "Odd" if it's odd."""

# def even_odd_discriminator():
    
#     num = int(input('Enter any integer to find if it is even or odd.: '))
    
#     if num % 2 == 0:
        
#         result = f'{num} is even.'
#         return result
#     else:
        
#         result = f'{num} is odd'
#         return result


# print(even_odd_discriminator())

#------------------------------------------------------------

# def getInt(prompt):
#     while True:
#         value = input(prompt)
        
#         try:
#             return int(value)
#         except ValueError:
#             print('Invalid integer.')
            
# def evenORodd(num):
    
            
#     if num % 2 == 0:
            
#         return f'{num} is even'
        
#     else:
        
#         return f'{num} is odd'
            
# num = getInt('Enter any integer to find if it is even or odd.: ')


# print(evenORodd(num))


    
    


"""Task 3: Function with Default Argument

Write a function that takes two arguments, one required and
the other with a default value, and returns their product. """

# def a_function(required, default=30):
    
    
#     result = required * default
    
#     return result

# required = int(input('Enter any integer: '))

# print(a_function(required))


"""Task 4: Function with a Loop

Write a function that takes an integer as input 
and prints all the numbers from 1 to that integer. """


# def dada():
    
#     counting_num = []
    
#     num = int(input('Enter any integer: '))
    
#     for i in range(1, num + 1 ):
        
#         counting_num.append(i)
        
        
#     return counting_num
        
    
# print(dada())


#------------------------------------------------------------

# def counter():
    
#     num = int(input('Enter any integer: '))
    
#     for i in range(1, num +1):
        
#         print(i)

# counter()

#------------------------------------------------------------
# def getInt(prompt):
#     while True:
#         value = input(prompt)
        
#         try:
#             return int(value)
#         except ValueError:
#             print('Invalid value')

# def counter(num):
    
#     container = []
    
#     for i in range(1, num + 1):
        
#         container.append(i)
        
#     return container

# num = getInt('Enter any integer: ')

# print(counter(num))

#------------------------------------------------------------

# def reverse(num):
    
#     container =  []
    
#     for i in range(num, 0 -1 , -1 ):
        
#         container.append(i)
    
#     return container

# a = getInt('Enter any integer: ')

# print(reverse(a))

# """Task 5: Function with While Loop

# Write a function that takes an integer as input and 
# prints all the numbers from 1 to that integer using a while loop."""

# def counter():
    
#     num = int(input("Enter any integer: "))
    
#     holder = []
    
#     counter = 0
    
#     while num > counter:
        
#         counter += 1

#         holder.append(counter)
    
#     return holder

# print(counter())

#------------------------------------------------------------

# def strike():
    
#     num = int(input('Enter any integer: '))
    
#     num2 = 0
    
#     while num2 < num:
        
#         num2 += 1
        
#         print(num2)
        
# strike()

#------------------------------------------------------------

# def get_int(prompt):
    
#     while True:
#         value = input(prompt)
        
#         try:
#             return int(value)
#         except ValueError:
#             print('Invalid value.')

# def counter(num):
    
#     container = []
#     counter = 0
    
#     while num > counter:
        
#         counter += 1
        
#         container.append(counter)
        
#     return container

# num = get_int('Enter any integer: ')

# print(counter(num))

#------------------------------------------------------------

# def reverse(num):
    
#     container = []
    
#     sub = 1
    
#     while num > 0:
        
#         container.append(num)
        
#         num -= sub
        
#     return container

# a = get_int('Enter any integer: ')

# print(reverse(a))


"""Task 6: Function with String Manipulation

Write a function that takes a string as input and returns the reverse of the string."""

# def reverse():
    
#     text = input("Enter any text: ")
    
#     reversed_text = [None] * len(text)
    
#     for index, element in enumerate(text):
#         if element.isupper():
#             reversed_text[-(index + 1)] = element.lower()
#         elif element.islower():
#             reversed_text[-(index + 1)] = element.upper()
#         else:
#             reversed_text[-(index + 1)] = element 
    
#     reversed_text = "".join(reversed_text)
    
#     return reversed_text

# print(reverse())

"""Task7: Function with Input Validation

Write a function that takes a string as input and checks 
if it contains only alphabetic characters (no digits or special characters)."""

# import re

# def onlyStr():
    
#     text = input("Enter any text to check if it contains only alphabetic characters \n(no digits or special characters): ")
    
    
#     pattern = r'[a-zA-Z\s]+'
    
#     match = re.fullmatch(pattern, text)

    
#     if match:
        
#         print('This text contains only alphabetic characters.')
        
        
    
#     else:
#         print('This text contains various kinds of characters.')
        

# onlyStr()


"""Task 8: Function with Multiple Returns

Write a function that takes an integer as input 
and returns "Positive," "Negative," or "Zero" based on the number's sign."""

# def sign_discriminator():
    
#     num = int(input("Enter any integer: "))
    
#     if num == 0:
#         print('Zero')
#     elif num > 0:
#         print('Positive')
#     elif num < 0:
#         print('Negative')

# sign_discriminator()


"""Task 9: Function with Input Validation (Part 2)

Write a function that takes a string as input and checks 
if it's a valid email address using regular expressions."""

# def email_checker():
    
#     email = input('Enter E ail address to check if it is valid: ')
    
#     pattern = r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$'
    
#     match = re.match(pattern, email)
    
#     if match:
        
#         print('This email address is valid.')
    
#     else:
#         print('This email address is invalid')
        
# email_checker()

"""Task 10: Function with Multiple Arguments

Write a function that takes five numbers as input and
returns the maximum, minimum, and average of those numbers."""

# def discriminator():
    
#     container = []
#     result = 0 
#     for i in range(5):
        
#         num = int(input('Enter any integer: '))
        
#         result += num
        
#         container.append(num)
        
#         average = result / 5
        
#     maxi = max(container)    
#     mini = min(container)    
    
#     return f'Maximum number : {maxi}, Minimum number : {mini}, average of those numbers : {average}'
    
    
# 


"""Exercise 11: Function with Variable Scope

Write a function that demonstrates variable scope by defining a variable inside the function
and trying to access it outside the function."""


# def scope():
#     text = 'This is a local variable.'
    
#     print(text)

# scope()

# # print(text)


"""Exercise 12: Function Composition

Write two functions, square and double, where square takes an integer as input
and returns its square, and double takes an integer as input and returns double that value.
Then, write a third function that combines these two functions to first square and then double a given integer.
"""

# def square(a, b = 2):
    
#     return a ** b 
    
    

# def double(a, b = 2):
    
#     return a * b


# def combine(a, b = 2):
    
#     return double(square(a))

# num = int(input('Enter any integer: '))

# print(square(num))
# print(double(num))
# print(combine(num))
