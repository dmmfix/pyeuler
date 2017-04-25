#!/usr/bin/python
import euler
from operator import add

numwords = {}
numwords[ 1] = 'one'
numwords[ 2] = 'two'
numwords[ 3] = 'three'
numwords[ 4] = 'four'
numwords[ 5] = 'five'
numwords[ 6] = 'six'
numwords[ 7] = 'seven'
numwords[ 8] = 'eight'
numwords[ 9] = 'nine'
numwords[10] = 'ten'
numwords[11] = 'eleven'
numwords[12] = 'twelve'
numwords[13] = 'thirteen'
numwords[14] = 'fourteen'
numwords[15] = 'fifteen'
numwords[16] = 'sixteen'
numwords[17] = 'seventeen'
numwords[18] = 'eighteen'
numwords[19] = 'nineteen'
numwords[20] = 'twenty'
numwords[30] = 'thirty'
numwords[40] = 'forty'
numwords[50] = 'fifty'
numwords[60] = 'sixty'
numwords[70] = 'seventy'
numwords[80] = 'eighty'
numwords[90] = 'ninety'
numwords[1000] = 'onethousand'

def getword(n):
    if (not n in numwords):
        if (n >= 100):
            str = getword(n//100) + 'hundred'
            if (n % 100):
                str += 'and' + getword(n % 100)
            numwords[n] = str
        else:
            str = getword((n//10)*10)
            if (n % 10):
                str += '' + getword(n % 10)
            numwords[n] = str

    return numwords[n]

print(reduce(add, map(len, map(getword, range(1,1001))), 0))
