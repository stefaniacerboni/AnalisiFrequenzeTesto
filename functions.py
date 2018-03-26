from __future__ import division
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


def letters_frequencies(f, letters):
    freq = [0] * 26
    for i in range(26):
        freq[i] = f.count(letters[i])
    # ax = plt.axes()
    # ax.set_xticklabels(letters)
    # pos = np.arange(len(letters))
    index = np.arange(26)
    plt.bar(index, freq)
    plt.xticks(index + 0.35, letters)
    plt.xlabel('Lettere')
    plt.ylabel('Frequenza')
    plt.show()


def block_distribution(q, f):
    dicts = {}
    i = 0
    while i < len(f)-q:
        block = ""
        for j in range(q):
            block = block+f[i+j]
        if block not in dicts:
            dicts[block] = 0
        dicts[block] = dicts[block]+1
        i+=q
    print("--- Empirical Distribution ---")
    for key in dicts:
        dicts[key] = dicts[key]/(len(f)//q)
        print(key + " : " + str(dicts[key]))
    return dicts


def block_index_of_coincidence(q, f):
    dicts = {}
    sum =0
    i=0
    a=(len(f)//q)
    while i < len(f)-q:
        block = ""
        for j in range(q):
            block = block+f[i+j]
        if block not in dicts:
            dicts[block] = 0
        dicts[block] = dicts[block]+1
        i+=q
    print("--- Index of Coincidence ---")
    for key in dicts:
        dicts[key] = (dicts[key]*(dicts[key]-1)) / ((a-1)*a)
        sum+=dicts[key]
    print('Ic : ' + str(sum))

def entropy(dicts):
    entropy = 0
    for key in dicts:
        entropy -= dicts[key] * math.log(dicts[key], 2)
    print("--- Entropy ---")
    print("ENTR : " + str(entropy))
