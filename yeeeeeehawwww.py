import csv
import math
with open popop.csv newline = ''  as f: 
    f = "popop.csv"
    reader = csv.reader (f)
    data=list(reader)

data.pop(0)

totalmarks=0
totalenteries= len(data)

for marks in data:
    totalmarks = totalmarks + float(marks[1])

mean = totalmarks/totalenteries
print("mean is this, i guess, i'm not a mathmatician lol ¯\(◉◡◔)/¯" + str(mean))


squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

sum =0
for i in squared_list:
    sum =sum + i

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)
