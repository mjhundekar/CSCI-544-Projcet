import os, re, string
from gensim import corpora, utils
from gensim.models.wrappers.dtmmodel import DtmModel
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import sys;
reload(sys)
import codecs;
sys.setdefaultencoding("utf-8")


DTM_PATH="/home/ankit/NLP_Project/dtm/dtm/"


#documents is a list of list containing words for each tweet
documents=[]

filePath="/home/ankit/NLP_Project/NLPProject/TfIdfCleanTweets/"
fileList=os.listdir(filePath)


for files in fileList:

    #Write down clean tweets for sentiment analysis
    with codecs.open(filePath+files, 'r', 'utf-8') as f:
        d=[]
        for line in f:
            for words in line.strip(" ").split(" "):
                if len(words.strip(" ")) > 0:
                    d.append(words.strip(" "))
        documents.append(d);
                
    f.close()



#time seq required for DTM (Should contain all 1s for our tweets case)
#time_seq = [3, 7]
time_seq=[];
for i in range(1,len(documents)+1):
    time_seq.append(1);


#Corpus class for DTM data load
class DTMcorpus(corpora.textcorpus.TextCorpus):
    def get_texts(self):
        return self.input
    def __len__(self):
        return len(self.input)

corpus = DTMcorpus(documents)


#path where dtm file is installed
dtm_path="/home/ankit/NLP_Project/dtm/dtm/dtm"
model = DtmModel.load("DTMMOdel.txt")


#model.save("DTModel.txt")
#Gives top 25 topics
tp= model.show_topics(num_topics=-1, times=1, num_words=100, log=False, formatted=False)
print tp
print type(tp)
for i in tp:
    for j in i:
        print type(j), j[1].decode("utf-8")

    #print i.decode("utf-8")
#for i, j in cnt:
#    print i,j.decode("utf-8")
#print "model.num_topics=",model.num_topics
#for i in range(0,model.num_topics):
#    print "model.show_topic",model.print_topics(num_topics=10, times=1, num_words=100)
    
    
