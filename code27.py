#!/usr/bin/env python

from __future__ import print_function

for i in range(9):
	for j in range(9):
		if( (i - j < 5) & (j - i < 5 ) &  (i + j > 3) & (i + j < 13)  ):
			print( "#",  end=" ")
		else:
			print (" ", end=" ")
	print("")
