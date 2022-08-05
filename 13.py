f = open("input.txt", 'r', encoding='utf-8')
a_dict = {'9': 0, '10': 0, '11': 0}
counter9 = 0
counter10 = 0
counter11 = 0

for line in f:
    try:
        if len(line) == 0:
            break
        else:
            info1 = line.split()
            a_class = info1[2]
            if int(a_class) == 9:
                counter9 += 1

            if int(a_class) == 10:
                counter10 += 1
            if int(a_class) == 11:
                counter11 += 1
            a_dict[a_class] += int(info1[3])
    except IndexError:
        pass
a_list = list(a_dict.values())
value9 = float(a_list[0] / counter9)
value10 = float(a_list[1] / counter10)
value11 = float(a_list[2] / counter11)
print(value9, value10, value11)
