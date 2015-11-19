# https://www.interviewbit.com/problems/word-ladder-i/
def similar_words(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [''.join([word[:i], letter, word[i + 1:]]) for letter in alphabet for i in xrange(len(word))]

def find_transformation(start, end, words):
    if start == end:
        return 1
    frontier, steps, seen, words = [start], 1, {start}, set(words)
    while frontier:
        steps, next_frontier = steps + 1, []
        for word in frontier:
            for new_word in similar_words(word):
                if new_word == end:
                    return steps
                if new_word in words and new_word not in seen:
                    seen.add(new_word)
                    next_frontier.append(new_word)

        frontier = next_frontier
    return 0

print find_transformation('hit', 'cog', {"hot","dot","dog","lot","log"})
