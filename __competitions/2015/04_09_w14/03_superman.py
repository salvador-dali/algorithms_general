def superman(data, I):
    """
    https://www.hackerrank.com/contests/w14/challenges/superman-celebrates-diwali
    =====
    During the first attempt I looked at the path as a graph which is constructed in the following way:

    Each node is a B_<building number>_<floor> and the value is the number of people at this floor.
    After this the edges are constructed. The edges from the same building to the next floor are obvious.
    But we also have edges from each floor (F_) on building A to the biggest floor on each other building
    that is <= then F_ - i. Also lets add the node 'start' which points to all top floors and 'end' which
    connects to all lowest floors.

    After the graph is constructed (note that the graph is DAG) we need to find the longest path from start
    to end. This is done in O(V + E) in DAG. To do this just find the Topological sorting and then use Khan
    algorithm. Everything looked nice, BUT apparently in practice in was not so good.

    =====
    So I started to think in a different way using Dynamic Programming approach.

    Firstly sort all buildings in the descending order based on the floors. So we end up with something like
    (floor, buildingID, number of people): (**1)

    We store information about: (**2)
    - previous number of collected people on each floor (array where each position is prev number for this building)
    - previous maximum of the number of people in the building
    - which floor had the maximum number of people
    - hash of the maximum people on each floor

    We are ready to descend from the building (populating all the stored information) (**3)
    One caveat can be (**4) that when we descend down some of the floors can be empty. So when we
    will access our hash of the maximum people we may access floor which is not populated
    for this reason populate information about missing floors with data maximum previous floor

    Now on each floor we calculate from which floor we might have jumped from (**5)\
    and use following DP formula:
    prevInBuilding[currentBuilding] = valueInBuilding + max(prevInBuilding[currentBuilding], maximumOnFloor.get(jumpFloor, 0))
    and also cache some values.

    At the end we have the maximum value on the last floor

    :arg    [{1: 3, 10: 1, 4: 1}, {8: 2, 9: 2, 3: 1, 5: 1, 7: 2}, {9: 1, 3: 1, 4: 1, 5: 1, 6: 1}]
            array of buildings which each building has {floor: number_of_people}
    :return
    """
    l = len(data)
    if not l:
        return 0

    # (**1)
    descFloors = [(floor, buildingID, data[buildingID][floor]) for buildingID in xrange(l) for floor in data[buildingID]]
    descFloors.sort(key=lambda x: x[0], reverse=True)

    # (**2)
    prevInBuilding, maxPrevInBuilding, prevFloor = [0] * l, 0, descFloors[0][0]
    maximumOnFloor = {prevFloor: 0}

    # (**3)
    for currentFloor, currentBuilding, valueInBuilding in descFloors:
        # (**4)
        if prevFloor - currentFloor > 1:
            for _ in xrange(currentFloor + 1, prevFloor):
                maximumOnFloor[_] = maximumOnFloor[prevFloor]

        # (**5)
        jumpFloor = currentFloor + I
        prevInBuilding[currentBuilding] = valueInBuilding + max(prevInBuilding[currentBuilding], maximumOnFloor.get(jumpFloor, 0))
        maxPrevInBuilding = max(prevInBuilding[currentBuilding], maxPrevInBuilding)
        maximumOnFloor[currentFloor] = maxPrevInBuilding
        prevFloor = currentFloor

    return maximumOnFloor[currentFloor]

from collections import Counter
data = []
N, H, I = map(int, raw_input().split())
for i in xrange(N):
    line = dict(Counter(list(map(int, raw_input().split()))[1:]))
    if line:
        data.append(line)

print superman(data, I)