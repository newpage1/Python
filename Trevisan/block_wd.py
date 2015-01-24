# -*-coding: utf-8-*-
"""
block weak design to reduce the overlap
"""
__author__ = 'Owner'
from math import e, log, ceil
from weakdes import weakdesign
def compute_l(m,t):
    """
    :param m: the one-bit extractor number
    :param t: the one-bit extractor seed length
    :return:block number
    """
    up = float(log(m-2*e,2) - log(t-2*e,2))
    down = float(log(2*e,2)-log(2*e-1,2))
    l = ceil(up/down)
    count = int(max(1,l))
    return count

def compute_mi(m,t):
    """
    compute the each m_i under formula 4
    :return:each block length
    """
    count = compute_l(m,t)
    m_set = list()
    n_set = list()
    for i in range(count):
        n = (1-float(1/(2*e)))**i
        n_i = n*(float(m/(2*e))-1)
        n_set.append(n_i)
        if i == 0:
            m_i = int(ceil(sum(n_set)))
            m_set.append(m_i)
        else:
            m_i = int(ceil(sum(n_set)) - sum(m_set))
            m_set.append(m_i)
    m_l = m - sum(m_set)
    m_set.append(m_l)
    return m_set

def compute_d(m,t):
    """
    compute the total seed length
    """
    l = compute_l(m,t)
    return (l+1)*t**2

def block_wd(m,t):
    """
    concentrate the total matrix of (m*d)
    :return:the list of matrix
    """
    l = compute_l(m,t)
    m_set = compute_mi(m,t)
    matrix = list()
    for i in range(l+1):
        m_i = m_set[i]
        wd = weakdesign(m_i,t)
        s_mi = wd.create_s()
        length = len(s_mi)
        for j in range(length):
            for k in range(t):
                s_mi[j][k] = s_mi[j][k] + i*t*t
        matrix.append(s_mi)
    return matrix


'''
m = 1024
t = 16
l = compute_l(m,t)
matrix = block_wd(m,t)
m_set = compute_mi(m,t)
result = 0
for i in range(l+1):
    result = result + m_set[i]
    print m_set[i]
    print matrix[i]
print result
'''





