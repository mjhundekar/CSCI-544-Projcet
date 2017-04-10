import logging
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


#For Hindi Stop Words Removal
def regex_tokenizer(doc):
    """Return a function that split a string in sequence of tokens"""
    token_pattern=r"(?u)\b\w\w+\b"
    token_pattern = re.compile(token_pattern)
    return token_pattern.findall(doc)

hindiStopWords=[]
with codecs.open("/home/ankit/NLP_Project/CSCI-544-Projcet/hindiST.txt", "r", "utf-8") as f:
    for line in f:
        hindiStopWords.append(line.decode("utf-8").strip("\n").strip())
f.close()
stop_words = [word.encode("utf-8") for word in hindiStopWords]
vectorizer = TfidfVectorizer(stop_words = stop_words, tokenizer = regex_tokenizer)
#End of loading Hindi Stop Words file


#For removal of Stop Words
def filter_list(full_list):
    s = set(hindiStopWords)
    '''print s;
    for  x in full_list :
        print x'''
    return (x for x in full_list if x not in s)
#End Stop Words removal


#documents is a list of list containing words for each tweet
documents=[]


#Start with a single file
with codecs.open('/home/ankit/NLP_Project/NLPProject/2017-04-09-10-41-28.txt', 'r', 'utf-8') as f:
    #rawDataList=f.read().replace(" :::: \n"," ::::: ").replace("\n","").replace(" ::::: "," :::: \n").split("\n")
    rawDataList=f.read().replace(" :::: \n"," ::::: ").replace("\n","").replace(" ::::: "," :::: \n").split("\n")

f.close();




#Write down clean tweets for sentiment analysis
with codecs.open('/home/ankit/NLP_Project/NLPProject/Clean_Tweet_2017-04-09-10-41-28.txt', 'w', 'utf-8') as f:
    for line in rawDataList:
        tweet=line.replace('#','').strip().decode("utf-8").split(" :::: ")[1]
        #print tweet
        #print re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', tweet,  flags=re.IGNORECASE)
        tweetCleaned=re.sub(r'#(\w+)|(http|https|ftp)://[a-zA-Z0-9\\./]+|@(\w+)', '', tweet,  flags=re.IGNORECASE)
        tweetCleaned = re.sub('[%s]' % re.escape(string.punctuation), '', tweetCleaned).strip()
        #print tweetCleaned,"\n"
        d=[]
        d=tweetCleaned.decode("utf-8").split(' ')
        features=list(filter_list(d))
        f.write(" ".join(features)+"\n")
        documents.append(features)
        '''        print "!!!!!!!d=",d
        if len(d) > 0:
            vectorizer.fit_transform(d)
            features = vectorizer.get_feature_names()
	    print "feature=",features
            documents.append(features)
        '''
    f.close()


	
for i in range(len(documents)):
    spaceRemovedDocument=[];
    for j in range(len(documents[i])):
        if len(documents[i][j].strip())>0:
            spaceRemovedDocument.append(documents[i][j].strip().decode("utf-8"))
    if len(spaceRemovedDocument) > 0:
        documents[i]=spaceRemovedDocument    
        #print documents[i][j].decode("utf-8")
	
    print i, documents[i];


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
topics = model.show_topic(topicid=0, time=1, num_words=25)
cnt= Counter(topics)
for i,j in cnt:
    print i,j;

