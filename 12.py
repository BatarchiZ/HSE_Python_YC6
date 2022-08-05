f = open("input.txt", 'r', encoding='utf-8')
a_dict = {'9': 0, '10': 0, '11': 0}

for line in f:
    try:
        if len(line) == 0:
            break
        else:
            info1 = line.split()
            a_class = info1[2]
            score = int(info1[3])

            if score > int(a_dict[a_class]):
                a_dict[a_class] = info1[3]
    except IndexError:
        pass

a_list = list(a_dict.values())
print(*a_list, sep=' ')
