from datetime import datetime, date


def analyse(d1, m1, y1, d2, m2, y2):
    total = 0
    for i in xrange(y1 * 12 + m1 - 1, y2 * 12 + m2):
        year = i / 12
        month = i % 12 + 1
        if date(year, month, 13).weekday() == 4:
            total += 1

    if d2 < 13:
        total -= int(date(y2, m2, 13).weekday() == 4)

    if d1 > 13:
        total -= int(date(y1, m1, 13).weekday() == 4)

    return total


for i in xrange(input()):
    d1, m1, y1, d2, m2, y2 = map(int, raw_input().split())
    print analyse(d1, m1, y1, d2, m2, y2)