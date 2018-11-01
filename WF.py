import argparse
import sys
import re
import time
from collections import Counter
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
    print("File name:" + os.path.abspath(file_name))
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
    with open(file_name) as f:
        txt = f.read().lower()
    for letter in letters:
        dicNum[letter] = txt.count(letter) #here count is faster than re
        totalNum += dicNum[letter]
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
    print("File name:" + sys.path[0] + "\\" + file_name)
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
    pattern = r"[a-z][a-z0-9]*"
    wordList = re.findall(pattern,txt)
    totalNum = len(wordList)
    tempc = Counter(wordList)
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            del tempc[word]
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
        verbDicNum = sorted(verbDicNum.items(), key=lambda k: k[0])
        verbDicNum = sorted(verbDicNum, key=lambda k: k[1], reverse=True)
    dicNum = sorted(dicNum.items(), key=lambda k:k[0])
    dicNum = sorted(dicNum, key=lambda k:k[1], reverse=True)
    t1 = time.clock()
    if (verbflag == True):
        display(verbDicNum[:n], 'words',totalNum,3)
    else:
        display(dicNum,'words',totalNum,3)
    print("Time Consuming:%4f" % (t1 - t0))

###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountPhrases(file_name,n,stopName,verbName,k):
    print("File name:" + sys.path[0] + "\\" + file_name)
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
    txt = re.sub(r'\s+',' ',txt)
    pword = r'(([a-z]+ )+[a-z]+)'  # extract sentence
    pattern = re.compile(pword)
    sentence = pattern.findall(txt)
    txt = ','.join([sentence[m][0] for m in range(len(sentence))])
    if(stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
    pattern = "[a-z]+[0-9]*"
    for i in range(k-1):
        pattern += "[\s|,][a-z]+[0-9]*"
    wordList = []
    for i in range(k):
        if( i == 0 ):
            tempList = re.findall(pattern, txt)
        else:
            wordpattern = "[a-z]+[0-9]*"
            txt = re.sub(wordpattern, '', txt, 1).strip()
            tempList = re.findall(pattern, txt)
        wordList += tempList
    tempc = Counter(wordList)
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            del tempc[word]
    dicNum = {}
    if (verbflag == True):
        verbDic = {}
        with open(verbName) as f:
            for line in f.readlines():
                key,value = line.split(' -> ')
                for tverb in value.replace('\n', '').split(','):
                    verbDic[tverb] = key
                verbDic[key] = key
        for phrase in tempc.keys():
            if (',' not in phrase):
                totalNum += 1
                verbList = phrase.split(' ')
                normPhrase = verbList[0]
                for verb in verbList[1:]:
                    if verb in verbDic.keys():
                        verb = verbDic[verb]
                    normPhrase += ' ' + verb
                if (normPhrase in dicNum.keys()):
                    dicNum[normPhrase] += tempc[phrase]
                else:
                    dicNum[normPhrase] = tempc[phrase]
    else:
        phrases = tempc.keys()
        for phrase in phrases:
            if (',' not in phrase):
                dicNum[phrase] = tempc[phrase]
                totalNum += tempc[phrase]
    dicNum = sorted(dicNum.items(), key=lambda k: k[0])
    dicNum = sorted(dicNum, key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    display(dicNum[:n], 'Phrases',totalNum,3)
    print("Time Consuming:%4f" % (t1 - t0))

###################################################################################
#Name:count_words
#Inputs:file name,the first n words, stopfile name
#outputs:None
#Author: Thomas
#Date:2018.10.22
###################################################################################
def CountVerbPre(file_name,n,stopName,verbName,preName):
    print("File name:" + sys.path[0] + "\\" + file_name)
    dicNum = {}
    totalNum = 0
    if (stopName != None):
        stopflag = True
    else:
        stopflag = False
    t0 = time.clock()
    with open(file_name) as f:
        txt = f.read()
    txt = txt.lower()
    txt = re.sub(r'\s+',' ',txt)
    pword = r'(([a-z]+ )+[a-z]+)'  # extract sentence
    pattern = re.compile(pword)
    sentence = pattern.findall(txt)
    txt = ','.join([sentence[m][0] for m in range(len(sentence))])
    if(stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
    pattern = "[a-z]+[0-9]*"
    for i in range(1):
        pattern += "[\s|,][a-z]+[0-9]*"
    wordList = []
    for i in range(2):
        if( i == 0 ):
            tempList = re.findall(pattern, txt)
        else:
            wordpattern = "[a-z]+[0-9]*"
            txt = re.sub(wordpattern, '', txt, 1).strip()
            tempList = re.findall(pattern, txt)
        wordList += tempList

    tempc = Counter(wordList)
    with open(preName) as f:
        preTxt = f.read()
    preList = preTxt.split('\n')
    verbDic = {}
    with open(verbName) as f:
        for line in f.readlines():
            key,value = line.split(' -> ')
            for tverb in value.replace('\n','').split(','):
                verbDic[tverb] = key
            verbDic[key] = key
    for phrase in tempc.keys():
        if(',' not in phrase):
            totalNum += 1
            verb, pre = phrase.split(' ')
            if (verb in verbDic.keys() and pre in preList):
                normPhrase = verbDic[verb] + ' ' + pre
                if (normPhrase in dicNum.keys()):
                    dicNum[normPhrase] += tempc[phrase]
                else:
                    dicNum[normPhrase] = tempc[phrase]
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            del dicNum[word]
    dicNum = sorted(dicNum.items(), key=lambda k: k[0])
    dicNum = sorted(dicNum, key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    display(dicNum[:n], 'VerbPre',totalNum, 3)
    print("Time Consuming:%4f"%(t1-t0))

def display(dicNum,type,totalNum,k):
    maxLen = 0
    if(totalNum <= 0):
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
        for path, _, filelist in os.walk(Dir_name):
            for file in filelist:
                if(arges):
                    Fuc(os.path.join(path, file), n, stopName, verbName,arges[0])
                else:
                    Fuc(os.path.join(path, file),n,stopName,verbName)
            if not reflag:
                break

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-f','--countWords', help="Output word frequencies",action = "store_true")
group.add_argument('-c','--countChar', help="Output character frequencies",action = "store_true")
group.add_argument('-p','--phraseNum', help="Output phrase frequencies",type = int,default=0)
group.add_argument('-q','--preName', help="Output PREPOSITION pair frequencies")
parser.add_argument('-v','--verbFile', help="Verb file to normalize the veb tenses",default=None)
parser.add_argument('-d','--dirFlag', help="Treat the <file name> as an directory",action = "store_true")
parser.add_argument('-s','--reFlag', help="Verb file to normalize the veb tenses",action = "store_true")
parser.add_argument('-n','--num',type = int, help="Output only the top <num> iterms",default=10)
parser.add_argument('-x','--stopFile', help="Use <stop word> as a list of stop words, which are ignored in the count",default=None)
parser.add_argument('path', help="The file/directory to be operated with")


if(__name__ == '__main__'):
    args = parser.parse_args()
    if args.phraseNum < 0:
        print("Error: The num of words in a phrase should not be negative!!")
        sys.exit()
    if args.num < 0:
        print("Error: The num of the iterms output should not be negative!!")
        sys.exit()
    if (args.countWords):
        if(args.dirFlag):
            OperateInDir(CountWords,args.path, int(args.num), args.stopFile, args.verbFile,args.reFlag)
        else:
            CountWords(args.path, int(args.num), args.stopFile, args.verbFile)
    elif (args.countChar):
        if (args.dirFlag):
            OperateInDir(CountLetters, args.path, int(args.num), args.stopFile, args.verbFile, args.reFlag)
        else:
            CountLetters(args.path, int(args.num), args.stopFile, args.verbFile)
    elif (args.phraseNum):
        if (args.dirFlag):
            OperateInDir(CountPhrases, args.path, int(args.num), args.stopFile, args.verbFile, args.reFlag,int(args.phraseNum))
        else:
            CountPhrases(args.path, int(args.num), args.stopFile, args.verbFile,int(args.phraseNum))
    elif (args.preName):
        if (args.dirFlag):
            OperateInDir(CountVerbPre, args.path, int(args.num), args.stopFile, args.verbFile, args.reFlag,args.preName)
        else:
            CountVerbPre(args.path, int(args.num), args.stopFile, args.verbFile,args.preName)
    else:
        print("Error: Please input the operation type (-f|-q|-p|-c)")