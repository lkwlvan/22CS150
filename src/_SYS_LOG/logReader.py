import os
import numpy as np
import string
import pandas as pd
import csv


FolderPath = "./_SYS_LOG"
FilePath = "FinalTest2.txt"
FilePath2 = "FinalTest_AAMLoss.txt"
FilePath3 = "FinalTest2.txt"
FilePath4 = "FinalTest2.txt"
FilePath = os.path.join(FolderPath,FilePath)
FilePath2  = os.path.join(FolderPath,FilePath2)
FilePath3  = os.path.join(FolderPath,FilePath3)
FilePath4  = os.path.join(FolderPath,FilePath4)
testLines = [] 
trainLines = []
test2Lines = []
train2Lines = []
test3Lines = []
train3Lines = []
test4Lines = []
train4Lines = []
    
    
with open(FilePath, 'r', encoding='utf-8') as file:
    for line in file:
        if 'Test epoch' in line:
            testLines.append(line.split(","))
            
        if 'Train epoch' in line:
            trainLines.append(line.split(","))
with open(FilePath2, 'r', encoding='utf-8') as file:
    for line in file:
        if 'Test epoch' in line:
            test2Lines.append(line.split(","))
            
        if 'Train epoch' in line:
            train2Lines.append(line.split(","))
with open(FilePath3, 'r', encoding='utf-8') as file:
    for line in file:
        if 'Test epoch' in line:
            test3Lines.append(line.split(","))
            
        if 'Train epoch' in line:
            train3Lines.append(line.split(","))        
with open(FilePath4, 'r', encoding='utf-8') as file:
    for line in file:
        if 'Test epoch' in line:
            test4Lines.append(line.split(","))
            
        if 'Train epoch' in line:
            train4Lines.append(line.split(","))        

trainLoss = []
trainAcc = []
trainLR = []
trainSpeed = []
traineat = []

train2Loss = []
train2Acc = []
train2LR = []
train2Speed = []
train2eat = []

train3Loss = []
train3Acc = []
train3LR = []
train3Speed = []
train3eat = []

train4Loss = []
train4Acc = []
train4LR = []
train4Speed = []
train4eat = []

for itmes in trainLines:
    trainLoss.append(float(itmes[2].split(':')[1]))
    trainAcc.append(float(itmes[3].split(':')[1]))
    trainLR.append(float(itmes[4].split(':')[1]))
    trainSpeed.append(float(itmes[5].split(':')[1].replace("data/sec","")))
    #traineat.append(float(itmes[6].split(':')[1]))
print("+============================================")
for itmes in trainLines:
    train2Loss.append(float(itmes[2].split(':')[1]))
    train2Acc.append(float(itmes[3].split(':')[1]))
    train2LR.append(float(itmes[4].split(':')[1]))
    train2Speed.append(float(itmes[5].split(':')[1].replace("data/sec","")))
    #train2eat.append(float(itmes[6].split(':')[1]))
for itmes in trainLines:
    train3Loss.append(float(itmes[2].split(':')[1]))
    train3Acc.append(float(itmes[3].split(':')[1]))
    train3LR.append(float(itmes[4].split(':')[1]))
    train3Speed.append(float(itmes[5].split(':')[1].replace("data/sec","")))
    #train3eat.append(float(itmes[6].split(':')[1]))
for itmes in trainLines:
    train4Loss.append(float(itmes[2].split(':')[1]))
    train4Acc.append(float(itmes[3].split(':')[1]))
    train4LR.append(float(itmes[4].split(':')[1]))
    train4Speed.append(float(itmes[5].split(':')[1].replace("data/sec","")))
    #train4eat.append(float(itmes[6].split(':')[1]))
print("+============================================")

print('trainLoss:', (trainLoss))
print('trainAcc:', (trainAcc))
print('trainLR:', (trainLR))
print('trainLoss:', (trainLoss))
print('trainSpeed:', (trainSpeed))

