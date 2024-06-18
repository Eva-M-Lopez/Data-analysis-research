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
#has to be all the same type - can not really supposed to
print(array)
print(np.sum(array))
print(array)
my_num = np.sum(array)
print(my_num)

#Try except
try:
    print(2/0)
except ZeroDivisionError:
    print("try again ;)")

#Bring it all together
#create a function where you write a set of numbers,

#if statements
my_val = 2
if my_val % 2 == 0:
    print("this is even")
elif my_val % 2 != 0:
    print("this is not even")


#input from user
my_input = input("input_value: ")
my_counter = 0
my_counter += 1

