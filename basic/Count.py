import re
import time
from collections import Counter
import operator as op
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
          #,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

###################################################################################
#Name:count_letters
#Inputs:file name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountLetters(file_name,n,stopName,verbName):
    print("File name:" + file_name)
    if (stopName != None):
        stopflag = True
    else:
        stopflag = False
    if(verbName != None):
        print("Verb tenses normalizing is not supported in this function!")
    else:
        pass
    totalNum = 0
    dicNum = {}
    t0 = time.clock()
    if (stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
            stopNum = len(stoplist)
    with open(file_name) as f:
        txt = f.read().lower()
    for letter in letters:
        dicNum[letter] = txt.count(letter) #here count is faster than re
        totalNum += dicNum[letter]
    for letter in letters:
        dicNum[letter] = dicNum[letter]
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            try:
                del dicNum[word]
            except:
                pass
    dicNum = sorted(dicNum.items(), key=lambda k: k[0])
    dicNum = sorted(dicNum, key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    display(dicNum[:n],'character',totalNum,9)
    print("Time Consuming:%4f" % (t1 - t0))


###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountWords(file_name,n,stopName,verbName):
    print("File name:" + file_name)
    if (stopName != None):
        stopflag = True
    else:
        stopflag = False
    if(verbName != None):
        verbflag = True
    else:
        verbflag = False
    t0 = time.clock()
    with open(file_name) as f:
        txt = f.read()
    txt = txt.lower()
    if(stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
            stopNum = len(stoplist)
    pattern = r"[a-z][a-z0-9]*"
    wordList = re.findall(pattern,txt)
    totalNum = len(wordList)
    tempc = Counter(wordList)
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            try:
                del tempc[word]
            except:
                pass
    dicNum = dict(tempc.most_common(n))
    if (verbflag == True):
        totalNum = 0
        verbDic = {}
        verbDicNum = {}
        with open(verbName) as f:
            for line in f.readlines():
                key,value = line.split(' -> ')
                verbDic[key] = value.replace('\n','').split(',')
                verbDicNum[key] = tempc[key]
                for word in verbDic[key]:
                    verbDicNum[key] += tempc[word]
                totalNum += verbDicNum[key]
        verbDicNum = sorted(dicNum.items(), key=lambda k: k[0])
        verbDicNum = sorted(verbDicNum, key=lambda k: k[1], reverse=True)
    dicNum = sorted(dicNum.items(), key=lambda k:k[0])
    dicNum = sorted(dicNum, key=lambda k:k[1], reverse=True)
    t1 = time.clock()
    if (verbflag == True):
        display(verbDicNum[:n], 'words',totalNum,3)
    else:
        display(dicNum,'words',totalNum,3)
    print("Time Consuming:%4f" % (t1 - t0))

def display(dicNum,type,totalNum,k):
    maxLen = 0
    if(not dicNum):
        print("Error:Nothing matched!!")
        return
    for word, fre in dicNum:
        if(len(word)>maxLen):
            maxLen = len(word)
    print("-"*int(2.18*k*maxLen))
    formatstr = "|{:^" + str(2*k * maxLen+1) + "}|"
    print(formatstr.format('The Rank List'))
    formatstr = "|{:" + str(k*maxLen) + "}|{:<" + str(k*maxLen) + "}|"
    print(formatstr.format(type, "Frequency"))
    formatstr = "|{:" + str(k*maxLen) + "}|{:<" + str(k*maxLen) + ".2%}|"
    for word, fre in dicNum:
        print(formatstr.format(word, fre/totalNum))
    print("-" * int(2.18*k * maxLen))

###################################################################################
#Name:CountWordsInDir
#Inputs:directory name,flag, the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def OperateInDir(Fuc,Dir_name,n,stopName,verbName,reflag,*arges):
    if(reflag):
        for path, _, filelist in os.walk(Dir_name):
            for file in filelist:
                if(arges):
                    Fuc(os.path.join(path, file), n, stopName, verbName,arges[0])
                else:
                    Fuc(os.path.join(path, file),n,stopName,verbName)
    else:
        for file in os.listdir(Dir_name):
            if(os.path.isdir(os.path.join(Dir_name, file))):
                pass
            else:
                if (arges):
                    Fuc(os.path.join(Dir_name, file), n, stopName, verbName, arges[0])
                else:
                    Fuc(os.path.join(Dir_name, file), n, stopName, verbName)