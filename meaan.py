import csv
with open('height.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
#print(file_data)
new_data=[]
for i in range(len(file_data)):
    num =file_data[i][1]
    new_data.append(float(num))

n=len(new_data)
total=0
for h in new_data:
    total=total+h
mean=total/n
print("total"+str(total))
print(str(total/n))
            