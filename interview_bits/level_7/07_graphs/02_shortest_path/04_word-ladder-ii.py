# https://www.interviewbit.com/problems/word-ladder-ii/
from collections import defaultdict

def similar_words(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [''.join([word[:i], letter, word[i + 1:]]) for letter in alphabet for i in xrange(len(word))]

def find_all(start, prevs, end):
    res = []
    def recursive_search(start, arr):
        last = arr[-1]
        if last == start:
            res.append(arr[::-1])
            return

        for prev in prevs[last]:
            recursive_search(start, arr[::] + [prev])

    recursive_search(start, [end])
    res.sort()
    return res

def find_transformation(start, end, words):
    if start == end:
        return [[start]]

    frontier, steps, seen, words, found, prevs = [start], 1, {start}, set(words), False, defaultdict(list)
    while frontier:
        next_frontier, steps = [], steps + 1
        for word in frontier:
            for new_word in similar_words(word):
                if new_word == end:
                    prevs[new_word].append(word)
                    found = True
                elif new_word in words and new_word not in seen:
                    prevs[new_word].append(word)
                    seen.add(new_word)
                    next_frontier.append(new_word)

        if found:
            break

        frontier = next_frontier

    if not found:
        return []

    return find_all(start, prevs, end)


# =====================

from collections import deque
def find_transformation2(start, end, dictV):
    dictV = set(dictV)
    dictV.add(end)
    queue = deque([(start, 1, [start])])
    visited = set()
    min_length = float('inf')
    ladders = []
    while queue:
        word, length, ladder = queue.popleft()
        visited.add(word)
        if word == end:
            if length == min_length:
                ladders.append(ladder)
            elif length < min_length:
                min_length = length
                ladders = [ladder]
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictV and new_word not in visited:
                    queue.append((new_word, length+1, ladder+[new_word]))
    return ladders
