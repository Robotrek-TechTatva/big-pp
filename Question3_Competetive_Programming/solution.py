import csv

def area(x1, y1, x2, y2, x3, y3): 
  
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0) 

def isInside(lis):
    x, y = 0, 0 
    x1, y1, x2, y2, x3, y3 = lis[1:]
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    y1 = int(y1)
    y2 = int(y2)
    y3 = int(y3)
    A = area (x1, y1, x2, y2, x3, y3) 
    
    A1 = area (x, y, x2, y2, x3, y3)   
    A2 = area (x1, y1, x, y, x3, y3)  
    A3 = area (x1, y1, x2, y2, x, y) 
    
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False


filename = "traingles.csv"

with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if line:
            print(isInside(line))