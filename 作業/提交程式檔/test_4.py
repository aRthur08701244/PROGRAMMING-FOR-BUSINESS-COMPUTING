total = float()
for i in range(25):
    if i == 0:
        f = 1
    else:
        f = 1
        for k in range(1, i + 1):
            f = f*k
    total += (2.718**(-20))*(20**i)/f

total = 1 - total

print(total)



total_2 = float()

mnb = 1
for i in range(1, 26):
    mnb = mnb*i

for i in range(10):
    n = 25 - i
    if i == 0:
        r_2 = 1
    else:
        r_2 = 1
        for k in range(1, i + 1):
            r_2 = r_2*k

    r_3 = 1
    for k in range(1, n + 1):
        r_3 = r_3*k

    f = mnb / (r_2 * r_3)
    total_2 += f*(0.45**i)*(0.55**(25-i))

total_2 = 1 - total_2
print(total_2)