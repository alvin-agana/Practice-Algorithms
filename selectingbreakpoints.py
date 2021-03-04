lst1 = [0, 15, 35, 50, 65, 90, 100, 130, 140, 155]

def selectingBreakpoints(b):
    """
    s = the breakpoints selected
    x = the places that we get gas -- Set as our new starting pt. every time we get gas
    p = an iterator that goes through each break point in our trip and checks if its the farthest we can go 
    c = our capacity
    n = the length of our list/"trip"

    We want to find the breakpoints for our car from point A to point B.
    With a capacity C, and assuming it is possible to reach point B given our capacity,
    we want to use a greedy choice such that we go as far as we can go before getting gas.

    While we're not at our point B, check if the current break point we are visiting is within our capacity, and check
    if it is not the last point.
    If both are true, keep going to the next breakpoint.
    As soon as we find that the next breakpoint is unattainable for our capacity, go back to the last breakpoint.
        --> This is our farthest breakpoint.
    Check again if we're not at the last point.
    If we are not, let's set our new starting point at x and select the breakpoint as a point to get gas by our greedy choice.
    Keep going until we reach the end. 
    """
    s = []  
    x = 0
    p = 0
    c = 30
    n = len(b)
    while x != b[n - 1]:
        while b[p] <= x+c and p < n-1:
            p += 1
        p -= 1
        
        if b[p] == x:
            return s
        else:
            x = b[p]
            s.append(b[p]);
            print(s)


A = selectingBreakpoints(lst1)
print(A)
 
