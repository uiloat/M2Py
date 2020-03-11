#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Syntax:
	Lia,Locb = ismember(a,B)

Description:
	Lia,Locb = ismember(a,B) Lia returns an array containing logical 1 (true) where the data in a is found in B.
	Elsewhere,	the array contains logical 0 (false). Locb contains the lowest index in B for each value in a that
	is a member of B. Values of -9999 indicate where A is not a member of B.
	-9999 = not exist

Example:
	a = np.array([5, 3, 4, 2])
	B = np.array([2, 4, 4, 4, 6, 8])

	Lia, Locb = ismember(a, B)
	print(Lia, Locb)

	# Lia: array([False, False,  True,  True])
	# Locb : [-9999, -9999, 1, 0]

Imitation MATLAB ismember: https://www.mathworks.com/help/matlab/ref/ismember.html
Mac 10.12.6 Anaconda 3 64bit, Python 3.7.0
@author: jiangtao
'''

import numpy as np


def ismember(a, B):
    # if len(B) == len(np.unique(B)):
    # 	index = [np.where(B == i)[0][0] for i in a]
    #
    # else:
    index = [np.where(B == i)[0] for i in a]
    for i, i_data in enumerate(index):
        if len(i_data) == 0:
            index[i] = -9999
        elif len(i_data) == 1:
            index[i] = i_data[0]
        elif len(i_data) > 1:
            index[i] = i_data[0]  # you can change [0] --> [1],[2]... to get the index of repeat elements.

    isin_logical = np.isin(a, B)
    Lia = isin_logical
    Locb = index

    return Lia, Locb
