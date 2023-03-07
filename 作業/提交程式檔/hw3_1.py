initial = int(input())
final = int()

while True:
    lst = [0, 0, 0, 0]
    lst[0] = initial // 1000
    lst[1] = (initial - lst[0]*1000) // 100
    lst[2] = (initial - lst[0]*1000 - lst[1]*100) // 10
    lst[3] = (initial - lst[0]*1000 - lst[1]*100 - lst[2]*10)

    lst.sort()

    biggest = lst[3]*1000 + lst[2]*100 + lst[1]*10 + lst[0]*1
    smallest = lst[0]*1000 + lst[1]*100 + lst[2]*10 + lst[3]*1

    final = biggest - smallest

    if final == 6174:
        print(6174, end="")
        break
    else:
        print(final, end=",")
        initial = final