InstituteForComputingInResearch
# LEXRANK
Lexrank is an unsupervised text summarization method using graph-based centrality. This algorithm scores sentences so a sentence similar to many other sentences will become a centrality. Sentences with higher ranking will be placed in the summary.
## INSTALLATION
use the package manager [pip](https://pypi.org/project/pip/) to install lexrank
```bash 
pip install lexrank
```
## PURPOSE
Evaluating NLP summarization dialect bias in twitter datasets (AE (AMERICAN ENGLISH) & AAE (AFRICAN AMERICAN ENGLISH)) & HAE (HISPANIC AMERICAN ENGLISH)
## DESCRIPTION
### BACKGROUND
Natural language processing (NLP) is a subfield of computer science, linguistics, and AI. Its focus on human and computer language interaction through manipulating and analyzing massive quantities of natural language data aims to understand contents like a regular human. As AI rapidly evolves, considering its ethics becomes essential to building responsible systems.
### FEATURES
The suggested bias evaluation metric is simple and efficient. It calculates the percentage of the extracted tweets from each dialect that ends up in the summary through the following equation: (the number of tweets from AE or AAE or HAE dataset) divided by (total number of tweets in the summarization).
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
