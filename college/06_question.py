numbers = [1,2,6,4,5,7,6,7,8,1,4,5]

count_list = []

for num in numbers:
    count = 0
    for x in numbers:
        if x == num:
            count = count + 1
    if count > 1 and [num, count] not in count_list:
        count_list.append([num, count])

for item in count_list:
    print(item[0], "appears", item[1], "times")