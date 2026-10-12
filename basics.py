# Variable is like a labeled box where you can store information

name = "Alice"
age = 25
is_student = True

score = 0
print(score)
score = 10

#This is a single line comment

"""
This is multiline comment
"""

# Data Types: 
# Python has 4 Main Data types: String, Number and Boolean

#Checking types
score = score + 10
print(type(score))


#Numbers: Integer and Float
age = 25
score = -10

price = 9.99
temprature = -5.5
pi = 3.14159

#String

name = "Alice"
message = "Hello, World!"
print(len(name))
age = 25
message = "Alice is "+ str(25) +" years old."
message_with_f_string = f"Aclice is {age} years old"


#Booleans
is_logged_in = True
is_admin = False
has_permission = True


#Operators

print(10 + 3)
print(10 - 3)
print(10 * 3) # Division always gives float
print(10 / 3)

print(10 // 3) #Flore division round of 3 (Rounds down)
print(10 % 3)
print(10 ** 3) # Power of 10 to 3


age = 18

print(age == 18)    # True  - Equal to
print(age != 21)    # True  - Not equal to
print(age > 17)     # True  - Greater than
print(age < 20)     # True  - Less than
print(age >= 18)    # True  - Greater than or equal
print(age <= 18)    # True  - Less than or equal


age = 25
has_license = True

can_drive = age > 18 and has_license
print(can_drive)

day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)

is_adult = age > 18
is_child = not is_adult
print(is_child)

#String manipulation

first_name = "John"
last_name = "Dao"

full_name = f"{first_name} {last_name}"

print(full_name.lower())
print(full_name.upper())
print(full_name.title())

#Control Flow

age = 18

if age >= 18:
    print("You can vote!")
    print("You are an adult")


if temprature >= 25:
    print("It's hot")
else:
    print("Nice Weather")   


score = 85

if score >= 90:
    print("A - Excellent")
elif score >= 80:
    print("B - Good Job")
elif score >= 70:
    print("C - Keep it up")
else:
    print("F - Need Improvement")

# Loops

for i in range(5):
    print(f"Hello {i}")

for i in "Alice":
    print(i)

colors = ["Red", "Blue", "Green"]
for i in colors:
    print(i)

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1


