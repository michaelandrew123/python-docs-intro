




###
#
# My first Django Project
#
# A library of reusable modules(building blocks)
#
# A Framework defines a structure for our applications
#
#
# INSTALL DJANGO
# open terminal and type
#
# -pip install django==2.1
# CREATE DJANGO PROJECT
# ctrl+l to clean the terminal
# execute the command
# -django-admin startproject pyshop .
#
# wsgi: web server gateway interface -> will provide standard interface between application build with django and webserver
#
# python3 manage.py runserver
#
#
# Create new apps
# python manage.py startapp products
# -----------------------------------------
#
# View Functions
#
#   create routes
#   create model
#   create migrations
#
#   python manage.py makemigrations
#   check pyshop -> settings
#   python manage.py migrate
#
#   Create auth
#   python manage.py createsuperuser
#
#   error database and need to upgrade the pip install django --upgrade
#  pip install django --upgrade
#  python manage.py migrate
#
#   UPDATE DJANGO
#   pip install --upgrade django==1.6.5
#
#
#
#
# ##






###
#
# py -m pip install -U Django
# py -Wa manage.py test
#
#
# ##




###
# Anaconda promp comman
# run: jupyter notebook
# ###


###
#
# AI Artiicial Intelligence
# Machine learning
# Machine Learning in Action
#
# 1. Import the Data
# 2. Clean the Data
# 3. Split the Data into Training/Test Sets
# 4. Create a Model
# 5. Train the Model
# 6. Make Predictions
# 7. Evaluate and Improve
#
#  Libraries and Tools for Machine Learning
#
# 1. Numpy
# 2. Pandas for csv files
# 3. MatPlotLib
# 4. Scikit-learn
#
# Recommended to use code editor
# Jupyter.org
# Anaconda.com = download
#
#
# Importing a Data Set
# Kaggle.com
# Need to check tutorial pandas data frame
#
#
#
# Jupyter Shortcuts
# Press
#   H check all the shortcut
#   df. tab to auto check all the functions that can be use
#   shift and tab to check the signature
#   insert cell a for top and b for bottom
#   delete cell double tap D
#   ctrl + / for add amd remove comment
#
#
# A Real Problem
#
# Machine Learning Project
#
#
# import pandas as pd
# music_data = pd.read_csv("data_2genre.csv")
# music_data
#
# Preparing The Data
#
#







exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Automation wiht Python
#
# Excel Spreadsheets
#
#
#
#
# ##


import openpyxl as xl
from openpyxl.chart import BarChart, Reference


def process_workbook(filename1, filename2):
    wb = xl.load_workbook(filename1)
    sheet = wb['Sheet1']
    #cell = sheet['a1'] #sheet.cell(1,1)
    #print(cell.value)
    #print(sheet.max_row)

    for row in range(2, sheet.max_row + 1):
        print(row)
        cell1 = sheet.cell(row, 3)
        corrected_price = cell1.value * 0.9
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price

    values = Reference(sheet,
              min_row=2,
              max_row=sheet.max_row,
              min_col=4,
              max_col=4
              )
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'e2')
    return wb.save(filename2)


process_workbook('transactions.xlsx', 'transactions2.xlsx')


exit()
#----------------------------End of the Tutorial ---------------------------------#


###
#
# Pypi and Pip (huh?)
# extracting information from the website
# install package in pypi.org
# search openpyxl
#
# Open new terminal on your pycharm editor
# Type: pip install openpyxl
#
# ##









exit()
#----------------------------End of the Tutorial ---------------------------------#



###
#
# Files and Directories
#
#
# ##
from pathlib import Path

#absolute path
#c:\Program File\Microsoft
#relative path
#


path = Path()
#print(path.mkdir())
#print(path.rmdir())
#print(path.glob('*.py')) get all the file in current directory that has py extension using for loop
#print path.glob('*') get all the file in current directory including folder using for loop
#
for file in path.glob('*'):
    print(file)





exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
# Generate Random Value
#
#
# ##

import random

for i in range(3):
    print(random.randint(10, 20))

members = ["Michael Andrew", "Lovely Joy", "Mike"]

leader = random.choice(members)
print(leader)

###
#
# Exercise
#
#
# ##

class Dice:
    def roll(self):
        first =  random.randint(1, 6)
        second =  random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())




exit()
#----------------------------End of the Tutorial ---------------------------------#

###
#
# Package
#
#
# ##

import ecommerse.shipping
ecommerse.shipping.calc_shipping()

from ecommerse.shipping import calc_shipping
calc_shipping()


from ecommerse import shipping
shipping.calc_shipping()




exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Modules
# Each file called module
#
#
# to access
# import converters =>  converters.kg_to_lbs(2)
#
#from converters import kg_to_lbs => kg_to_lbs(2)
# ##
import converters
from converters import kg_to_lbs
print(kg_to_lbs(20))
print(converters.kg_to_lbs(2))


###
#
#
# Execise
#
# ##



from utils import find_max

print(find_max())


exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Classes Inheritance
# It is a mechanism for using code
# dry: dont repeat yourself
# ##
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("This dog always barking!")

class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")

cat1 = Cat()
cat1.be_annoying()
cat1.walk()

dog = Dog()
dog.bark()
dog.walk()


exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Classes Constructor
#
# Use Pascal language
# Always capitalize the first letter of each word
# e.g Class EmailClient
# ##

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point = Point(10, 20)
print(point.x)

###
#
# Execise
#
#
# ##

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Talk here {self.name}")

try:
    name = str(input("Enter name: "))
except ValueError:
    print("Invalid name")

person = Person(name)
person.talk()
person2 = Person("Lovely Joy")
person2.talk()

exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Classes
#
# Use Pascal language
# Always capitalize the first letter of each word
# e.g Class EmailClient
# ##

class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.move()

point2 = Point()
point2.x = 1
print(point2.x)



exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Comments
#
#
# ##

#Just minimize your comment for explaining your code to avoid bad comments

exit()
#----------------------------End of the Tutorial ---------------------------------#

###
#
#
# exceptions function
#
#
# ##
try:
    age = int(input("Age: "))
    income = 15000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero")
except ValueError:
    print("Invalid Value")



exit()
#----------------------------End of the Tutorial ---------------------------------#
# ###
# #
# #
# # Create a Reusable Function
# #
# #
# # ##

def emoji_converted(message):
    words = message.split(" ")

    emojis = {
        ":)": "😊",
        ":(": "😒",
        "<3": "❤"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converted(message))


exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Return statement function
#
# if we dont have return then the output will return none as default
# ##

def square(number):
    return number * number

result = square(3)
print(result)


exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Keyword Arguments function
#
#
# ##




def greet_user(first_name, last_name):
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome Aboard.")


print("Start")
greet_user(last_name="Suarez", first_name="Michael Andrew")
greet_user("Suarez", first_name="Michael Andrew")
calc_cost(total=50, shipping=5, discount=0.1)
print("Finish")



exit()
#----------------------------End of the Tutorial ---------------------------------#
###
#
#
# Function Parameters
#
#
# ##



def greet_user(first_name, last_name):
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome Aboard.")


print("Start")
greet_user("Michael Andrew", "Suarez")
print("Finish")




exit()
#----------------------------End of the Tutorial ---------------------------------#

###
#
#
# Function
#
#
# ##

def greet_user():
    print("Hi there!")
    print("Welcome Aboard.")


print("Start")
greet_user()
print("Finish")





exit()
#----------------------------End of the Tutorial ---------------------------------#


###
#
#
# Emoji Converter :)
#
# ##

message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😒",
    "<3": "❤"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

exit()
#----------------------------End of the Tutorial ---------------------------------#

###
#
#
# Dictionaries
#
#
# ##

###
#
# Name: Michael Andrew
# Email: suarezmike129@gmail.com
# Phone: 1234
#
# ##
customer = {
    "name": "Michael Andrew",
    "age": 27,
    "is_verified": True
}
#update value on customer. customer["name"] = "Mike Andrew"
print(customer["name"])
#add new key. customer["favorite_color"] = "Blue"
#get can be set own key and value. customer.get["birthdat", "Sep. 20, 1993"] the result would be Sep. 20, 1993
print(customer.get("name"))

###
#
# Exercise
#
# Enter number then auto translate into words
#
#
# ##

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)



exit()
#----------------------------End of the Tutorial ---------------------------------#


###
#
#
# Unpacking
# It can work both tuples () and list []
# ##

coordinates = (1, 2, 3)
#coordinates[0] * coordinates[1] * coordinates[2] we can pack this one
x, y, z = coordinates
print(y)



exit()
#----------------------------End of the Tutorial ---------------------------------#

##
#
#
# TUPLES
# Another important struture in Python
#
# ###



###
# We only have two method for tuples
# Count
# Index
# The tuples not supported on asigning value. numbers[0] = 10
#
# ##
numbers = (1, 2, 3)
print(numbers)

exit()
#----------------------------End of the Tutorial ---------------------------------#


###
#
# LIST METHOD
#
#
# ##

numbers = [5, 2, 1, 5, 7, 4]
print(50 in numbers) #check if numbers has 50 value in the list. Reuslt would be boolean true or false
print(numbers.count(5)) # the count method will count then the specific value inside the list. [5, 2, 1, 5, 7, 4] The result would be 2
numbers.sort() #not allowed to direct print
print(numbers) #this is the result of sort method. sort means it will arrange the number ascending [1, 2, 4, 5, 5, 7]
numbers.reverse() #it will reverse the value of the numbers from ascending to descending
numbers2 = numbers.copy() #duplicate the value of numbers and past it on the numbers2
numbers.append(20) #add new item to the new list
numbers.insert(0, 10) #add new item in any index of the list
numbers.remove(1) #remove speciic item in the list
numbers.index(5) #get the index of 5 value in the list [5, 2, 1, 7, 4] and the result would be 0
numbers.pop() #remove the last item in the list
numbers.clear() #clear all the list

