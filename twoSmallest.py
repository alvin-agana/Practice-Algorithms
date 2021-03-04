#finds the two smallest numbers in an array
#assume array is of power of 2

list1 = [4,21,24,100,18,0,-3,8, 11]

def twoSmallest(A):
    if len(A) == 2:
        if A[1] >= A[0]:
            return A[0], A[1]
        else:
            return A[1], A[0]
    else:
        mid = int(len(A) / 2)
        (leftSmallest1, leftSmallest2) = twoSmallest(A[0:mid])
        (rightSmallest1, rightSmallest2) = twoSmallest(A[mid:len(A)])
        
        if leftSmallest2 < rightSmallest1:
            return leftSmallest1, leftSmallest2
        elif rightSmallest2 < leftSmallest1:
            return rightSmallest1, rightSmallest2
        else:
            if leftSmallest1 < rightSmallest1:
                return leftSmallest1, rightSmallest1
            else:
                return rightSmallest1, leftSmallest1

(first, second) = twoSmallest(list1)
print(first)
print(second)