#print('traineat:', (traineat))
print("+============================================")


testThreshold = []
testTpr = []
testFpr = []
testErr = []

test2Threshold = []
test2Tpr = []
test2Fpr = []
test2Err = []

test3Threshold = []
test3Tpr = []
test3Fpr = []
test3Err = []

test4Threshold = []
test4Tpr = []
test4Fpr = []
test4Err = []


for itmes in testLines:
    testThreshold.append(float(itmes[2].split(':')[1]))
    testTpr.append(float(itmes[3].split(':')[1]))
    testFpr.append(float(itmes[4].split(':')[1]))
    testErr.append(float(itmes[5].split(':')[1]))
for itmes in test2Lines:
    test2Threshold.append(float(itmes[2].split(':')[1]))
    test2Tpr.append(float(itmes[3].split(':')[1]))
    test2Fpr.append(float(itmes[4].split(':')[1]))
    test2Err.append(float(itmes[5].split(':')[1]))
for itmes in test3Lines:
    test3Threshold.append(float(itmes[2].split(':')[1]))
    test3Tpr.append(float(itmes[3].split(':')[1]))
    test3Fpr.append(float(itmes[4].split(':')[1]))
    test3Err.append(float(itmes[5].split(':')[1]))
for itmes in test4Lines:
    test4Threshold.append(float(itmes[2].split(':')[1]))
    test4Tpr.append(float(itmes[3].split(':')[1]))
    test4Fpr.append(float(itmes[4].split(':')[1]))
    test4Err.append(float(itmes[5].split(':')[1]))
print('testThreshold:',(testThreshold))
print('testTpr:',(testTpr))
print('testFpr:',(testFpr))
print('testErr:',(testErr))
print("+============================================")


from matplotlib import pyplot as plt

plt.plot(test2Err, label = "ECAPA-TDNN-SAP Err")
plt.plot(test2Fpr, label = "ECAPA-TDNN-SAP Fpr")
plt.legend()
plt.show()

plt.plot(test2Tpr, label = "ECAPA-TDNN-ASP Tpr")
plt.legend()
plt.show()



plt.plot(testErr, label = "GELoss Err")
plt.plot(test2Err, label = "AAMLoss Epr")
plt.legend()
plt.show()


plt.plot(testFpr, label = "GELoss Fpr")
plt.plot(test2Fpr, label = "AAMLoss Fpr")
plt.legend()
plt.show()



plt.plot(testTpr, label = "GELoss Tpr")
plt.plot(test2Tpr, label = "AAMLoss Tpr")
plt.legend()
plt.show()



# plt.plot(testTpr, label = "ECAPA-TDNN-ASP Tpr")
# plt.plot(test2Tpr, label = "ECAPA-TDNN-SAP Tpr")


# plt.plot(testErr, label = "ECAPA-TDNN-ASP Err")
# plt.plot(test2Err, label = "ECAPA-TDNN-SAP Err")
# plt.plot(test3Err, label = "TDNN-ASP Err")
# plt.plot(test4Err, label = "TDNN-SAP Err")
# plt.ylim(0,0.3)
# plt.legend()
# plt.show()

# plt.plot(testTpr, label = "ECAPA-TDNN-ASP Tpr")
# plt.plot(test2Tpr, label = "ECAPA-TDNN-SAP Tpr")
# plt.plot(test3Tpr, label = "TDNN-ASP Tpr")
# plt.plot(test4Tpr, label = "TDNN-SAP Tpr")
# plt.legend()
# plt.show()



# plt.plot(testFpr, label = "ECAPA-TDNN-ASP Fpr")
# plt.plot(test2Fpr, label = "ECAPA-TDNN-SAP Fpr")
# plt.plot(test3Fpr, label = "TDNN-ASP Fpr")
# plt.plot(test4Fpr, label = "TDNN-SAP Fpr")
# plt.ylim(0,0.3)
# plt.legend()
# plt.show()




