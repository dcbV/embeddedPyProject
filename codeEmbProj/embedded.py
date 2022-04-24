"""
File: embedded.py
Description: code related to the embedded element
"""

import os
from os.path import isfile, join

import pywintypes
import win32file


def compare_to_pattern_list(sample: list, pattern: list = []) -> int or None:
    """
    Returns the first repeating number of the sample vector in the pattern vector or, in other case, return None. If any
    list is empty, return None.

    :param sample: list of input values
    :param pattern: pattern list
    :return: first value repeated or None
    """

    # Input protection (type)
    assert isinstance(sample, list), "sample type is not list"
    assert isinstance(pattern, list), "pattern type is not list"

    result = set(sample).intersection(pattern)
    return next(iter(sorted(result)), None)


def search_file_meet(path: str, owner: int = 0, size: int = 14680, exec: bool = True) -> str or None:
    """
    Returns first file that meets file owner, size and executable mode

    :param path: path where to search for the file
    :param owner: identifier of the owner of the file to search (owner id 0 (admin))
    :param size: maximum file size to search (default: 14.680.064 B ~ 14680 kB)
    :param exec: file not executable (False) or executable (True)
    :return: name of the first file that meets requirements
    """

    if not os.path.exists(path):
        return None

    else:
        # Look for all files in the folder
        files = [f for f in os.listdir(path) if isfile(join(path, f))]

        if not files:
            return None

        else:
            # Iterates through the folder to the first file that meets conditions
            for file in files:
                filepath = path + '/' + file
                fileobj = os.stat(filepath)
                if fileobj.st_uid == owner and fileobj.st_size <= size:
                    try:
                        # If it has to be executable and it is, it returns the file, otherwise, it continues
                        if win32file.GetBinaryType(filepath) == exec:
                            return file
                    except pywintypes.error:
                        continue


def coin_permutations(sequence: list) -> list and int:
    """
    Returns quantity of permutations so that the sequence ends interspersed (0 tails and 1 heads)
    :param sequence: input sequence
    :return: number of permutations needed
    """

    tails = 0
    heads = 0

    # Input protection (type and not empty list and value not 0-tail or 1-head)
    assert isinstance(sequence, list), "sequence type is not list"
    assert set(sequence).issubset([0, 1]), "Values in sequence are not all heads and tails"

    for idx in range(len(sequence)):

        # Sets value to zero or one depending on position and fixed first position value
        modtails = idx % 2  # First position of the sequence to be compared to tails
        modheads = (idx + 1) % 2  # First position of the sequence to be compared to heads

        # Adds 1 if the position does not match the pattern (0 or 1)
        if sequence[idx] != modtails:
            tails = tails + 1
        elif sequence[idx] != modheads:
            heads = heads + 1

    # Modifies the sequence to make the minimum necessary permutations
    for idx in range(len(sequence)):
        sequence[idx] = (idx + (tails > heads)) % 2

    return sequence, min(tails, heads)
