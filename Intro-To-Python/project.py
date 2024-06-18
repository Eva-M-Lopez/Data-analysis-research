import csv
#read from file
with open('Intro-To-Python/sleepdata.csv', 'r') as csvfile:
    #create a reader object
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    #print(header)
    my_list = []
    for row in csv_reader:
        my_list.append(row)
    print(my_list)
