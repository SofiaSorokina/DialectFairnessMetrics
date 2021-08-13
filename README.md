# SummarizationFairnessMetrics
There are three datasets which contain tweets with dialects from African-American(AA), Hispanic(H), and White (WH). A summary of all those tweets is generated with a summarization bot and then the summary is evaluated on its representation of all three dialects. 

Folder "TwitterData" contains three different sets of the three dialects. Each run has an initial .csv file for each dialect from outside data source, a .txt file of those csv files, and a new txt files which contain all the lines from all three dialects and are distributed in order and randomly. 
 - You can run DataOrganizing.py to get all those files again, exept you'll need the initial .csv files
 
File SumyPythonCode.py and folder LSA-Text-Summarization-master are the extractive summarization bots. To run Sumy, just open and run it's python file. To run LAS, open the folder and run the summarization.py file. These bots will give you the summaries of all ordered and randomised tweets and store them in a corresponding to the bot's name folder for summaries. 

To see how the bot represented all three dialects in the summary, run Compare.py. It will give you the percentagies of representation of each dialect.  
