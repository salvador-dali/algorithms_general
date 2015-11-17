# https://www.interviewbit.com/problems/majority-element/
def majority_element(arr):
    counter, possible_element = 0, None
    for i in arr:
        if counter == 0:
            possible_element, counter = i, 1
        elif i == possible_element:
            counter += 1
        else:
            counter -= 1

    return possible_element


from collections import defaultdict
def majority_element_general(arr, k=1):
    counter, i = defaultdict(int), 0
    while len(counter) < k and i < len(arr):
        counter[arr[i]] += 1
        i += 1

    for i in arr[i:]:
        if i in counter:
            counter[i] += 1
        elif len(counter) < k:
            counter[i] = 1
        else:
            fields_to_remove = []
            for el in counter:
                if counter[el] > 1:
                    counter[el] -= 1
                else:
                    fields_to_remove.append(el)
            for el in fields_to_remove:
                del counter[el]

    potential_elements = counter.keys()
    # might want to check that they are really frequent.
    return potential_elements

print majority_element_general([1, 2, 3, 1, 1, 2, 2, 4], 3)

