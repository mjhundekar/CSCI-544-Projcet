# -*- coding: utf-8 -*-
import json, string, io, codecs, pickle

model = {}
model2 = {}
with io.open("HSWN_WN.txt", encoding="utf-8") as f:
    content = f.readlines()

for line in content:
    words = line.split()
    pscore = float(words[2])
    nscore = float(words[3])
    synonyms = words[4].split(',')
    # print synonyms
    for eachWord in synonyms:
        if eachWord not in model:
            val = pscore - nscore
            #if check >= 0.1:
                #if pscore > nscore:
                    #tag = 1
                #else:
                    #tag = -1
            #else:
                #tag = 0
            #print eachWord
            model[eachWord] = val
        else:
            val = pscore - nscore
            model[eachWord] = float(model[eachWord] + val)/2

with open("sentiment_model.txt", "w") as f:
    json.dump(model, f)
