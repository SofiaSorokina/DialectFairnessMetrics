# DialectFairnessMetrics
Summarization Fairness Metrics measures the representation of specific dialects in a summary

## Usage
Please run this line of code in the terminal 
``` python 
python3 DialectFairnessMetrics.py
```
It will return the analysis of the data we have provided
``` text
LSA Summary Organized 1
summary: 23
count: 23
from AA: 2 or 0.201% --> takes up 8.696% in the summary
from Hisp: 11 or 1.1% --> takes up 47.826% in the summary
from White: 10 or 1.0% --> takes up 43.478% in the summary

...
```
- First word in first line means which bot performed the summary. 
- Third word in first line means if the data the bot used was organised or randomised.
- Number in the first line means which run from the dataset was used.
- The second line shows how many tweets are in the summary.
- The third line shows how many comparrisons the algorythm has found.
	- if there is a count that is a bigger than the number of tweets in a summary that means in the summary there are shorter tweets ("lol", "XD", "Here") that can be found in the bigger longer tweets of the dataset
- And lines 4 to 6 show how many tweets in the summary came from which dialect, as well as the percentage of those tweets compared to the dataset and compared to the summary. 

## Data Files
Folder [TwitterData](https://github.com/SofiaSorokina/DialectFairnessMetrics/tree/main/TwitterData) contains three different runs which contain tweets with dialects from African-American(AAE), Hispanic(HAE), and White(AE) demographics. Each run has an initial .csv file for each dialect from outside data source, a .txt file of those csv files, and a new txt files which contain all the lines from all three dialects and are distributed either in order or randomly. 
 - You can run ```python3 DataOrganizing.py``` to get all those files again, exept you'll need the initial .csv files

## Summarization Bots
There are currently three different summarization bots which perform summarization on the tweets from the data set.
- [LSA-Bot](https://github.com/SofiaSorokina/DialectFairnessMetrics/tree/main/LSA-Bot) 
	- follow the steps of the README file in that folder if you don't have the required libraries installed
	- run ```python3 summarization.py```
- [SMMRY-bot](https://github.com/SofiaSorokina/DialectFairnessMetrics/tree/main/SMMRY-Bot)
	- follow the steps of the README file in that folder if you don't have the required libraries installed
	- run ```python3 run_example.py```
- [SUMY-Bot](https://github.com/SofiaSorokina/DialectFairnessMetrics/tree/main/SUMY-Bot)
	- follow the steps of the README file in that folder if you don't have the required libraries installed
	- run ```python3 SUMY-Bot.py```

These bots will give you the summaries of all ordered and randomised tweets and store them in a corresponding to the bot's name folder for summaries. 
