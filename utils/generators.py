import pandas as pd
import string
from .degraders import *

'''
Create a dataframe for this Syntax Degradation Analysis (SDA).
It will contain all results from the various stages of syntax degradation.
As a list of strings, the first string is the initial familiar phrase,
while the last string is the lorem-giberish version.
The Text Set is used to generate LLM embeddings, followed by various analyses.
'''

def create_text_set_df(initial_text, intensity=1, mode='default'):
    """
    Create a string list of syntactically degraded versions of the input text.
    The first string is the initial string, usually a familar phrase.
    The last string has the same number of words by are gibberish 'lorem' words.

    Modes:
        'default' - Applies a set of predefined syntax degraders one at a time.
        'lorem_by_word' - Replaces each word (one at a time) with lorem noise while keeping other words unchanged.

    Parameters:
        initial_text (str): the base sentence
        intensity (int): how many times to apply each degrader in 'default' mode
        mode (str): which degradation scheme to use ('default' or 'lorem_by_word')

    Returns:
        List[str]: sequence of degraded text samples
    """
    degraders = [
        lambda t: degrade_random_word(t, letter_swap),
        lambda t: degrade_random_word(t, letter_insert),
        lambda t: degrade_random_word(t, letter_drop),
        lambda t: degrade_random_word(t, letter_duplicate),
        word_drop,
        word_swap,
        word_reorder,
    ]

    initial_text = initial_text.translate(str.maketrans('', '', string.punctuation))
    degraded = [initial_text]

    if mode == 'default':
        for func in degraders:
            current = initial_text
            # repeat for intensity times
            for _ in range(intensity):
                current = func(current)
            degraded.append(current)

    elif mode == 'lorem_by_word':
        words = initial_text.split()
        for i in range(len(words)):
            modified = words[:]
            modified[i] = phrase_lorem(words[i])
            degraded.append(' '.join(modified))

    degraded.append(phrase_lorem(initial_text))

    sda_df = pd.DataFrame({'initial_text': [initial_text] * len(degraded)})
    sda_df['degraded_text'] = degraded

    return sda_df

