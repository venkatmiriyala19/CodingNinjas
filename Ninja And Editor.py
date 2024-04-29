from os import *
from sys import *
from collections import *
from math import *

def editSentence(s):
    words=[]
    word=''
    for x in s:
        if x.isupper():
            if word:
                words.append(word.lower())
                word=x
                continue
            # word+=x
        word+=x
    words.append(word.lower())
    return ' '.join(words)
    # Write your code here.
    pass
