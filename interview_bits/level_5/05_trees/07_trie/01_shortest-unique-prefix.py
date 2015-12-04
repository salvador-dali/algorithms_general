# https://www.interviewbit.com/problems/shortest-unique-prefix/
def generateTrie(words):
    trie = {}
    for word in words:
        curr_level = trie
        for char in word:
            if char not in curr_level:
                curr_level[char] = [1, {}]
            else:
                curr_level[char][0] += 1

            curr_level = curr_level[char][1]

    return trie

def check_prefix(trie, word):
    curr_level, found_now = trie, ''
    for char in word:
        if curr_level[char][0] > 1:
            found_now += char
            curr_level = curr_level[char][1]
        else:
            found_now += char
            return found_now

def solution(arr):
    trie = generateTrie(arr)
    return [check_prefix(trie, i) for i in arr]