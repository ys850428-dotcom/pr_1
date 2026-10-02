#importdatetime
from datetime import datetime


name = input("Enter your name: ")
age = str(input("enter your age:"))
height = str(input("enter your height:"))
favorite_num = str(input("enter your favorite number:"))
print(type(name))
print(type(age))
print(type(height))
print(type(favorite_num))
current_year = datetime.now().year
birth_year = current_year - int(age)
print(id(name))
print(id(age))
print(id(height))
print(id(favorite_num))
print(current_year)
print(birth_year)
print(datetime.today())



