#Part 1
binary_data = open("input_day_3.txt")
sbd = []
for line in binary_data:
    sbd.append(line.strip("\n"))

gamma = ""
epsilon = ""

for i in range(len(sbd[0])):
    count_one = 0
    count_zero = 0
    for item in sbd:
        if item[i] == "1":
            count_one += 1
        else:
            count_zero += 1
    if count_one >= count_zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

a = int(gamma,2)
b = int(epsilon,2)
answer = a*b
print(answer)
