# Part 1
import pandas as pd

data = pd.read_csv(r'C:\Users\sophie\IdeaProjects\Python\Current\Advent_of_code_2021\Day_2_input.csv')
column_1 = data.iloc[:,0]

strings_with_forward = [string for string in column_1 if 'forward' in string]
strings_with_down = [string for string in column_1 if 'down' in string]
strings_with_up = [string for string in column_1 if 'up' in string]

horitontal = sum([int(number) for item in strings_with_forward for number in item.split() if number.isnumeric()])
down = sum([int(number) for item in strings_with_down for number in item.split() if number.isnumeric()])
up = sum([int(number) for item in strings_with_up for number in item.split() if number.isnumeric()])

depth = down-up
answer = horitontal*depth

#print(answer)

# Part 2 (new method, part 1 method not helpful...)

split_list = []
for item in column_1:
    create_array = item.replace("\n","")
    split_item = create_array.split(' ')
    split_list.append(split_item)

horizontal = 0
depth = 0
aim = 0

for item in split_list:
    if item[0] == 'forward':
        horizontal += int(item[1])
        aim += (depth * int(item[1]))
    elif item[0] == 'down':
        depth += int(item[1])
    elif item[0] == 'up':
        depth -= int(item[1])

print(horizontal * aim)




