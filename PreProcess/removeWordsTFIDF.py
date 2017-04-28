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

fileList=os.listdir("/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/")
file_path = "/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/"
tfIdf_file_path = "/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/Cleaned/"
#fileList=["trim_2017-04-09.txt"]
for files in fileList:
    docText=""
    if ".txt" in files:
        print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
	with open(file_path + files,'r') as fp:
	    for line in fp:
		#print "line=",line

                d=line.strip(" ").strip("\n").split(" ")
                t=1;
		for words in d:
#                    print words
		    if len(words)>0 and words.decode("utf-8") in wordsDict.keys() :
#                        print words.decode("utf-8"), wordsDict[words.decode("utf-8")]
                        if words.strip().decode("utf-8")+" " != " ":
    			    docText+=words.strip().decode("utf-8")+" ";
                            t=0;
                if t==0:
		    docText+="\n"
		#print "docText=",docText

	    with codecs.open(tfIdf_file_path + files,'w', 'utf-8') as fopen:
		fopen.write(docText.decode("utf-8"))
		docText=""
		fopen.close()
            fp.close();
