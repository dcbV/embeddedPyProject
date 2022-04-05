"""
File: main.py
Description: main file
"""

from embedded import *

if __name__ == '__main__':
    sampleInput = [0, 1, 3, 2]
    sampleOutput = [2, 2, 3]
    sequence = [1, 1, 1, 1, 0]

    print(sequence)

    a = compare_to_pattern_list(sampleInput)
    file = search_file_meet('./Test_search_file_meet_samples')
    output, permutation = coin_permutations(sequence)

    print(output)
    print(permutation)
