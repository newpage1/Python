# -*-coding: utf-8-*-
"""
weak design when t = 2^x
"""
__author__ = 'Owner'
from math import log, ceil
class weakdesign:
    def __init__(self,m,t):
        """
        :param m: output length(one-bit extractor number)
        :param t: one-bit extractor seed length
        """
        self.m = m
        self.t = t

    def compute_c(self):
        """
        :return: poly coeff numbers
        """
        log_m = float(log(self.m,2))
        log_t = float(log(self.t,2))
        c = ceil(log_m/log_t-1) #
        return int(c)

    def compute_alf(self):
        """
        compute the poly coeff
        :return:poly coeff matrix
        """
        poly = []
        alf = []
        c = self.compute_c()
        for i in range(1,self.m+1):
            for j in range(0,c+1):
                acc = ((i-1)/(self.t**j))%self.t
                alf.append(acc)
            poly.append(alf)
            alf = []
        return poly

    def compute_poly(self,x,n):
        """
        :param x: x belongs to GF(t)
        :param n: the NO.n poly coeff
        :return:  the No.n poly value under x
        """
        c = self.compute_c()
        p_x = 0
        alf = self.compute_alf()
        for i in range(0,c+1):
            p_x = p_x + alf[n-1][i]*(x**i)
        p_x = p_x % self.t #mod t
        return p_x

    def create_sidict(self):
        """
        :return: return the poly value dict
        """
        s = list()
        s_i = dict()
        for i in range(1,self.m+1):
            for j in range(self.t):
                s_i[j] = self.compute_poly(j,i)
            s.append(s_i)
            s_i = {}
        return s

    def create_s(self):
        """
        :return:the substring index set
        """
        s_dict = self.create_sidict()
        s = list()
        result = list()
        for i in range(self.m):
            for j in range(self.t):
                co = s_dict[i][j]*self.t+j
                s.append(co)
            result.append(s)
            s = list()
        return result

    def compute_d(self):
        return self.t**2

'''
m = 256
t = 16
s = weakdesign(m,t)
res = s.create_s()
for i in range(m):
    print res[i]
'''









