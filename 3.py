size = int(input())
a_list = list(map(int, input().split()))
number = int(input())
answer = a_list[0]

for i in range(0, size):
    if abs((number - a_list[i])) <= abs((number - answer)):
        answer = a_list[i]

print(answer)
