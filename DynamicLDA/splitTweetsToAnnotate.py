# -*- coding: utf-8 -*-
import os, re
from collections import defaultdict
import sys
import codecs
import math


keyWordsDict=defaultdict(int)

with codecs.open("topicsMultiLDA.txt", "r", "UTF-8") as fp:
    for line in fp:
        allValues=re.findall(r'"(.*?)"', line)
        for val in allValues:
            keyWordsDict[val]+=1

with codecs.open("topic.txt", "w", "UTF-8") as fout:
    for key, value in sorted(keyWordsDict.iteritems(), key=lambda (k,v): (v,k), reverse = True):
        if (value > 10):
            fout.write(key+":"+str(value)+"\n")
        print key
    fout.close()

exit(1)



path="../DayWiseTfIdfCleanTweets/"
files=os.listdir(path)
for file in files:
    if "txt" in file:
        i=0
        tweetsToBeWritten=defaultdict(int)
        with codecs.open(path+file,"r","UTF8") as fp:
            with codecs.open("../DayWiseTfIdfCleanTweets/toBeAnnotated/"+file,"w","UTF-8") as fout:
                for line in fp:
                    wordList=line.strip().split(" ")
                    for words in wordList:
                        if words in keyWordsDict and i<250 and tweetsToBeWritten[line]==0:
                            tweetsToBeWritten[line]+=1
                            fout.write(line)
                            i+=1
                            break
                fout.close()
            fp.close()
                        
        
    
