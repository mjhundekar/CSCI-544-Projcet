import os, sys, codecs, math, json
from collections import OrderedDict

def tf(word, curr_dict):
    return curr_dict[word] / (len(curr_dict) * 1.0)
    

def n_containing(word, dict_list):
    #    print 'n_containing ' + word
    #    print 'n_containing ' +str(sum(1 for blob in bloblist.values() if word in blob))
    cnt = 0
    for a_dict in dict_list.values():
        if word in a_dict:
            cnt += 1

    return cnt


def idf(word, dict_list):
    return math.log(len(dict_list) / (1.0 + n_containing(word, dict_list)))


# tfidf(word, review[key], review) for word in review[key]}
# tfidf(word, blob, blob_list)

def tfidf(word, curr_dict, dict_list):
    return tf(word, curr_dict) * idf(word, dict_list)


fileList=os.listdir("/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/")
file_path = "/home/ankit081190/NLP/CSCI-544-Project/DayWiseTfIdfCleanTweets/"

dict_list = {}
dict_words = {} 
for files in fileList:
    if ".txt" in files:
        print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
        dict_list[files] = {}
	with open(file_path + files,'r') as fp:
	    for line in fp:
	        for word in line.strip(" ").split(" "):
                    strippedWord=word.strip(" ").strip("\n")
		    if strippedWord  not in dict_words:
			dict_words[strippedWord] = 0
     		    if strippedWord in dict_list[files]:
		        dict_list[files][strippedWord] += 1
		    else:
			dict_list[files][strippedWord] = 1


for files in fileList:
    if ".txt" in files:
        #pri-nt "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
        
	with open(file_path + files,'r') as fp:
	    for line in fp:
	        for word in line.strip(" ").split(" "):
                    strippedWord=word.strip(" ").strip("\n")
		    dict_words[strippedWord] = tfidf(strippedWord, dict_list[files], dict_list)

#print dict_words

finalTfIdf=OrderedDict(sorted(dict_words.items(),key=lambda x:x[1], reverse=True))
finalList=finalTfIdf.keys()
final=finalList[:int(0.8*len(finalList))]
finalTfIdf_Eighty=OrderedDict()

i=0

for key, value in finalTfIdf.items():
    if i < 0.8*len(finalTfIdf):
        finalTfIdf_Eighty[key]=value
        i+=1






with open("/home/ankit081190/NLP/CSCI-544-Project/Model/OrignialTfIdf.txt","w") as fp:
    json.dump(finalTfIdf,fp,encoding="utf-8", indent=2)
    fp.close()


with open("/home/ankit081190/NLP/CSCI-544-Project/Model/tfIdf.txt","w") as fp:
    json.dump(finalTfIdf_Eighty,fp,encoding="utf-8", indent=2)
    fp.close()

	
