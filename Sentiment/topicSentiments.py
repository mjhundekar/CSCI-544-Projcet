import os, sys, codecs
from collections import defaultdict
reload(sys)
sys.setdefaultencoding("utf-8")


def getValues(word):
    #print "word================>",word,"================"
    inFilePath="/home/ankit081190/NLP/CSCI-544-Project/SentimentResultsFinal/"
    d = defaultdict(int)
    fileList=os.listdir(inFilePath)
#    print fileList
   
    for files in fileList:
        with codecs.open(inFilePath+files,"r", "utf-8") as f:
            for line in f:
                if word.decode("utf-8").strip() in line.strip().split(" "):
                    d[line.split(" :::: ")[0]] +=1
            f.close()
    return d;

with codecs.open("topics.txt", "r", "utf-8") as f:
    with codecs.open("topicSentiment.txt", "w", "utf-8") as fopen:
        for line in f:
            if ":" in line:
                #print line.split(":")[1].decode("utf-8")
                dict=getValues(line.split(":")[0].decode("utf-8").strip())
                dictStr=""
		for i, j in dict.items():
                    dictStr+=" :: "+str(i)+" : "+str(j)
                fopen.write(line.split(":")[0].decode("utf-8").strip()+" \t "+dictStr+"\n")
        fopen.close()
    f.close()



