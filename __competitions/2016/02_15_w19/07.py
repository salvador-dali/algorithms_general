data = [tuple(map(int, line.strip().replace("[", "").replace("]", "").split())) for line in open("data.txt")]
data.sort()
print data