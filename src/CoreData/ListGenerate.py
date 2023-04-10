import os
from pydub import AudioSegment
import shutil
import glob
import numpy as np
import pandas as pd
import json
import datasetConfig
from responses import target
import random
sr = 16000


def buildWav(mp3FolderPath, wavFolderPath="wav_Data"):          #buildWav("./mp3_DataTest","./wav_DataTest")
    mp3FileList = os.listdir(mp3FolderPath)#mp3FolderPath
    for i in mp3FileList:
        sourcePath = os.path.join(mp3FolderPath,i)
        dstPath = sourcePath.replace(mp3FolderPath,wavFolderPath)
        
        print(sourcePath)
        print(dstPath)
        sound = AudioSegment.from_mp3(sourcePath)
        sound.export(dstPath.replace(".mp3",".wav"), format="wav")   

def buildCommonVoiceHKzhDataBase(wavfilePath,DatasetPath):
    validated_Table = pd.read_csv('validated.tsv', sep='\t')
    clientIDList = validated_Table["client_id"].values.tolist()
    clientIDList = list(set(clientIDList))

    clipPathList = validated_Table["path"].values.tolist()

    test = wavfilePath
    
    #create dst folder 
    if not os.path.exists(DatasetPath):
        os.makedirs(DatasetPath)
    #for index in range(len(clientIDList)) :
        #os.makedirs("./wav/p{:05}".format(index))
        
    fileList = glob.glob('./Data/*.wav')

    voiceCountPreID = [0]*len(clientIDList)

    count = 0
        
    for row in validated_Table.itertuples(index=True, name='Pandas'):
        clientId = row.client_id
        mp3Path = row.path
        clientIndex = clientIDList.index(clientId)
        srcPath = './Data/{str}'.format(str=mp3Path.replace(".mp3",".wav"))
        desPath = './wav/p{:05}/{:03}.wav'.format(clientIndex,voiceCountPreID[clientIndex])
        voiceCountPreID[clientIndex] = voiceCountPreID[clientIndex]+1
        shutil.move(srcPath,desPath)
        count+=1
        print(count/100000) 

def generatList():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return ""


def generateJson():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return ""



TargetList = [1494, 477, 1600, 787, 2043, 1772, 1240, 414, 1517, 432]

TotalSpeakerLimitation = -1


minVoiceDataPerSpeaker = 5
maxVoiceDataPerSpeaker = 30
wavFolderPath = "wav"
dstFolderPath = "wav_5perSpeaker"  
    

    
    
trainPathList = []
testPathList = []

    
speakerList = glob.glob('./Data/wav/*')
voiceCountPreIndex = []
#print(arr)
for i in speakerList:
    voiceCountPreIndex.append(len(glob.glob('./Data/wav/p{a}/*.wav'.format(a=i[-5:]))))

print("Total Speaker: ",len(voiceCountPreIndex))

IndexList = []
jsonData = [{}]
for index in range(len(voiceCountPreIndex)):
    if voiceCountPreIndex[index]>=minVoiceDataPerSpeaker:
        IndexList.append(index)
print("Total valid Speaker: ",len(IndexList))
test_listfile = open('./Data/test_list.txt','w')
train_listfile = open('./Data/train_list.txt','w')
indexCount = 0
speakIDList = []
max = -1
maxIndex = -1
maxList = []


newList=[0] * 1501
for index in IndexList:
    #if index in TargetList:
        #continue
    speakIDList.append("p{:05}".format(index))
    if indexCount>=TotalSpeakerLimitation and TotalSpeakerLimitation != -1:
        break
    print(index/len(voiceCountPreIndex)*100,"%")
    speakVoiceDataList = glob.glob("./Data/wav/p{:05}/*".format(index))
    DataPerSpeakercount = 0
    for j in speakVoiceDataList:
        
        if DataPerSpeakercount > maxVoiceDataPerSpeaker and maxVoiceDataPerSpeaker!=-1:
            break
        
        dir = os.path.split(j)[0]
        trainPathList.append({'wav':j,'labels':indexCount})
        #train_listfile.write(j.replace("/wav",'/Data/wav')+"\t"+str(indexCount)+"\n")
        
        a = random.uniform(0.0,1.0)

        if DataPerSpeakercount <2:
            test_listfile.write(j.replace("/Data/","/dataset/")+"\t"+str(indexCount)+"\n")
        else:
            train_listfile.write(j.replace("/Data/","/dataset/")+"\t"+str(indexCount)+"\n")

        DataPerSpeakercount = DataPerSpeakercount+1
    maxList.append((DataPerSpeakercount,index))
    if (DataPerSpeakercount> max):
        
        max = DataPerSpeakercount
        maxIndex = index
    indexCount = indexCount + 1 
    if DataPerSpeakercount < 200:
        
        newList[DataPerSpeakercount] = newList[DataPerSpeakercount] +1
    else:
        newList[200] = newList[200] +1
#maxList = sorted(maxList)
#print(maxList)

newList = newList[:50]

print(newList)
import matplotlib.pyplot as plt
#plt.scatter(newList)
plt.bar(range(50),newList )
plt.xlabel("VoiceData Count")
plt.ylabel("Speaker Count")
plt.show() #display the graph
#newList  = []