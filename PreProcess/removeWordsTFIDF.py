# -*- coding: utf-8 -*-
import os, json, sys, codecs
from collections import OrderedDict
os.system("taskset -p 0xffff %d" % os.getpid())
reload(sys)
sys.setdefaultencoding("utf-8")



wordsDict=OrderedDict();
with codecs.open("/home/ankit081190/NLP/CSCI-544-Project/Model/tfIdf.txt","r", "utf-8") as fp:
    wordsDict=json.load(fp)
    fp.close()

#print wordsDict

#for key, value in sorted(wordsDict.items()):
#    print key, value
#exit(1)

fileList=os.listdir("/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/toBeAnnotated/")
file_path = "/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/toBeAnnotated/"
tfIdf_file_path = "/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/toBeAnnotated/"
fileList=["2017-04-09.txt", "2017-04-10.txt", "2017-04-12.txt", "2017-04-18.txt", "2017-04-15.txt"]
for files in fileList:
    docText=""
    if ".txt" in files:
        print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
	with open(file_path + files,'r') as fp:
	    for line in fp:
		#print "line=",line
		senti=(line.split(" ::: "))[1]
                d=((line.split(" ::: "))[0]).strip(" ").strip("\n").split(" ")
                t=1;
		for words in d:
#                    print words
		    if len(words)>0 and words.decode("utf-8") in wordsDict.keys() :
#                        print words.decode("utf-8"), wordsDict[words.decode("utf-8")]
                        if words.strip().decode("utf-8")+" " != " ":
    			    docText+=words.strip().decode("utf-8")+" ";
                            t=0;
                if t==0:
		    docText+=" ::: "+senti
		#print "docText=",docText

	    with codecs.open(tfIdf_file_path +"Annotated_"+ files,'w', 'utf-8') as fopen:
		fopen.write(docText.decode("utf-8"))
		docText=""
		fopen.close()
            fp.close();
