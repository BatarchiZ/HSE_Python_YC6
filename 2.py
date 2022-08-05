a_list = list(map(int, input().split()))

number = 0
index = 0

for i, value in enumerate(a_list):
    if number <= value:
        number = value
        index = i
print(number, index)
