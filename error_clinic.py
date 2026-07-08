# |fredi Miranda | lab 5| error clinic
# Missing parenthesis
print("Hello, world!")
# this code will not run if is missing a paranthesis.
# i was correct it was missing a paranthesis '(' was never closed).
#SyntaxError: '(' was never closed

# Missing colon
x = 14
if x > 5:
   print("x is greater than 5")
#this will run but it will turn into an error.
# i was correct the only thing that was missing was ":" and we had to defined what "x" is.
#yntaxError: expected ':'
#NameError: name 'x' is not defined

# Missing quotes
Message = "Hello world!"
# we are missing the quotes. 
# yup the quotes where the problem and they did not run when the quotes where not on.
#SyntaxError: invalid syntax


# Indentation
for i in range(5):
    print(i)
# we have a small problem that the code will not run if the "print" is on the correct spot.
# that was correct it needed to have a space in the bottom.
#ndentationError: expected an indented block after 'for' statement 


# Misspelled keyword
def greeting(name):
    return "Hello, " + name

print(greeting("Alice"))
# the same thing we need to put "retrun" in the correct spot.
# we needed to put it back to its main place.



# ZeroDivisionError (fixed)
#result = 10 / 0
#ZeroDivisionError: division by zero
divisor = 0
if divisor != 0:
  print(10 / divisor)
else:
  print("Cannot divide by zero")

# the problem might be the result = 10 / 0 python cannot divide zero
#i was correct because python cannot "divide by zero".

# TypeError (fixed)

age = "25"
total = 30 + int(age)
print(total) #55
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# we might have to put an 'int' or a 'str'
# i was corrrect that was the only thing i was missing 'int'


# IndexError (fixed)
numbers = [1, 2, 3]
print(numbers[2])  #  3 (the lat item)
#IndexError: list index out of range
#we might have to  put a '#' at the end or write a different code.
# we haded to also cahnge number 3 for number 2 to make it work.

# KeyError (fixed)
person = {"name": "John", "age": 30}
print(person.get("city", "Unknown")) # Unknown
#KeyError: 'city'
# we need to add a paranthesis and quotes.
# we haded to put a "# unknown so that way the code could be run and be fixed."

# NameError (fixed)
age = 25
print(age)
#NameError: name 'age' is not defined 
#it might not give me a error
# i was correct it did not gave me an error but it gave me the age "25".


# Off-by-one error (fixed)
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
#IndentationError: expected an indented block after 'for' statement on line 88
# we need to put the "print" in its right place and take out '+' and '1'
# i was correct  those where the correct changers that i had to do.

# Incorrect conditional (fixed)

name = "Charlie"
if name == "Alice" or "Bob":
   print("Hello, friend!")

else:
   print("Hello, stranger!")
#IndentationError: expected an indented block after 'if' statement on line 97
#need to put the "print's" to its place so that way we can iave a good code and mabey make space.
# i was 100% correct that we needed to space out "else" and the word "print"
name = "Charlie"
if name == "Alice" or name == "Bob":
   print("Hello, friend!")

else:
   print("Hello, stranger!")
# even cleaner:
if name in ("Alice", "Bob"):
    print("Hello, friend!")


# Infinite loop (fixed)
count = 0
while count < 5:
    print(count)
    count += 1 # this is what eventually ends the loop
#IndentationError: expected an indented block after 'while' statement on line 117
#we might need to move print or/and add something else

# Print debugging example
def calculate_area(radius):
    print("DEBUG radius =", radius)
    area = 3.14 * radius ** 2
    print("DEBUG area =", area)
    return area

print(calculate_area(5))
#the program will calculate and print the area of a circle with a radius of 5.
#DEBUG radius = 5 DEBUG area = 78.5 78.5
# i was correct, but there was no error


# Function example
def calculate_area(radius):
    return 3.14 * radius ** 2

print(calculate_area(5))
print(calculate_area(10))
#The function will calculate the area of a circle using the given radius values.
# this is the out-put 78.5 314.0



# Test case example
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
print(is_even(0))

#The function will check whether each number is even and return True for even numbers and False for odd numbers.
# this is the out-putTrue 'False' and 'True'


#Snippet 1
x = 10
y = 0

if y != 0:
    result = x / y
    print("Result:", result)
else:
    print("Cannot divide by zero.")
# Prediction (Error Type): ZeroDivisionError
#Explanation: The code will attempt to divide 10 by 0, which Python cannot do.


#Snippet 2
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
#Prediction (Error Type): IndexError
#Explanation: numbers[i + 1] will attempt to access a non-existent index at some point in time.

#Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#Prediction (Error Type): SyntaxError
#Explanation: The definition of the function is missing a colon at the end of def calculate_area(radius).

#Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
#Prediction (Error Type): SyntaxError
#Explanation: The if and else conditions are missing their colons.


#Snippet 5
for i in range(5):
    print(i)
#Prediction (Error Type): SyntaxError
#Explanation: The for loop line is missing its colon.


#Snippet 6
def greet(name):
    return "Hello, " + name

print(greet("Alice"))

#Prediction (Error Type): SyntaxError
#Explanation: The string is incorrectly constructed as it should contain the "+" operator between "Hello, " and name.

#Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)

#Prediction (Error Type): Logic Error
#Explanation: The code runs, but because of the indentation, the total is printed after the loop ends.

#Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#Prediction (Error Type): RecursionError (Logic Error)
#Explanation: The function will move farther from 0 and will never reach its terminating condition.

#Snippet 9
name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
#Error Type: Logic Error
#Explanation: The program will run fine, but the condition will always be true since the string "Bob" will evaluate to True on its own.


#Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))
#Error Type: ZeroDivisionError
#Explanation: The program will not run because the function will be trying to divide by zero.

