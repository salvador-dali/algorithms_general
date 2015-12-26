import sys

max_tags = input()
    
elements, result = [], []
for i in sys.stdin:
    destination, tags = i.rstrip().split(':')
    tags = set(tags.split(','))
    if len(tags) >= max_tags:
        elements.append((destination, tags))

def groupOfTwo(elements):
    res = []
    for i in xrange(len(elements)):
        d1, t1 = elements[i][0], elements[i][1]
        for j in xrange(i + 1, len(elements)):
            d2, t2 = elements[j][0], elements[j][1]
            intersect = t1.intersection(t2)
            if len(intersect) >= max_tags:
                res.append((set([d1, d2]), intersect))
    return res

def expandItemset(itemset, elements):
    new_itemset = []
    new_set = set([])
    for items, tags1 in itemset:
        # print items, tags1, len(tags1)
        notFound = True
        for el, tags2 in elements:
            if el not in items:
                new_items = items.union([el])
                new_tags = tags1.intersection(tags2)
                if len(new_tags) == len(tags1):
                    notFound = False

                if len(new_tags) >= max_tags:
                    items_for_set = tuple(sorted(new_items))
                    if items_for_set not in new_set:
                        new_set.add(items_for_set)
                        new_itemset.append((new_items, new_tags))
                # print '   ', new_items
                # print '       ', len(new_tags)

        if notFound:
            result.append((items, tags1))

    return new_itemset

itemset = groupOfTwo(elements)
while len(itemset):
    itemset = expandItemset(itemset, elements)


new_res = []
for destinations, tags in result:
    new_res.append([len(tags), ','.join(sorted(list(destinations))) + ':' + ','.join(sorted(list(tags)))])


new_res.sort(key=lambda x: (-x[0], x[1]))

for i in new_res:
    print i[1]