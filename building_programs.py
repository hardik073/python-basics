# --------------------------------- Function -------------------------------------  #

# Functions are building block of any program, Instead of writing the same code multiple times,
# you write it once in a function and call it whenever needed.

def greetings():
    print("Hello World!")
    print("Welcome to python")

greetings()


#Every function follows this syntax

def function_name():
    #Code goes here
    #keep it indented
    pass

# def => keyword that creates a function
# Function name followed by ()
# Colon : to start the function body
# Indented code block 

def check_weather():
    temprature = 30
    if temprature > 25:
        print("It's hot!")
    else:
        print("Nice weather!")

check_weather()

# Variable Scope

# Local Variable = Variables created inside the function body

def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price() 

#Global Variables = created outside the function body

discount_rate = 0.15

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

result = apply_discount(100)
print(result) 


#Modify the global vaiable 

counter = 0

def increment():
    global counter # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)


# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

#Function can have default value/parameter

#Put the default parameter at last, required parameter come first

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Hardik")

#Keyword argument - name the parameter where position does not metter

def create_profile(name, age, city):
    print(f"{name}, is {age} years old, from {city}")

create_profile("Alice",25,"New York")

create_profile(name="John", city="Mumbai", age=30)
create_profile(age = 20, city="Maxico", name="Dao")

#Function can return value

def sum(a, b):
    return a + b

print(sum(5,8))