InstituteForComputingInResearch
# LEXRANK
Lexrank is an unsupervised approach to text summarization based on graph-based centrality scoring of sentences. It strives for sentences to recommend other similar sentences to the reader; therefore, a sentence similar to many others will be a centrality. In other words, to get ranked highly and placed in a summary, a sentence must be similar to many sentences that are also similar to many others, instigating intuitive sense.
## INSTALLATION
use the package manager [pip](https://pypi.org/project/pip/) to install lexrank
```bash 
pip install lexrank
```
## PURPOSE
EVALUATING NLP SUMMARIZATION BIAS (DIALECT) IN TWITTER (AE (AMERICAN ENGLISH) & AAE (AFRICAN AMERICAN ENGLISH)) & HAE (HISPANIC AMERICAN ENGLISH)
## DESCRIPTION
### BACKGROUND
Natural language processing (NLP) is a beautiful subfield of computer science, linguistics, and artificial intelligence. Its focus on human and computer language interaction through manipulating and analyzing massive quantities of natural language data aims to understand contents like a regular human being, further advancing the daily lives of many with technology. With technology promptly progressing, it is typical that people overlook the withholdings that follow, especially dialect bias in summarization. Everybody's voice deserves to be heard, but when it comes to natural language processing, popular summarization methods such as lexrank disappoints.
### FEATURES
The suggested bias evaluation metric is simple and efficient- it calculates the percentage of the extracted tweets from each dialect that ends up in the summary through the following equation: (the number of tweets from AE or AAE or HAE dataset) divided by (total number of tweets in the summarization).
## STEPS
```python 
# run the following in the terminal
python3 code.py
# type the datasets you want to run out of ae, aae, and hae and press enter after typing each one
# type enter when you are done
# type in a sample size (has to be an integar)
```
you can edit input.txt to the file names and sample numbers you want
## ACKNOWLEDGEMENT
Thank you for running our code and feel free to contact us with suggestions!
## SUPPORT
Stuck? Feel free to contact us if you have run into any issues!
