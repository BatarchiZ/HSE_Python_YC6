a_list = list(map(int, input().split()))
for i, value in enumerate(a_list):
    try:
        if value >= a_list[i + 1]:
            print('NO')
            break
    except IndexError:
        print('YES')