print(numbers)

###
#
#
# Challenge
# Write a program to remove the duplicates in a list
#
#
# ##

number_lists = [3, 2, 2, 6, 5, 6, 8, 2, 10]
uniques = []
for number_list in number_lists:
    if number_list not in uniques:
        uniques.append(number_list)
print(uniques)

exit()
#----------------------------End of the Tutorial ---------------------------------#

###
#
#
# 2D Lists or Two Dimensional Lists
#
#
# ##

#
# [
#   1 2 3
#   4 5 6
#   7 8 9
# ]
#

#
#matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
#
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])
####
#
# Display all the matrix value
#
# #

for row in matrix:
    for item_matrix in row:
        print(item_matrix)


exit()



#Lists
name = [
    "Michael",
    "Andrew",
    "Lovely",
    "Joy",
    "Indoso",
    "Suarez"
]
print(name[0])
# name[0] output Michael
# name[-1] output Suarez
# name[-2] output Indoso
# name[2:] output from index 2 to the end, this is called range
# name[2:4] output lovely and Joy, the 4 index is not included
# name[:] the default is zero and this will give us output from index 0 to the end
# name[0] = "Mike" this will update the index zero from Michael to Mike

#challenge
#write a program to find the largest number in a list
number_lists = [6, 3, 20, 7, 5, 10]
max = number_lists[0]
for x_list in number_lists:
    if x_list > max:
        max = x_list
print(max)




#Nested Loop
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

#For Loops
prices_loop = [10, 20, 30]
total_price = 0
for price_loop in prices_loop:
    total_price += price_loop
print(f"Total: {total_price}")

#challenge
number_for_loop = [5, 2, 5, 2, 2]
for x_count in number_for_loop:
    nested_loop_output = ''
    for x_count_nested in range(x_count):
        nested_loop_output += 'x'
    print(nested_loop_output)
# The output will be
# xxxxx
# xx
# xxxxx
# xx
# xx


#range(10) = 1 2 3 4 5 6 7 8 9
#range(5, 10) = 5 6 7 8 0
#range(5, 10, 2) = 5 7 9 go two itep forward
for item4 in range(5, 10, 2):
    print(item4)

for item3 in [1, 2, 3, 4]:
    print(item3)

for item2 in ["Michael", "Andrew", "Lovely", "Joy", "Indoso", "Suareez"]:
    print(item2)

for item in 'Python':
    print(item)


#Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped!")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry, I don't understand that!")


#Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")



#While loops
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")



#Project: Weight Converter
weight = int(input("Weight: "))
unit = input("(L)bs (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.")

#Comparison Operators
#if temperature is greater than 30
#   it's a hot day
#otherwise if it's less

name_com = "Michael Andrew Suarez"

if len(name_com) < 3:
    print("Nmae must be at least 3 characters.")
elif len(name_com) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good")

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#logical Operators
#and = both must be true
#or = must have one must be true
#not = oposite

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

#if statements
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("IT's a lovely dau")

#Quest
house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Down Payment: ${down_payment}")

#math function
import math #math module
print(math.floor(2.9))
#math.floor(2.9) return 2
#math.ceil(2.9) return 3
x = 2.9;
print(abs(-2.9))
#round()
#abs() absolute function
#

#Operator Precedence
x = (10 + 3) * 2 ** 2 #result 22
x=(2 + 3) * 10 - 3 #result 47
print(x)
#execute sequence
#Parenthesis
#exponentiation 2**2
#Multiplication or Division
#Addition or Subtraction


#Arithmetic Operation
#float and int
#10 / 3 result is float
#10 // 3 result is int
#10 % 3 returns reminder and 10 ** 3 return 10 to the power of 3(10*10*10)

#String methods
course_method='Python for Beginners'
print(len(course_method))
print(course_method.upper())
print(course_method.lower())
print(course_method.find('y'))
print(course_method.replace('Beginners', 'absolute Beginners'))
print('Python' in course_method)
#len()
#variable.upper()
#variable.lower()
#variable.title()
#variable.find()
#variable.replace()

#Formatting String
first='Michael Andrew'
last='Suarez'
message=first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

course_array = "Python's Course For Beginners Array"
print(course_array[0:3])
name_array = "Michael"
print(name_array[1:-1])

course = "Python's Course For " + '"Beginners"'
print(course)
email = '''
    Hi Michael Andrew,
    
    Here is our first email to you.
    
    Thank you,
    The support team


'''

print("Michael Andrew Suarez")
price = 10
rating = 4.9
name = "Michael"
is_published = False
print(price)
name = input("What is your name? ")
print("Hi " + name)
favorite_color = input("What is your favorite color? ")
print(name + " Likes " + favorite_color)
birth_year = input("Birth Year: ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(birth_year))
print(name + " is a " + str(age) + " year/s old")
weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(name + " has weight of " + str(weight_kg) + " kg")