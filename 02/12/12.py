import numpy as np
import csv


def createFile(filename,data):
    with open(filename,"w") as file:
        for line in data:
            file.write(line+"\n")
        
col1 = []
col2 = []
with open("hightemp.txt","r") as file:
    reader = csv.reader(file,delimiter="\t")
    for index, row in enumerate(reader):    
        col1.append(row[0])
        col2.append(row[1])

createFile("col1.txt",col1)
createFile("col2.txt",col2)