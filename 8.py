info = list(map(int, input().split()))
number_users = info[1]
space = info[0]
occupancy_list = []
while number_users != 0:
    occupancy_list.append(int(input()))
    number_users -= 1
occupancy_list = sorted(occupancy_list)
answer = 0
for i in occupancy_list:

    if space - i < 0:
        pass
    else:
        space -= i
        answer += 1

print(answer)
