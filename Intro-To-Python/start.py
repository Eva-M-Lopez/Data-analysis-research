#basic variable
my_str = "Hello World"
my_int = 3
print(f"{my_str} {my_int}")
#Another way to format a string without having to concatonizing it
#print(my_str + " " +  str(my_int))
#how to cast int to string
#print(my_int)

#list
my_list = [1, my_str, 1.3]
print(my_list[0])

#loops
for item in my_list:
    print(item)

#dictionary
dict = {"item-one": 1, "item_two": 2, "item_three": 3}
for item, item2 in dict.items():
    print(item, item2)

print(dict.items())

#functions
#you have to make the function above the place you are using it

def multiply(x: int, y: int):
    return x*y
print(multiply(1,2))

#write to file
with open("test.txt", "w") as file:
    file.write("Hello World")

#read from file
with open("test.txt", "r") as file:
    print(file.read())

#Numpy Array
import numpy as np

array = np.array([1,2,3])
print(array)