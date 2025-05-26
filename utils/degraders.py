import random
import string

# Define the letter-level degrader functions for: swap, insert, drop, duplicate

def letter_swap(word):
    """Swap two adjacent letters in a word at a random position."""
    if len(word) < 2:
        return word
    i = random.randint(0, len(word) - 2)
    return word[:i] + word[i+1] + word[i] + word[i+2:]

def letter_insert(word):
    """Insert a random letter into a word at a random position."""
    i = random.randint(0, len(word))
    return word[:i] + random.choice(string.ascii_lowercase) + word[i:]

def letter_drop(word):
    """Remove a single letter from a word at a random position."""
    if len(word) < 2:
        return word
    i = random.randint(0, len(word) - 1)
    return word[:i] + word[i+1:]

def letter_duplicate(word):
    """Duplicate a letter at a random position in the word."""
    if len(word) < 1:
        return word
    i = random.randint(0, len(word) - 1)
    return word[:i] + word[i] + word[i] + word[i+1:]

# Define the Word-level Degrader functions: drop, swap, and reorder.

def word_drop(text):
    """Remove a random word from the sentence."""
    words = text.split()
    if len(words) > 1:
        del words[random.randint(0, len(words) - 1)]
    return ' '.join(words)

def word_swap(text):
    """Swap two random adjacent words in the sentence."""
    words = text.split()
    if len(words) < 2:
        return text
    i = random.randint(0, len(words) - 2)
    words[i], words[i+1] = words[i+1], words[i]
    return ' '.join(words)

def word_reorder(text):
    """Randomly shuffle the word order of a sentence."""
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

# Utility to apply word-level degradation

def degrade_random_word(text, letter_func):
    """Apply a letter-level function to a single random word in the text."""
    words = text.split()
    if words:
        i = random.randint(0, len(words) - 1)
        words[i] = letter_func(words[i])
    return ' '.join(words)

# Define a Phrase-level degrader function generating a giberish sentence,
# used as the last string in the text set.

def phrase_lorem(text):
    """Generate random lowercase letters preserving word-spacing of input text."""
    return ''.join(c if c == ' ' else random.choice(string.ascii_lowercase) for c in text)
