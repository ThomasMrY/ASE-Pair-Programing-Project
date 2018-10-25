import re
import time
from collections import Counter
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'\
          ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

###################################################################################
#Name:count_letters
#Inputs:file name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountLetters(file_name):
    totalNum = 0
    dicNum = {}
    t0 = time.clock()
    with open(file_name) as f:
        txt = f.read()
    for letter in letters:
        dicNum[letter] = txt.count(letter) #here count is faster than re
        totalNum += dicNum[letter]
    t1 = time.clock()
    for letter in letters:
        dicNum[letter] = dicNum[letter]/totalNum
    dicNum = sorted(dicNum.items(), key = lambda k: k[1],reverse=True)
    t2 = time.clock()
    # print(l_num)
    # print(dic_num)
    # print(t1-t0)
    # print(t2-t1)
    print("--------------------------")
    print("|     The rank list      |")
    print("|   Letter   | Frequency |")
    for letter,fre in dicNum:
        print("|\t   %s | %.2f      |"%(letter,fre))
    print("--------------------------")
###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountWords(file_name,n,stopName,verbName):
    dicNum = {}
    totalNum = 0
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
    if (stopflag == True):
        tempc = Counter(wordList)
        dicNum = dict(tempc.most_common(n+stopNum))
        for word in stoplist:
            word = word.replace('\n','')
            del dicNum[word]
    else:
        tempc = Counter(wordList)
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
        verbDicNum = sorted(verbDicNum.items(), key=lambda k: k[1], reverse=True)
    dicNum = sorted(dicNum.items(), key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    if (verbflag == True):
        print("--------------------------------")
        print("|         The rank list        |")
        print("|   Word           | Frequency |")
        for word, fre in verbDicNum[:n]:
            print("|\t{:15}|{:<11.2f}|".format(word, fre / totalNum))
        print("--------------------------------")
    else:
        print("----------------------")
        print("|   The rank list    |")
        print("|   Word | Frequency |")
        for word, fre in dicNum:
            print("|\t{:5}|{:<11.2f}|" .format(word, fre/totalNum))
        print("----------------------")

    # print(t1-t0)

###################################################################################
#Name:CountWordsInDir
#Inputs:directory name,flag, the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountWordsInDir(Dir_name,flag,n,stopName,verbName):
    if(flag):
        for path, _, filelist in g:
            for filename in filelist:
                CountWords(os.path.join(path, filename),n,stopName,verbName)
    else:
        for file in os.listdir(Dir_name):
            CountWords(file,n,stopName,verbName)

###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountPhrases(file_name,k,n,stopName,verbName):
    dicNum = {}
    totalNum = 0
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
    pword = r'(([a-z]+\s+)+[a-z]+)'  # extract sentence
    pattern = re.compile(pword)
    sentence = pattern.findall(txt)
    txt = ','.join([sentence[m][0] for m in range(len(sentence))])
    if(stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
            stopNum = len(stoplist)
    pattern = "[a-z]+[0-9]*"
    for i in range(k-1):
        pattern += "[^a-z0-9]+[a-z]+[0-9]*"
    wordList = []
    for i in range(k):
        if( i == 0 ):
            tempList = re.findall(pattern, txt)
        else:
            wordpattern = "[a-z]+[0-9]*"
            txt = re.sub(wordpattern, '', txt, 1).strip()
            tempList = re.findall(pattern, txt)
        wordList += tempList
    if (stopflag == True):
        tempc = Counter(wordList)
        dicNum = dict(tempc.most_common(n+stopNum))
        for word in stoplist:
            word = word.replace('\n','')
            del dicNum[word]
    else:
        tempc = Counter(wordList)
        # totalNum = sum([tempc[x] for x in tempc.keys() if ',' not in x])
        # print(totalNum)
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
        verbDicNum = sorted(verbDicNum.items(), key=lambda k: k[1], reverse=True)
    dicNum = sorted(dicNum.items(), key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    if (verbflag == True):
        print("--------------------------------")
        print("|         The rank list        |")
        print("|   Word           | Frequency |")
        for word, fre in verbDicNum[:n]:
            print("|\t{:15}|{:<11.2f}|".format(word, fre))
        print("--------------------------------")
    else:
        print("----------------------------")
        print("|      The rank list       |")
        print("|   Word   | Frequency     |")
        for word, fre in dicNum:
            print("|\t{:5}|{:<11.2f}|" .format(word, fre))
        print("-----------------------------")
    print(t1-t0)

###################################################################################
#Name:CountWordsInDir
#Inputs:directory name,flag, the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountPhrasesInDir(Dir_name,k,flag,n,stopName,verbName):
    if(flag):
        for path, _, filelist in g:
            for filename in filelist:
                CountPhrases(os.path.join(path, filename),k,n,stopName,verbName)
    else:
        for file in os.listdir(Dir_name):
            CountPhrases(file,k,n,stopName,verbName)

###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountPreposition(file_name,n,stopName,verbName,prepositionName):
    dicNum = {}
    totalNum = 0
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
    with open(prepositionName) as f:
        pre = f.read()
    preList = pre.split('\n')
    verbDic = {}
    with open(verbName) as f:
        for line in f.readlines():
            key, value = line.split(' -> ')
            verbDic[key] = value.replace('\n', '').split(',')
            verbDic[key].append(key)
            pattern = '|'.join(verbDic[key]) + r"[\s|\t|\r|\n]+"
            for prew in preList:
                patternpre = pattern + prew
                dicNum[key+' '+pre] = len(re.findall(patternpre,txt))
                print(dicNum[key+' '+pre])
    print(dicNum)
#
# CountLetters('gone_with_the_wind.txt')
# CountWords('gone_with_the_wind.txt',10,None,None)
# CountPhrases('gone_with_the_wind.txt',2,10,None,None)
# CountPreposition('gone_with_the_wind.txt',10,None,'verbs.txt','prepositions.txt')