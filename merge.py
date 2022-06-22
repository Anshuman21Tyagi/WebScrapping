import csv 

data1 = []
data2 = []

with open("stars.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        data1.append(i)

with open("convertedstars.csv","r") as f:
    reader = csv.reader(f)
    for i in reader:
        data2.append(i)

header1 = data1[0]
header2 = data2[0]

starname1 = data1[1:]
starname2 = data2[1:]

headers = header1 + header2
starname = []

for index,row in enumerate(starname1):
    starname.append(starname1[index] + starname2[index])

with open("merge.csv","a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(starname)