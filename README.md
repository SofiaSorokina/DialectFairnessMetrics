# DialectFairnessMetrics
Summarization Fairness Metrics measures the representation of specific dialects in a text

## Usage
Run this line of code in the terminal in the main folder

'''python
python3 DialectFairnessMetrics.py
'''

It will return the analysis of the data we have provided

'''bash
LSA Summary Organized 1
summary: 23
count: 23
from AA: 2 or 0.201% --> takes up 8.696% in the summary
from Hisp: 11 or 1.1% --> takes up 47.826% in the summary
from White: 10 or 1.0% --> takes up 43.478% in the summary
'''

First word in first line means which bot performed the summary.
Third word in first line means if the data the bot used was organised or randomised.
And number in the first line means which run from the dataset was used.

The second line shows how many tweets are in the summary.
The third line shows how many comparrisons the algorythm has found.
- if there is the count is a bigger number that means that in the summary there are short tweets that can be found in the bigger longer tweets

And lines 4 to 6 show how many tweets in the summary came from which dialect, as well as the percentage of those tweets compared to the dataset and compared to the summary. 

##Not polished explanation below
There are three datasets which contain tweets with dialects from African-American(AA), Hispanic(H), and White (WH). A summary of all those tweets is generated with a summarization bot and then the summary is evaluated on its representation of all three dialects. 

Folder "TwitterData" contains three different sets of the three dialects. Each run has an initial .csv file for each dialect from outside data source, a .txt file of those csv files, and a new txt files which contain all the lines from all three dialects and are distributed in order and randomly. 
 - You can run DataOrganizing.py to get all those files again, exept you'll need the initial .csv files
 
File SumyPythonCode.py and folder LSA-Text-Summarization-master are the extractive summarization bots. To run Sumy, just open and run it's python file. To run LAS, open the folder and run the summarization.py file. These bots will give you the summaries of all ordered and randomised tweets and store them in a corresponding to the bot's name folder for summaries. 

To see how the bot represented all three dialects in the summary, run Compare.py. It will give you the percentagies of representation of each dialect.  
