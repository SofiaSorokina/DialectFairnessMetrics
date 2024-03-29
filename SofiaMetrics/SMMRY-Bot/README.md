# Running This Code
Firstly, download 'averaged_perceptron_tagger' from nltk
```python
import nltk
nltk.download('averaged_perceptron_tagger')
```
Then you can run it by typing
```python 
python3 run_example.py
```
# Requirements

* Python 3.x
* numpy
* NLTK

# Smmry
A Python text summarizer inspired by [Smmry](https://smmry.com) and this [tutorial](https://nlpforhackers.io/textrank-text-summarization/). It contains the following functions:
- **sent_tokenizer**: splits text into words per sentence
- **preprocess**: removes punctuation and removes stopwords
- **tag_pos**: part-of-speech tagger that selects adjectves (ADJ) and nouns(NN)
- **stem**: stems words in sentences
- **text_rank**: ranks sentences based on text rank algorithm
- **build_similarity_matrix**: creates a cosine similarity matrix based on tfidf vectors
- **summarize**: runs through all the steps above and generates a summary
