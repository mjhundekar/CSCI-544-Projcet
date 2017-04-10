# -*- coding: utf-8 -*-
import os, json, sys, codecs
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding("utf-8")



wordsDict=OrderedDict();
with codecs.open("/home/ankit/NLP_Project/CSCI-544-Projcet/Model/tfIdf.txt","r", "utf-8") as fp:
    wordsDict=json.load(fp)
    fp.close()

print wordsDict


fileList=os.listdir("/home/ankit/NLP_Project/CSCI-544-Projcet/CleanTweets/")
file_path = "/home/ankit/NLP_Project/CSCI-544-Projcet/CleanTweets/"
tfIdf_file_path = "/home/ankit/NLP_Project/CSCI-544-Projcet/TfIdfCleanTweets/"
#fileList=['2017-04-10-07-41-28.txt']

for files in fileList:
    docText=""
    if ".txt" in files:
        print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
	with open(file_path + files,'r') as fp:
	    for line in fp:
		#print "line=",line

                d=line.strip(" ").split(" ")
		for words in d:
		    if len(words)>0 and words.decode("utf-8") in wordsDict.keys() :
			docText+=words.strip().decode("utf-8")+" ";
		docText+="\n"
		#print "docText=",docText

	    with codecs.open(tfIdf_file_path + files,'w', 'utf-8') as fopen:
		fopen.write(docText.decode("utf-8"))
		docText=""
		fopen.close()
