# CptS 355 - Fall 2019 Assignment 3
# Nick Lamos
# worked with Tyler Cleveland and Puthypor Sengkeo

debugging = True


def debug(*s):
    if debugging:
        print(*s)

# 1
# a)
def sprintLog(sprint):
    retSprint = {}
    for key1, value1 in sprint.items():
        for key2, value2 in value1.items():
            if key2 in retSprint:
                retSprint[key2][key1] = value2
            else:
                retSprint[key2] = {key1: value2}
    return retSprint
# b)
def addSprints(sprint1, sprint2):
    retSprint = {}
    for key1 in sprint1:
        retSprint[key1] = sprint1[key1]
    for key2 in sprint2:
        if key2 in retSprint:
            value2 = sprint2[key2]
            for key3 in value2:
                if key3 in retSprint[key2]:
                    retSprint[key2][key3] += sprint2[key2][key3]
                else:
                    retSprint[key2][key3] = sprint2[key2][key3]
        else:
            retSprint[key2] = sprint2[key2]
    return retSprint
# c)
def addNLogs(logList):
    retList = []
    retDict1 = {}
    retDict2 = {}
    for sprint in logList:
        retList.append(sprintLog(sprint))
    for item in range(len(retList)):
        retDict2 = addSprints(retList[item], retList[item - 1])
        retDict1.update(retDict2)
    return retDict1

# 2
# a)
def lookupVal(L, k):
    for item in range(len(L)):
        for key, value in L[item].items():
            if key == k:
                retValue = value
    return retValue
# b)
def lookupVal2(tL, k):
    for item1 in tL:
        for key1, value1 in item1[1].items():
            if key1 == k:
                for item2 in tL[item1[0]]:
                    for key2, value2 in tL[item1[0]][1].items():
                        if key2 == k:
                            retValue = value2
    return retValue

# 3 Worked with Puthypor Sengkeo
def unzip(L):
    list1 = list(map(lambda xy: xy[0], L))
    list2 = list(map(lambda xy: xy[1], L))
    list3 = list(map(lambda xy: xy[2], L))
    return (list1, list2, list3)

# 4 Worked with Tyler Cleveland
def numPaths(m, n, blocks):
    if m == 1 and n == 1:
        return 1

    blocksAbove = 0
    blocksLeft = 0
    if (m - 1, n) not in blocks and m - 1 > 0 and n > 0:
        blocksAbove = numPaths(m - 1, n, blocks)

    if (m, n - 1) not in blocks and m > 0 and n - 1 > 0:
        blocksLeft = numPaths(m, n - 1, blocks)

    return blocksAbove + blocksLeft

# 5
class iterFile():
    def __init__(self, filename):
        self.file = open(filename)
        self.current = []

    def __next__(self):
        try:
            for line in self.file.read(1):
                for ch in line:
                    while ch != (" " or "\n"):
                        word = word + ch
            return word
        except:
            raise StopIteration

    def __iter__(self):
        return self