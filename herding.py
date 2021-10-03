fin = open("herding.in", "r")
fout = open("herding.out", "w")
positions = list(map(int, fin.readline().split()))
upper = positions[2] - positions[1]
lower = positions[1] - positions[0]
if upper == 1 and lower == 1:
    fout.write(str(0) + '\n')
    fout.write(str(0))
else:
    if upper == 2 or lower == 2:
        fout.write(str(1) + '\n')
    else:
        fout.write(str(2) + '\n')
    fout.write(str(max(upper, lower) - 1))
