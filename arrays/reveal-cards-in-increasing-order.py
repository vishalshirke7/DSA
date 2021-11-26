"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/
"""
import collections

def deckRevealedIncreasing(deck):
    N = len(deck)
    index = collections.deque(range(N))
    ans = [None] * N
    for card in sorted(deck):
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ans

def deckRevealedIncreasing(deck):
        d = collections.deque()
        for x in sorted(deck)[::-1]:
            d.rotate()
            d.appendleft(x)
        return list(d)


print('Output', deckRevealedIncreasing([17,13,11,2,3,5,7]))