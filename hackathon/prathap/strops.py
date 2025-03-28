#this is used to find the string span
def getspan(s, ss):
    index = s.find(ss) 

    if index == -1:  # Substring not found
        return None
    else:
        return (index, index + len(ss) - 1)
#this function used for the reverse the given string
def reverseWords(s):
    words= s.split()
    rev=words[::-1]
    return " ".join(rev)
#this function used for remove the punctuation of given string 
import string
def removePunctuation(s):
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

#this function used for the count the string
def countWords(s):
    word=s.split()
    return len(word)
#this is used for the  charecter map in the given string 
from collections import Counter
def charecterMap(s):
    return dict(Counter(s))
#this function is used to make the give string as title
def makeTitle(s):
    return s.title()
#this is used to normalize space inthe given string 
import re
def normalizeSpaces(s):
    return re.sub(r'\s+', ' ', s.strip())
#this is used to fransform the given string 
def transform(s):
    p= s.swapcase()
    return p[::-1]
#this is use to find the permutations
import itertools
def getPermutations(s):
    return [".join(p)for p in iteratools.permutations(s)"]