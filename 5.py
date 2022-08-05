a_list = list(map(int, input().split()))
a_list_copy = a_list[:]
max1 = max(a_list)
a_list.remove(max1)
max2 = max(a_list)
a_list.remove(max2)
max3 = max(a_list)
min1 = min(a_list_copy)
a_list_copy.remove(min1)
min2 = min(a_list_copy)
a_list_copy.remove(min2)
if max1 * max2 * max3 >= min1 * min2 * max1:
    print(max1, max2, max3)
else:
    print(max1, min1, min2)
