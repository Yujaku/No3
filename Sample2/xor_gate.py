# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:36:25 2017

@author: yujaku
"""
from and_gate import AND
from or_gate import OR
from nand_gate import NAND


def XOR(x1, x2):
    #コードここから
    
    #コードここまで

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))