import csv
import math

data_traff = {'out': [], 'in': []}  # Array for storing incoming, outgoing traffic

def csv_dict_reader_traff(file_obj,ip): #Function for parsing a csv - file and filling the array with data
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
        #print(line)
        if line['da'] == ip:
           data_traff['in'].append(line['ibyt'])
        if line['sa'] == ip:
            data_traff['out'].append(line['obyt'])

def traffic(data): # Payment calculation
    price = 0
    traf_Mbit = 0
    sum_traf = 0

    for traf_out in data['out']:
        sum_traf+= float(traf_out)
    for traf_in in data['in']:
        sum_traf += float(traf_in)
    traf_Mbit = sum_traf / (131072) - 1000 # From bytes to Mbit

    print('sum_traf = ' , sum_traf )
    print('traf_Mbit = ' , traf_Mbit )


    price+=round(math.ceil(traf_Mbit*100)/100, 2)*1 #  - 1 rub / Mbit
    return price


with open("file.csv") as f_obj:
        ip = input("Enter ip: ")
        csv_dict_reader_traff(f_obj, ip)
        print('Price = ', traffic(data_traff))