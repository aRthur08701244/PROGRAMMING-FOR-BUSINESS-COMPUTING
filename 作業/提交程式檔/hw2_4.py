import math

n = int(input())
s = list()

for i in range(n):
    s.append(float(input()))

au041 = int()
au042 = int()
au043 = int()

for i in range(n):
    if s[i] > 7.0:
        au041 += 1

total = float()
aver = float()
for i in range(n):
    total += s[i]
aver = total / n

if aver <= 6.0:
    au042 = n - au041
else:
    au043 = n - au041

lemon = float()
oil = float()
honey = float()
egg = float()

lemon = 1.5*au041
oil = 4*au041 + 9*au042
honey = 18*au042 + 6*au043
egg = 2*au043

if math.ceil(lemon) >= 5:
    lp = math.ceil(lemon)*6.3
else:
    lp = math.ceil(lemon)*7
op = oil*0.6
hp = honey*1.2
ep = math.ceil(egg/3)*25

tp = lp + op + hp + ep

print(int(tp))