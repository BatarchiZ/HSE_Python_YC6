def QuickSort(A):
    less = []
    equal = []
    greater = []
    if len(A) > 1:
        mid = A[0]
        for x in A:
            if x < mid:
                less.append(x)
            if x == mid:
                equal.append(x)
            if x > mid:
                greater.append(x)
        return QuickSort(less) + equal + QuickSort(greater)
    else:
        return A


print(*QuickSort(list(map(int, input().split()))), sep=' ')
