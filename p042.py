#!/usr/bin/python
import euler
import math

def word_score(w):
    return sum(map(ord, w.upper())) - (ord('A')-1)*len(w)
        
def is_trinum(n):
    sn = int(math.floor(math.sqrt(n * 2)))
    return n == (sn * (sn+1))//2
    
def is_triword(w):
    return is_trinum(word_score(w))

triwords = filter(is_triword, euler.read_words('data/p042_words.txt'))
print(len(triwords))
