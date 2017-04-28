# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 02:00:47 2017

@author: Sagar Makwana
"""
import codecs
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

directoryPath = "F:\USCSem3\NLP\NLPProjectResources\AnnotatedTweets"
devTweetsDirPath = ""
tweetFiles = []
tweetVector = []
tweets = []
labels = []

bagOfWords = {}

for root, dirs, files in os.walk(directoryPath):
    for f in files:
        temp_file = codecs.open(os.path.join(root, f), 'r', 'utf-8')
        tweetFiles.append(temp_file.readlines())
        temp_file.close()
        
index = 0
for tweetFile in tweetFiles:
    for tweetandlabel in tweetFile:
        tweetSplit = tweetandlabel.strip().split(':::') 
        tweet = tweetSplit[0].strip()
        label = int(tweetSplit[1].strip())
        tweets.append(tweet)
        labels.append(label)
        
        words = tweet.split(' ')
        for word in words:
            if word not in bagOfWords:    
                bagOfWords[word] = index
                index += 1 
  
labels = np.asarray(labels)

colSize = len(bagOfWords)
rowSize = len(tweets)

tweetX = np.zeros((rowSize,colSize))

index = 0
for tweet in tweets:
    words = tweet.split(' ')
    for word in words:
        tweetX[index][bagOfWords[word]] += 1
    index += 1
 

X_train, X_test, y_train, y_test = train_test_split(tweetX, labels, test_size=0.25, random_state=42)
            
rf = RandomForestClassifier(n_estimators=50)
rf.classes_ = [0,1,-1]
rf.n_classes_  = 3
rf.fit(X_train, y_train)

a = rf.predict(X_test)
print np.sum(a == y_test)*100.0/len(y_test)

#scores = cross_val_score(rf, tweetX, labels, cv=10)
                
#print np.sum(a == labels)*100.0/len(tweets)
#print np.sum(scores)/np.size(scores)   
    
         