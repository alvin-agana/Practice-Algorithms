"""
Activity Selection. Greedy algorithm, where our greedy choice is to pick the activities that end the earliest.
Activity Selection Start Last. Greedy algorithm, where our greedy choice is to pick the acitivities that start the latest.
"""

def activitySelection(start, finish):
    n = len(start)
    A = []
    j = 1
    A.append(j)
    for i in range(2, n):
        if start[i] >= finish[j]:
            A.append(i)
            j = i
    return A

def activitySelectionStartLast(start, finish):
    n = len(start)
    A = []
    j = n - 1
    i = n - 2
    A.append(j)
    for i in range(n-1, -1, -1):
        if start[j] >= finish[i]:
            A.append(i)
            j = i
    return A

S = [0,1, 1, 3, 5, 8, 12, 14]
F = [0, 3, 5, 6, 8, 13, 15, 18]
print(activitySelection(S,F))
print(activitySelectionStartLast(S,F))

# prints indexes of starting array of the activities chosen
