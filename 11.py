def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    res += A[i:] + B[j:]
    return res


a_list = list(map(int, input().split()))

b_list = list(map(int, input().split()))
fin_list = merge(a_list, b_list)
print(*fin_list, sep=' ')
