"""
Depth-First Search using dictionaries as graph & color representations.
white -> not visited
gray -> visited, but not complete
black -> visited and complete

We want to check every vertex and see how deep it goes in the graph, and then go back up.
First, we initialize all elements to "white".
Then we check if every vertex in the graph is "white".
If it is, then we color it gray and check the edges of those vertices and repeat.\
"""

graph = {
    "S": ['A', 'C', 'G'],
    "A": ['B', 'S'],
    "B": ['A'],
    "C": ['D', 'E', 'F', 'S'],
    "D": ['C'],
    "E": ['C', 'H'],
    "F": ['C', 'G'],
    "G": ['F', 'H', 'S'],
    "H": ['E', 'G']
}

time = 0

def depthFirst(g):
    color = {}
    for vertex in g:
        color[vertex] = "white"
    print ("Starting from the beginning node S..")
    for vertex in g:
        if color[vertex] == "white":
            visit(vertex, g, color, time)

def visit(v, g, color, time):
    print("We visited " + v)
    color[v] = "gray"
    time += 1
    edgesOfV = g[v]
    for edge in edgesOfV:
        if color[edge] == "white":
            visit(edge, g, color, time)
    color[v] = "black"
    time += 1

depthFirst(graph)
print(time)
