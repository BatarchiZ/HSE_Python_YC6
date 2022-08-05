d = {}
for line in open('input.txt'):
    try:
        person, score = line.rstrip().split()
        score = int(score)
        if person not in d:
            d[person] = score
    except ValueError:
        pass
while len(d) != 0:
    lolololo = max(d, key=d.get)
    print(lolololo)
    del d[lolololo]

# Both Solving methods are good

#   if customer not in d:
#     d[customer] = {}
#   d[customer][product] = d[customer].get(product, 0) + quantity
#
# for customer in sorted(d.keys()):
#   print(customer + ":")
#   for product in sorted(d[customer].keys()):
#     print(product, d[customer][product])
