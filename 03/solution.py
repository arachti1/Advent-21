data = open("data.txt").read().split()
b_gamma = ""
b_epsilon = ""
b_oxy = data.copy()
b_co2 = data.copy()
# print(data, b_oxy, b_co2, sep = "\n")
for i in range(len(data[0])):
    most = '1' if len([row[i] for row in data if row[i] == '1'])/len(data) >= .5 else '0'
    b_gamma += most
    b_epsilon += '0' if most == '1' else '1'
    while b_oxy[0][:i + 1] != b_gamma and len(b_oxy) > 1:
        b_oxy.pop(0)
    while b_co2[0][:i + 1] != b_epsilon and len(b_co2) > 1:
        b_co2.pop(0)
    print(i, ":", b_gamma, [row[:i] + " " + row[i:] for row in  b_oxy[:5]])
    print("   ", b_epsilon, [row[:i] + " " + row[i:] for row in  b_co2[:5]])
    # oxy = [val for val in oxy if val[:i] == b_gamma[:i] or len(oxy) == 1]
    # co2 = [val for val in co2 if val[:i] == b_epsilon[:i] or len(co2) == 1]
gamma = int(b_gamma, 2)
epsilon = int(b_epsilon, 2)
oxy = int(b_oxy[0], 2)
co2 = int(b_co2[0], 2)
print(gamma, epsilon, gamma * epsilon)
print(oxy, co2, oxy * co2)