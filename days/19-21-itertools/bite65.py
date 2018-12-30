from itertools import permutations
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perms=_get_permutations_draw(draw)
    words=[]
    for combos in perms:
        for combo in combos:
            if ''.join(combo).lower() in dictionary:
                words.append(''.join(combo).lower())
    return words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return [list(permutations(draw,i)) for i in range(2,len(draw)+1)]