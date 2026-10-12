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