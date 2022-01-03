cmds = [cmd.split() for cmd in open("data.txt").read().split('\n')]
x = 0
depth = 0
corrected_depth = 0
for cmd in cmds:
    cmd[1] = int(cmd[1])
    if cmd[0] == "up":
        depth -= cmd[1]
    if cmd[0] == "down":
        depth += cmd[1]
    if cmd[0] == "forward":
        x += cmd[1]
        corrected_depth += depth * cmd[1]

print(x, depth, corrected_depth, x * depth, x * corrected_depth)