import pandas as pd

data = pd.read_csv(r'C:\Users\sophie\IdeaProjects\Python\Current\Advent_of_code_2021\Day_1_input.csv')
column_1 = data.iloc[:,0]
diff_list = []
for i in range(1,len(column_1)):
    x = column_1[i] - column_1[i-1]
    diff_list.append(x)
#print(diff_list) #checking differences
pos_count, neg_count = 0, 0
for num in diff_list:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1
print('Part 1 - Number of measurements larger than previous measurement:',pos_count)

s = pd.Series(column_1)
rolling_sum = s.rolling(3).sum()

#print(rolling_sum)

diff_list_2 = []
for i in range(2,len(rolling_sum)):
    y = rolling_sum[i] - rolling_sum[i-1]
    diff_list_2.append(y)

pos_count_2, neg_count_2 = 0, 0
for num in diff_list_2:
    if num > 0:
        pos_count_2 += 1
    else:
        neg_count_2+ = 1

print('Part 2 - Number of measurements larger than previous measurement:',pos_count_2)