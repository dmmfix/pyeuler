#!/usr/bin/python
import euler
from operator import mul


LookingFor = [1, 10, 100, 1000, 10000, 100000, 1000000]

CurrDigit = 0
CurrN = 1
NextN = 10
DPer  = 1

def advance():
    global CurrDigit
    global CurrN
    global NextN
    global DPer
    if CurrN == NextN:
        NextN *= 10
        DPer  += 1
    CurrN += 1
    CurrDigit += DPer

Series = []
while LookingFor:
    if (CurrDigit + DPer) >= LookingFor[0]:
        digits = list(reversed(euler.digits(CurrN)))
        Series.append(digits[LookingFor[0] - CurrDigit - 1])
        LookingFor = LookingFor[1:]
    advance()

print(Series, reduce(mul, Series, 1))
