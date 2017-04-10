# -*- coding: utf-8 -*-
import json, string, codecs, os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fileList=os.listdir("D:/NLP/Project/CSCI-544-Project/TfIdfCleanTweets/")
file_path = "D:/NLP/Project/CSCI-544-Project/TfIdfCleanTweets/"
outputPath = "D:/NLP/Project/CSCI-544-Project/SentimentResults/"

def sentiment_ananlysis(tweets):
    output = []
    for tweet in tweets:
        tweetWords = tweet.split(" ")
        value = 0
        for word in tweetWords:
            if word != " ":
                if word in model:
                    print word, model[word]
                    value += model[word]
        if value < 0:
            sentiment = -1
        if value == 0:
            sentiment = 0
        if value > 0:
            sentiment = 1

        # sentiment = maxIndex(score)
        # print tweet
        output.append(str(sentiment) + " :::: " + tweet)

    with codecs.open(outputPath + file, 'w', 'utf-8') as fopen:
        for line in output:
            fopen.write(line)
    fopen.close()

    #with open('sentiment-output.txt', 'w') as f:
     #   for line in output:
      #      f.write(line)
    #f.close()

model = {}
with codecs.open("sentiment_model.txt", "r", "utf-8") as f:
    model = json.load(f)
    print "model", model


dict_list = {}
dict_words = {}
for file in fileList:
    if ".txt" in file:
        print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",file
        tweets = []
        print file_path+file
        for line in codecs.open(file_path + file, "r", "utf-8"):
            if line != "":
                tweets.append(line)
        print "content", tweets
        sentiment_ananlysis(tweets)






