# Eish Kapoor, Matt Seminatore, Kyle Mondina
# Scrambles Data
import random


pickedIdx = []
scrambledData = []

inputFile = open('./trimmedData.csv','r')
outputFile = open('./scrambledData.csv','w')

data = inputFile.readlines()
labels = data[0]
del data[0]


for i in range(len(data)):
    randomIdx = random.randint(0,len(data)-1)
    while(randomIdx in pickedIdx):
        randomIdx = random.randint(0,len(data)-1)
    pickedIdx.append(randomIdx)
    print(len(pickedIdx))
    scrambledData.append(data[randomIdx])

scrambledData.insert(0,labels)
for i in range(len(scrambledData)):
    outputFile.writelines(scrambledData[i])


outputFile.close()
inputFile.close()
