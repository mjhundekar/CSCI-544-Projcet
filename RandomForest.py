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

directoryPath = "F:\USCSem3\NLP\NLPGit\DayWiseTfIdfCleanTweets\Final_Raw_Hand_Annotated_Files"
toBeAnnotatedDirectory = "F:\USCSem3\NLP\NLPGit\DayWiseTfIdfCleanTweets\Raw_Unannotated_Files" 
annotatedDirectory = "F:\USCSem3\NLP\NLPGit\DayWiseTfIdfCleanTweets\Final_Random_Forest_Annotated_Files"

tweetFiles = []
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
 
#75-25 Train-Test split results
X_train, X_test, y_train, y_test = train_test_split(tweetX, labels, test_size=0.25, random_state=42)
            
rf = RandomForestClassifier(n_estimators=50)
rf.classes_ = [0,1,-1]
rf.n_classes_  = 3
rf.fit(X_train, y_train)

a = rf.predict(X_test)

print 'Train-Test Split Results'
print np.sum(a == y_test)*100.0/len(y_test)


#Cross Validation Results
'''
rf = RandomForestClassifier(n_estimators=50)
rf.classes_ = [0,1,-1]
rf.n_classes_  = 3
rf.fit(tweetX,labels)


cv_scores = cross_val_score(rf, tweetX, labels, cv=10)
print '\nCross Validation Results'
print cv_scores                
print np.sum(cv_scores)/np.size(cv_scores)   
'''
#----------------------------------------------------------------------------------
#Annonatate Unknown tweets
unannotatedTweetFiles = []
unanTweetX = []

for root, dirs, files in os.walk(toBeAnnotatedDirectory):
    for f in files:
        print 'Processing '+f+' ...'
        temp_file = codecs.open(os.path.join(root, f), 'r', 'utf-8')
        unanTweets = temp_file.readlines()
        temp_file.close()
        
        unanTweetX = np.zeros((len(unanTweets),colSize))
        index = 0
        for unanTweet in unanTweets:            
            words = unanTweet.split(' ')
            for word in words:
                if word in bagOfWords:
                    unanTweetX[index][bagOfWords[word]] += 1
            index += 1 
        
        labels = rf.predict(unanTweetX)
        outputFile = codecs.open(os.path.join(annotatedDirectory, f), 'w', 'utf-8')
        
        index = 0
        for unanTweet in unanTweets:
            outputFile.write(str(labels[index])+' :::: '+unanTweet + '\n')
            index += 1
        outputFile.close()
        
        