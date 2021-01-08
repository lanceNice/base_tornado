# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 16:00
# @Author  : lance
# @File    : learn.py
# @Software: PyCharm


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return 'FrenchDeck-0'

def test():
    """dsdsd"""

print(test.__doc__)
