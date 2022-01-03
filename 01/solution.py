def threesum(i):
    return 0 if i > len(inp) - 3 else inp[i] + inp[i + 1] + inp[i + 2]

inp = [int(i) for i in open("data.txt").read().split()]

ts_sup = 0
sup = 0

for i in range(len(inp) - 1):
    if inp[i] < inp[i + 1]:
        sup += 1
    if threesum(i) < threesum(i + 1):
        ts_sup += 1

print(sup)
print(ts_sup)