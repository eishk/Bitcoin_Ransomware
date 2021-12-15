# Eish Kapoor, Matt Seminatore, Kyle Mondina
# Splits original file into 40k, balanced dataset
import random

file = open('.\BitcoinHeistData.csv','r')
data = file.readlines()


labels = data[0]

#removing the labels
del data[0]

ransomWareIdx = 40000

randomRansomWare = []
pickedIdxs = []

for i in range(20000):
    randomIdx = random.randint(0,ransomWareIdx-1)
    while(randomIdx in pickedIdxs):
        randomIdx = random.randint(0,ransomWareIdx-1)
    pickedIdxs.append(randomIdx)
    randomRansomWare.append(data[randomIdx])

randomWhite = []
pickedIdxs = []
for i in range(20000):
    randomIdx = random.randint(ransomWareIdx,len(data)-1)
    while(randomIdx in pickedIdxs):
        randomIdx = random.randint(ransomWareIdx,len(data)-1)
    pickedIdxs.append(randomIdx)
    randomWhite.append(data[randomIdx])

preprocessedData = randomRansomWare + randomWhite
preprocessedData.insert(0,labels)
trimmedData = open('trimmedData.csv','w')
for i in range(len(preprocessedData)):
    trimmedData.writelines(preprocessedData[i])


#andomIdx = -1
#for i in range(20000):
    

trimmedData.close()
file.close()
