# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"
SENTENCES_COUNT = 5

if __name__ == "__main__":
    for x in range(1,4):
        for y in ["Order", "Random"]:
            #read the all tweets file and perform summarization
            i = str(x)

            parser = PlaintextParser.from_file("TwitterData/run"+i+"/" +y+"AllTweets"+i+".txt", Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)
            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)
            line = ""

            #create a new file for summary based on tweets to be stored in
            open("SUMY-summaries/"+y+"Summary"+i+".txt","w")
            print("========= Summary "+y+" "+i+" =========")
            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                print(sentence)
                line += (str(sentence) + ". ")
            print("========= End of summary "+y+" "+i+" =========\n")

            f= open("SUMY-summaries/"+y+"Summary"+i+".txt","a")
            f.write(line[:-1])