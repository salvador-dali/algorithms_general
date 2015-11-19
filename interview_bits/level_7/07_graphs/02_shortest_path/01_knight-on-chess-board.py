# https://www.interviewbit.com/problems/knight-on-chess-board/
def knigh(N, M, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    frontier, seen, steps = [(x1, y1)], {(x1, y1)}, 0
    while frontier:
        steps, next_frontier = steps + 1, []
        for x, y in frontier:
            possible = [(x + 1, y + 2), (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2), (x + 2, y + 1), (x - 2, y + 1), (x + 2, y - 1), (x - 2, y - 1)]
            for x_p, y_p in possible:
                if 0 < x_p <= N and 0 < y_p <= M and (x_p, y_p) not in seen:
                    if x_p == x2 and y_p == y2:
                        return steps
                    seen.add((x_p, y_p))
                    next_frontier.append((x_p, y_p))

        frontier = next_frontier

    return -1

print knigh(10, 9, 2, 2, 8, 9)
