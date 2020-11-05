import csv
filename = "points.csv"
#I am smort(atleast i think so)
with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    points = []
    for line in csv_reader:
        points.append(line)
    final_point = points[-1]
    if final_point[1] == '1':
        print('A')
    else:
        print('B')
        
    
