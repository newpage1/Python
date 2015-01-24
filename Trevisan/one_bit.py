# -*-coding: utf-8-*-
__author__ = 'Owner'
from math import log,ceil
class rsh_extractor:
    def __init__(self,n,e):
        """
        :param n: the input length
        :param e: the error percent
        """
        self.n = n
        self.e = e

    def compute_l(self):
        l = log(self.n,2) + 2*log(int(2/self.e),2)
        result = ceil(l)
        return result.__int__()

    def compute_s(self):
        l = self.compute_l()
        s = ceil(self.n/float(l))
        return s.__int__()

s = rsh_extractor(10,0.02)
print s.compute_l()
print s.compute_s()
