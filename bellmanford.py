"""
Bellman-ford shortest path algorithm.
"""

def bf(graph, weight, start):
    distance = {}
    pi = {}
    vCount = 0
    for vertex in graph:
        distance[vertex] = 10000
        pi[vertex] = 0
        vCount += 1
    distance[start] = 0
    for i in range(1, vCount-1):
        for vertex in weight:
            temp = list(vertex)
            u = temp[0]
            v = temp[1]
            if distance[v] > distance[u] + weight[vertex]:
                distance[v] = distance[u] + weight[vertex]
                pi[v] = u

    for vertex in weight:
        temp = list(vertex)
        u = temp[0]
        v = temp[1]
        if distance[v] > distance[u] + weight[vertex]:
            return False
    return True, distance, pi

def spath(distance, pi, node):
    key = node
    path = []
    print ("Shortest path to " + node + " is ")
    while pi[key] != 0:
        path.insert(0, pi[key])
        key = pi[key]
    for node in path:
        print("--> " + node)

graphA = {
    "S": ["B", "C"],
    "B": ["C","D","E"],
    "C": [],
    "D": ["B"],
    "E":["D"]
}

weightA = {
    "SB": -1,
    "SC": 4,
    "BC": 3,
    "BD": 2,
    "BE": 2,
    "DB": 1,
    "ED": -3
}

boo, d, p = bf(graphA, weightA, "S")
print(boo)
print(d)
print(p)

spath(d,p,'D')
