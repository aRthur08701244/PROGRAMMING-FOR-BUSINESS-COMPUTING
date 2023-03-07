x = int(input())

for i in range(3):
    large = x // 100
    mid = (x - large*100) // 10
    small = (x - large*100 - mid*10)
    tem = int()

    if mid >= large:
        if small >= mid:
            tem = large
            large = small
            small = tem
        else:
            if large >= small:
                tem = large
                large = mid
                mid = tem
            else:
                tem = large
                large = mid
                mid = small
                small = tem
    else:
        if large <= small:
            tem = small
            small = mid
            mid = large
            large = tem
        else:
            if small >= mid:
                tem = mid
                mid = small
                small = tem

    x = (large - small)*100 + (small - large)
    
    if i != 0:
        print(",", end="")

    print(x, end="")