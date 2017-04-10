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
                d.append(words.strip())
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
model = DtmModel(dtm_path, corpus, time_seq, num_topics=1,
                 id2word=corpus.dictionary, initialize_lda=True)


#Gives top 25 topics
topics = model.show_topic(topicid=0, time=1, num_words=100)
cnt= Counter(topics)
with codecs.open("topics.txt","w", "utf-8") as f:
    for i,j in cnt:
        print i,j;
        f.write(str(i)+":"+str(j).decode("utf-8")+"\n")
    f.close()
