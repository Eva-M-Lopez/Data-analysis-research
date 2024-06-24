import csv
import numpy as np
#read from file

def read():
    try:
        with open('Intro-To-Python/weatherdata.csv', 'r') as csvfile:
            #create a reader object
            csv_reader = csv.DictReader(csvfile)
            
            #create a list of dictionaries - list comprehension
            wdata = [row for row in csv_reader]
            
            return wdata
    except IOError:
        print("File could not be read")
 
def make_list_temp(my_list: list):
    temp_list = []
    for item in my_list:
        temp_list.append(int(item['Temperature']))
    return temp_list

def make_list_humidity(my_list: list):
    temp_list2 = []
    for item in my_list:
        temp_list2.append(int(item['Humidity']))
    return temp_list2

tl = make_list_temp(read())
hl = make_list_humidity(read())
        
    
def average_calculator(my_list: list):
    
    temp_l = np.array(my_list)
    print(np.mean(temp_l))

    return


average_calculator(tl)
average_calculator(hl)

def max_finder(my_list: list):
    temp_l = np.array(my_list)
    print(np.max(temp_l))

def min_finder(my_list: list):
    temp_l = np.array(my_list)
    print(np.min(temp_l))

max_finder(tl)
min_finder(tl)
max_finder(hl)
min_finder(hl)
    
# def main():
#     print("test")

# if __name__ == "__main__":
#     main()







