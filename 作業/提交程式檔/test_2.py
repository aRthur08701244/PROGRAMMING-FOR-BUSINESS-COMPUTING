a = [3,2,5,4,6,8]
b = [1,1,2,2,2,0]

order = []
qualified = []

for i in range(len(a)):
    for k in range(len(a)):
        if b[k] == i:
            qualified.append(k)

for i in range(len(a)):
    for k in range(i + 1, len(a)):
        if (b[qualified[i]] == b[qualified[k]]) & (a[qualified[i]] > a[qualified[k]]):
            tem = qualified[i]
            qualified[i] = qualified[k]
            qualified[k] = tem

for i in range(len(a)):
    print(qualified[i])