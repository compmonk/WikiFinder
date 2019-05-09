import string

import nltk
from nltk.corpus import stopwords


def get_keywords(text):
    """
    Get the keyword from the text after cleaning it
    :param text: The text string to extract keywords from
    :return: List of keywords
    """
    text.rstrip()

    """
    Remove stop words and punctuation
    """
    stop_words = stopwords.words('english') + list(string.punctuation)
    text = ' '.join([
        word for word in text.split()
        if word.lower() not in stop_words
    ])

    tokens = nltk.word_tokenize(text)
    return tokens
