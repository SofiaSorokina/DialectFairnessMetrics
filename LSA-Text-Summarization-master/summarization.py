from lsa_summarizer import LsaSummarizer
import nltk
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

for x in range(1,4):
    from nltk.corpus import stopwords

    #read the all organized tweets file and perform summarization
    i = str(x)
    source_file = "TwitterData/run"+i+"/OrderAllTweets"+i+".txt"
    with open(source_file, "r", encoding='utf-8') as file:
        text = file.readlines()

    summarizer = LsaSummarizer()
    stopwords = stopwords.words('english')
    summarizer.stop_words = stopwords
    summary = summarizer(text[0], 10)

    #create a new file for summary based on organized tweets to be stored in
    f = open("LSA-summary/OrderSummary"+i+".txt","w")
    endSum = " ".join(summary)
    f.write(endSum)

    #print("====== Original text "+i+" =====")
    #print(text)
    #print("====== End of original text "+i+" =====\n")

    print("========= Summary "+i+" =========")
    print(endSum)
    print("========= End of summary "+i+" =========\n")

#Devides the summary sentences and puts them in a list format
def summaryTokens (filename):
    my_file = open("LSA-summary/" + filename, "r")
    content = my_file.read()
    content_list = content.split(". ")
    my_file.close()
    f = open("LSA-summary/Token" + filename,"w")
    f.write(str(content_list))

summaryTokens ("OrderSummary1.txt")
summaryTokens ("OrderSummary2.txt")
summaryTokens ("OrderSummary3.txt")