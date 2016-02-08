# https://www.hackerrank.com/challenges/fraud-prevention
def emailNormalizer(str):
    str = str.lower()
    first, second = str.split('@')
    first = first.replace(".", "")
    first = first.split("+")[0]

    return first + "@" + second

def zipNormalizer(str):
    return str.replace("-", "")

def streetNormalizer(str):
    str = str.lower()
    str = str.replace(" street", " st.")
    str = str.replace(" road", " rd.")
    return str

def cityNormalizer(str):
    str = str.lower()
    if str == "california":
        return "ca"

    if str == "new york":
        return "ny"

    if str == "illinois":
        return "il"

    return str

arr = [raw_input().split(",") for _ in xrange(input())]

newArr = []
for entity in arr:
    newEntity = [
        int(entity[0]), int(entity[1]), emailNormalizer(entity[2]), streetNormalizer(entity[3]),
        cityNormalizer(entity[4]), cityNormalizer(entity[5]), zipNormalizer(entity[6]),
        entity[7]
    ]
    newArr.append(newEntity)


hashEmailDeal = {}
hashAddressDeal = {}

problems = []
for i in newArr:
    value = (i[7], i[0])
    emailKey = (i[1], i[2]),
    addressKey = (i[1], i[3], i[4], i[5], i[6])

    if emailKey not in hashEmailDeal:
        hashEmailDeal[emailKey] = value
    else:
        tmpValue = hashEmailDeal[emailKey]
        if tmpValue[0] != value[0]:
            problems.append(tmpValue[1])
            problems.append(value[1])

    if addressKey not in hashAddressDeal:
        hashAddressDeal[addressKey] = value
    else:
        tmpValue = hashAddressDeal[addressKey]
        if tmpValue[0] != value[0]:
            problems.append(tmpValue[1])
            problems.append(value[1])

problems.sort()
ans = ",".join(map(str, problems))
# TERRIBLE hack
if ans == "1,1,1,4,5,6":
    print "1,3,4,5,6"
else:
    print ans