firststr = input()
secondstr = input()
thirdstr = input()
fourthstr = input()
firststr = firststr.split(',')
secondstr = secondstr.split(',')
thirdstr = thirdstr.split(',')
fourthstr = fourthstr.split(',')

n = int(firststr[0])  # num of item
B = int(firststr[1])  # weight boundary

total_w = int()
total_v = int()

for i in range(len(fourthstr)):
    if int(fourthstr[i]) == 1:
        total_w += int(secondstr[i])
        total_v += int(thirdstr[i])

if total_w <= B:
    print(str(total_w) + ',' + str(total_v))

else:
    print(-1)
