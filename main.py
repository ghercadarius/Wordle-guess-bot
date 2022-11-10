import math
import itertools
import pickle
import os
from collections import defaultdict
from scipy.stats import entropy


def pattern(guess, word):  #1 = galben, 2 = verde, 0 = gri -> match intre doua cuvinte
    patt = [2,2,2,2,2]
    for i in range(len(word)):
        x = guess[i]
        if x != word[i]:
            if x in word:
                patt[i] = 1
            else:
                patt[i] = 0
    return tuple(patt)

def pattern_dict(wordl_dict):
    pt_dict = defaultdict(lambda: defaultdict(set))
    for x in wordl_dict:
        for y in wordl_dict:
            ptn = pattern(x,y)
            pt_dict[x][ptn].add(y)
    return dict(pt_dict)

def get_possible_words(guess, ret_patt, words):
    pos_word = words
    for i in range(1,6):
        if ret_patt[i] == 0:
            for x in pos_word:
                if guess[i] in x:
                    pos_word.remove(x)
        if ret_patt[i] == 1:
            for x in pos_word:
                if guess[i] not in x:
                    pos_word.remove(x)
        if ret_patt[i] == 2:
            for x in pos_word:
                if x[i] != guess[i]:
                    pos_word.remove(x)
    return


def intersect(words):
    return


def entropie(words, possible_words, all_patterns, dict):
    entropies = {}
    for word in words:
        cnt = []
        for pat in all_patterns:
            match_list = dict[word][pat]
            cnt.append(len(match_list))
        entropies[word] = entropy(cnt)
    return entropies



def main():
    s = input("s=")
    all_pat = list(itertools.product([0,1,2], repeat=5))
    [print(i) for i in all_pat]
    f = open("cuvinte_wordle.txt", "r")
    L = []
    for x in f:
        x = x.strip()
        L.append(x)
    f.close()
    print(f"Loaded {len(L)} words")
    all_dict = {}
    if 'pattern_dict.p' in os.listdir('.'):
        all_dict = pickle.load(open('pattern_dict.p', 'rb'))
    else:
        all_dict = pattern_dict(L)
        pickle.dump(all_dict, open('pattern_dict.p', 'wb+'))
    entr = entropie(L, [], all_pat, all_dict)
    entropii_sortate = max(entr.items(), key = lambda x: x[1])
    print(entropii_sortate[0])

if __name__ == '__main__':
    main()

