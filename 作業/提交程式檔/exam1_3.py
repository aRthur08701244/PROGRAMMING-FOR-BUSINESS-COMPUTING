firststr = input()
firststr = firststr.split(',')
for i in range(len(firststr)):
    firststr[i] = int(firststr[i])
n = firststr[0]
B = firststr[1]

secondstr = input()
secondstr = secondstr.split(',')
w = []
for i in range(len(secondstr)):
    w.append(int(secondstr[i]))

w.reverse()

num_box = 1
box = [0]

for i in range(len(w)):
    for k in range(num_box):
        if k < (num_box - 1) and w[i] <= (B - box[k]):
            box[k] += w[i]
            break
        elif k == (num_box - 1) and w[i] <= (B - box[k]):
            box[k] += w[i]
        elif k == (num_box - 1) and w[i] > (B - box[k]):
            num_box += 1
            box.append(w[i])

print(num_box)