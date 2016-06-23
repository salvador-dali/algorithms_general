super_set = set()

def generate(x, y, used, line):
    if used[y][x]:
        if len(line) == 2 * len(m[0]):
            super_set.add(line)
        return
    new_line = line + m[y][x]
    new_used = [used[0][:], used[1][:]]
    new_used[y][x] = 1

    if x == 0:
        generate(x + 1, y, new_used, new_line)
        if y == 0:
            generate(x, y + 1, new_used, new_line)
        else:
            generate(x, y - 1, new_used, new_line)
    elif x == len(used[0]) - 1:
        generate(x - 1, y, new_used, new_line)
        if y == 0:
            generate(x, y + 1, new_used, new_line)
        else:
            generate(x, y - 1, new_used, new_line)
    elif y == 0:
        generate(x - 1, y, new_used, new_line)
        generate(x + 1, y, new_used, new_line)
        if (used[0][x - 1] and used[1][x - 1]) or (used[0][x + 1] and used[1][x + 1]):
            generate(x, y + 1, new_used, new_line)
    else:
        generate(x - 1, y, new_used, new_line)
        generate(x + 1, y, new_used, new_line)
        if (used[0][x - 1] and used[1][x - 1]) or (used[0][x + 1] and used[1][x + 1]):
            generate(x, y - 1, new_used, new_line)

def find_all(m):
    if len(m[0]) == 1:
        super_set.add(m[0][0] + m[1][0])
        super_set.add(m[1][0] + m[0][0])
        return
    used = [
        [0] * len(m[0]),
        [0] * len(m[0])
    ]

    for i in xrange(len(m[0])):
        generate(i, 0, used, '')
        generate(i, 1, used, '')

from datetime import datetime
startTime = datetime.now()

m = [
    'accdegeflixhazzzefxasdl4rfajn34azll4cfsajoimmasofjuagugnlsjdfhua',
    'clefsizlqhbbtuzqeuasf132rfsva3fgaadfs0lfasfahsiufbinladsnfbauiut'
]
find_all(m)
print len(super_set)

print datetime.now() - startTime
