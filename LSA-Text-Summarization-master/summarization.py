from lsa_summarizer import LsaSummarizer
import nltk
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

for x in range(1,4):
    for y in ["Order", "Random"]:
        from nltk.corpus import stopwords

        #read the all tweets file and perform summarization
        i = str(x)
        source_file = "TwitterData/run"+i+"/" +y+"AllTweets"+i+".txt"
        with open(source_file, "r", encoding='utf-8') as file:
            text = file.readlines()

        summarizer = LsaSummarizer()
        stopwords = stopwords.words('english')
        summarizer.stop_words = stopwords
        summary = summarizer(text[0], 10)

        #create a new file for summary based on tweets to be stored in
        f = open("LSA-summaries/"+y+"Summary"+i+".txt","w")
        endSum = " ".join(summary)
        f.write(endSum)

        #print("====== Original text "+i+" =====")
        #print(text)
        #print("====== End of original text "+i+" =====\n")

        print("========= Summary "+y+" "+i+" =========")
        print(endSum)
        print("========= End of summary "+y+" "+i+" =========\n")
