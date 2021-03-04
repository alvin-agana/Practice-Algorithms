"""
Breadth-First Search using dictionaries as graph & distance representations
and arrays as queue representations.
Make the distance to each vertex a large, arbritrary number (+infinity).
Let the distance of the starting index "S" be 0.
Insert the starting index in the queue.
While the queue isn't empty, pop it and search every adjacent vertex of the queue.
If we find that the distance of the edges of the vertex we are looking at is +infinity,
then let distance of edge = to distance of current vertex + 1.
Insert that edge into queue so we can look at the edges of that vertex.
Return the distance dictionary to get the list of the distances.

"""

graph = {
    "S": ['C'],
    "A": ['S'],
    "C": [ 'E',],
    "D": ['S'],
    "E": ['D', 'F'],
    "F": [],
}

def breadthFirst(g, s):
    distance = {}
    queue = []
    for vertex in g:
        distance[vertex] = 10000

    distance["S"] = 0
    queue.insert(0, "S")
    while queue:
        tempVertex = queue.pop()
        for edge in g[tempVertex]:
            if distance[edge] == 10000:
                distance[edge] = distance[tempVertex] + 1
                queue.insert(0, edge)
    return distance

d = breadthFirst(graph, "S")
print(d)
        
