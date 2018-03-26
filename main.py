import string
import functions
import math
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
values = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
          0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020,
          0.001]
dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
       'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
       'Z': 25}
def __main__():
    with open('MobyDick.txt') as inputfile:
        f = inputfile.read().upper().translate(None, string.punctuation).translate(None, " ").translate(None, "\n")
    q = 0
    while q < 1:
        q = int(raw_input("Please enter block length q >= 1 "))
    #q = 4
    dicts = functions.block_distribution(q, f)
    functions.entropy(dicts)
    functions.block_index_of_coincidence(q, f)
    #functions.letters_frequencies(f, letters)
    return 0


if __name__ == __main__():
    __main__()