# -*-coding: utf-8-*-
"""
create the total seed string using the built-in random function
"""
__author__ = 'Owner'
from random import *
class ran_string:
    def __init__(self):
        pass

    def ran_choice(self,d):
        s = str()
        seq = ['0','1']
        for i in range(100000):
            l = choice(seq)
            s = s+l
        return s[-d:]

    def zero_occur(self,seq):
        length = len(seq)
        zero = 0
        for i in range(length):
            if seq[i] == '0':
                zero += 1
        rate = float(zero)/float(length)
        return rate


