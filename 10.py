km = list(map(int, input().split()))
price = list(map(int, input().split()))

i = len(km)
sum = 0
while i != 0:
    sum += max(km) * min(price)
    i -= 1
    km.remove(max(km))
    price.remove(min(price))
print(sum)
