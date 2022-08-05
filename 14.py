try:
    f = open("input.txt", 'r', encoding='utf-8')
    a_dict = {school: 0 for school in range(1, 100)}
    for line in f:
        try:
            if len(line) == 0:
                break
            else:
                info1 = line.split()
                a_class = int(info1[2])
                a_dict[a_class] += 1
        except IndexError:
            pass

    max_list = []
    max_school = max(a_dict, key=a_dict.get)
    max_list.append(max_school)

    max_value = a_dict[max_school]

    a_dict.pop(max_school, None)
    while True:
        if max(a_dict.values()) == max_value:
            max_school = max(a_dict, key=a_dict.get)
            max_list.append(max_school)
            a_dict.pop(max_school, None)
        else:
            break
    print(*max_list, sep=' ')
except ValueError:
    print(*max_list, sep=' ')
