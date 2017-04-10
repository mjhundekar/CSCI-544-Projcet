import os, re, string, codecs, sys
reload(sys)
sys.setdefaultencoding("utf-8")



def readStopWords(hindiStopWords, stopWordsFileName):
    #For Hindi Stop Words Removal
    with codecs.open("/home/ankit/NLP_Project/CSCI-544-Projcet/hindiST.txt", "r", "utf-8") as f:
        for line in f:
            hindiStopWords.append(line.decode("utf-8").strip("\n").strip())
    f.close()
    print hindiStopWords
    #End of loading Hindi Stop Words file
    

def filter_list(full_list):
    s = set(hindiStopWords)
    return (x for x in full_list if x not in s)
#End Stop Words removal




def readSingleFile(fileName, fileOutName) :
#Start with a single file
    print fileName, fileOutName
    with codecs.open(fileName, 'r', 'utf-8') as f:
        rawDataList=f.read().replace(" :::: \n"," ::::: ").replace("\n","").replace(" ::::: "," :::: \n").split("\n")
        #print "rawDataList=",rawDataList," End Of rawDataList"
    f.close();


    #Write down clean tweets for sentiment analysis
    with codecs.open(fileOutName, 'w', 'utf-8') as f:
        for line in rawDataList:
            #print line.split(" :::: ")
            if " :::: " in line:
                tweet=line.replace('#','').strip().decode("utf-8").split(" :::: ")[1]
                tweetCleaned=re.sub(r'#(\w+)|(http|https|ftp)://[a-zA-Z0-9\\./]+|@(\w+)', '', tweet,  flags=re.IGNORECASE)
                tweetCleaned = re.sub('[%s]' % re.escape(string.punctuation), '', tweetCleaned).strip()
                d=[]
                d=tweetCleaned.decode("utf-8").split(' ')
                features=list(filter_list(d))
                f.write(" ".join(features)+"\n")
    f.close()



#main
hindiStopWords=[]
stopWordsFileName="/home/ankit/NLP_Project/CSCI-544-Projcet/hindiST.txt"
readStopWords(hindiStopWords, stopWordsFileName)

inFilePath="/home/ankit/NLP_Project/NLPProject/"
outFilePath="/home/ankit/NLP_Project/NLPProject/CleanTweets/"

fileList=os.listdir("/home/ankit/NLP_Project/NLPProject/")

for files in fileList:
    if ".txt" in files:
        #print "~~~~~~~~~~~~~filename~~~~~~~~~~~~~~",files
        readSingleFile(inFilePath+files, outFilePath+files)    
#fileName='/home/ankit/NLP_Project/NLPProject/2017-04-09-10-41-28.txt'

