"""

List : Like a shopping list (ordered items)

Dictionary : Like a phone book (name > numbers)

Tuples : Like coordinates (fixed values)

Sets : Like a bag of unique items

"""

#list

my_list = []

fruits = ["apple", "banana", "orange"]

numbers = [1,2,3,4,5,6]

mixed = ["Hello", 3, True, 4.5]

print(fruits[0])
print(fruits[1])
print(fruits[-1]) #Last item
print(fruits[-2]) #second last

print(fruits[0:2]) #apple, banana it slices and remove orange

fruits[0] = "Mango" #change the first item of the list

fruits.append("grape") #Add to end
fruits.insert(1,"kiwi") #Insert at position

fruits.remove("banana") #remove by value
del fruits[0] #remove by index
last = fruits.pop() #return and return last 


# ---------- Dictionary  ----------#

#Think it of a real disctionary where you lookup a work and its defination

my_dist = {}

person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
}

score = dict(math=95,english=90,science=92)

print(person["name"])

print(person.get("job")) #Returns none
print(person.get("job", "Unkown")) #Return Unkown as default

print(person.get("age"))


person["email"] = "alice@gmail.com" #Add new
person["age"] = 30 #Update existing

del person["email"] #remove by key
age = person.pop("age") # remove and return

person.clear() #Remove all

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])


# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"



#Tuples

# ---------- Tuples  ----------#


#Tuples are like list but it can't be changed once created.
#They are immutalbe sequances.

empty = ()

points = (3, 5)
colors = ("Red","Green","Blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

print(points[0])
print(colors[-2])

# Slicing works too
print(colors[0:2])   # ("red", "green")

# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!


#Sets

# ---------- Set  ----------#

#Sets are collections that only stores unique values.

empty_set = set()

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red","green"}
colors.add("blue")
print(colors)

colors.remove("blue") #Error if not found
colors.discard("yellow") #No Error if not found

# Check membership
if "red" in colors:
    print("Red is available")