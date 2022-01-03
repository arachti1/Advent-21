data = open("data.txt").read().split()
gamma = []
epsilon = []
oxy = data.copy()
co2 = data.copy()
for i in range(len(data[0])):
    most = 1 if len([row[i] for row in data if row[i] == '1'])/len(data) >= .5 else 0
    gamma.append(str(most))
    epsilon.append('0' if most else '1')
    oxy = [val for val in oxy if val[0:i] == data[i]]
gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)
print(gamma, epsilon, gamma * epsilon)