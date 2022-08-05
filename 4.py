a_list = list(map(int, input().split()))
pos1 = 0
pos2 = 0
neg1 = 0
neg2 = 0
if len(a_list) == 2:
    print(min(a_list[1], a_list[0]), max(a_list[1], a_list[0]))
else:
    for i in range(0, len(a_list)):
        if a_list[i] > 0:
            if a_list[i] < pos1 and a_list[i] > pos2:
                pos2 = a_list[i]
            if a_list[i] >= pos1:
                if pos1 > pos2:
                    pos2 = pos1
                pos1 = a_list[i]

        if a_list[i] < 0:
            if a_list[i] > neg1 and a_list[i] < neg2:
                neg2 = a_list[i]
            if a_list[i] <= neg1:
                if neg1 < neg2:
                    neg2 = neg1
                neg1 = a_list[i]

    if pos2 * pos1 >= neg1 * neg2:
        print(min(pos2, pos1), max(pos1, pos2))
    else:
        print(min(neg1, neg2), max(neg2, neg1))

