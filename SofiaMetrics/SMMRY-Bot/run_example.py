#
# By Sofia Sorokina, August 2021
#
from app import Smmry
import io

for x in range(1,4):
        for y in ["Order", "Random"]:
            #read the all tweets file and perform summarization
            i = str(x)

            text = io.open("TwitterData/run"+i+"/" +y+"AllTweets"+i+".txt", 'r', encoding='utf-8').read()
            smmry = Smmry(text, lang="english")
            endSum = smmry.summarize(length=20)
            print("========= Summary "+y+" "+i+" =========")
            print(endSum)
            print("========= End of summary "+y+" "+i+" =========\n")

            #create a new file for summary based on tweets to be stored in
            f= open("SMMRY-summaries/"+y+"Summary"+i+".txt","w")
            f.write(endSum)
            f.close
