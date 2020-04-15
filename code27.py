#!/usr/bin/env python

from __future__ import print_function

#provide an odd value eg. 3,5,7,9.. etc
W = 19
M = (W + 1)/2
L = W - M - 1
R = W + M - 1
for i in range(W):
        for j in range(W):
                if( (i - j < M ) & (j - i < M ) &  (i + j > L) & (i + j < R)  ):
                        print( "*",  end=" ")
                else:
                        print (" ", end=" ")
        print("")
