# -*- coding: utf-8 -*-
import json, string, codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''def maxIndex(score):
    a = score[0]
    y = score[1]
    z = score[2]
    Max = a
    index = 0
    sentiment = 0
    if y > Max:
        Max = y
        index = 1
    if z > Max:
        Max = z
        index = 2
        if y > z:
            Max = y
            index = 1
    if score[index] == 0:
        sentiment = -1
    if score[index] == 1:
        sentiment = 0
    if score[index] == 2:
        sentiment = 1
    return sentiment
'''
#tweets = fileRead('Clean_Tweet_2017-04-09-10-41-28.txt')
tweets = []
for line in codecs.open('Clean_Tweet_test.txt', "r", "utf-8"):
    tweets.append(line)
print "content", tweets

model = {}
with codecs.open("sentiment_model.txt", "r", "utf-8") as f:
    model = json.load(f)
    print "model", model

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

    #sentiment = maxIndex(score)
    #print tweet
    output.append(str(sentiment) + " " + tweet)

with open('sentiment-output.txt', 'w') as f:
    for line in output:
        f.write(line)
f.close()



