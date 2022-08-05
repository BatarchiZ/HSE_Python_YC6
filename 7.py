keys = int(input())
max_press = list(map(int, input().split()))
total_press = int(input())
presses = list(map(int, input().split()))
a_dict = {index: i for index, i in enumerate(max_press, 1)}

for press in presses:
    a_dict[press] -= 1

for key in a_dict:
    if a_dict[key] < 0:
        print('YES')
    else:
        print('NO')
