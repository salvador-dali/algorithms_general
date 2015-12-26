def find_last(graph, verts):
    queue = [(v, 0) for v in verts]
    visited = set(verts)

    while queue:
        last_vert = queue.pop(0)
        for adjacent in graph[last_vert[0]]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((adjacent, last_vert[1] + 1))

    return last_vert


graph = {
    1: [2],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
}

u = find_last(graph, [1])
v = find_last(graph, [u[0]])
x = find_last(graph, [u[0], v[0]])
print((x[1] + 1) / 2)