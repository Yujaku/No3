# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:36:25 2017

@author: 
"""
def AND(x1, x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp=w1*x1+w2*x2
    if tmp <= theta:
        return 0
    else:
        return 1
    
def NAND(x1,x2):
    #　ここからコード
    
        
    #ここまで


def　OR(x1,x2):
    #ここからコード
    
    
    #ここまで

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
