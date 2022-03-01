import csv
with open('tools_dh_proceedings.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        results=('2015: ',row['2015'], '2019: ',row['2019'],'sum: ',str(int(row['2015'])+int(row['2016'])+int(row['2017'])+int(row['2018'])+int(row['2019'])))

def dh(tool_name,tool_data):
    with open(tool_data) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["Tool"]==tool_name:
                print(row)
dh(input('Enter tool name: '),'tools_dh_proceedings.csv')

