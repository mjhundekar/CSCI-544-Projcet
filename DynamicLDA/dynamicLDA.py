import os, re, string
from gensim import corpora, utils
from gensim.models.wrappers.dtmmodel import DtmModel
from gensim.models.ldamulticore import LdaMulticore
from gensim.models.ldamodel import *;
from gensim.corpora.dictionary import Dictionary;
import pyLDAvis.gensim


import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import sys;
reload(sys)
import codecs;
sys.setdefaultencoding("utf-8")


DTM_PATH="/home/ankit081190/NLP/dtm/dtm"


#documents is a list of list containing words for each tweet
documents=[]

filePath="/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/Cleaned/"
fileList=os.listdir(filePath)


for files in fileList:

    #Write down clean tweets for sentiment analysis
    with codecs.open(filePath+files, 'r', 'utf-8') as f:
        d=[]
        for line in f:
            for words in line.strip(" ").split(" "):
                if len(words.strip(" ").strip("\n")) > 0:
                    d.append(words.strip(" ").strip("\n"))
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

    #corpus = DTMcorpus(documents)
    corpus=documents
    dictionary=Dictionary(corpus)

    corpus = [dictionary.doc2bow(doc) for doc in corpus]
    for (token, uid) in dictionary.token2id.items():
            dictionary.id2token[uid] = token

    print type(dictionary), type(corpus)

    #path where dtm file is installed
    dtm_path="/home/ankit081190/NLP/dtm/dtm/dtm"

    #model = DtmModel(dtm_path, corpus, time_seq, num_topics=1,
    #                 id2word=corpus.dictionary, initialize_lda=True)

    model=LdaMulticore(corpus, num_topics=10, id2word=dictionary)

    model.save("DTModelMultiCore_"+files+".model")
    #Gives top 25 topics

    tp= model.show_topics(num_topics=25, log=False, formatted=True)
    print model.print_topics(num_topics=25)
    data = pyLDAvis.gensim.prepare(model, corpus, dictionary)
    pyLDAvis.save_html(data, 'index_lda_'+files+'.html')

    cnt= Counter(tp)
    with codecs.open("topicsMultiLDA"+files+".txt","w", "utf-8") as f:
        for i,j in cnt:
            print i,j;
            f.write("\nFor Topic Number "+str(i)+":\n"+str(j).decode("utf-8")+"\n")
        f.close()

    #for i, j in cnt:
    #    print "\nFor topic number: " ,i, "\n"; 
    #    print j.decode("utf-8")
    #for i in range(0,model.num_topics-1)):
    #    print model.show_topic
    
    
    #topics = model.show_topic(topicid=0, time=1, num_words=100)
    #cnt= Counter(topics)
    #with codecs.open("topicsMultiLDA.txt","w", "utf-8") as f:
    #    for i,j in cnt:
    #        print i,j;
    #        f.write(str(i)+":"+str(j).decode("utf-8")+"\n")
    #    f.close()
