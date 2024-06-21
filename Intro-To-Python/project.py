import csv
import numpy as np
#read from file

def read():
    with open('Intro-To-Python/weatherdata.csv', 'r') as csvfile:
        #create a reader object
        csv_reader = csv.DictReader(csvfile)
        
        #create a list of dictionaries - list comprehension
        wdata = [row for row in csv_reader]
        
        return wdata
 

def average_calculator(my_list: list):
    temp_list = []
    for item in my_list:
        temp_list.append(int(item['Temperature']))
    tl = np.array(temp_list)

    temp_list2 = []
    for item in my_list:
        temp_list2.append(int(item['Humidity']))
    tl2 = np.array(temp_list2)

    print(np.mean(tl))
    print(np.mean(tl2))
    return


average_calculator(read())








