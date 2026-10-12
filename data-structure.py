"""

List : Like a shopping list (ordered itesm)

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