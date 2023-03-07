w0 = 0.5
wa = float()
wh = float()
c = int(input())
h = int()
t = int(input())
d = int(input())
w = float()
v = float(input())

if c <= 35:
    wa = w0 + (100 - c) * 0.005
else:
    wa = w0 + (45 - c) * 0.02

h = 100 - 5 * (t - d)
if h <= 30:
    wh = (w0 / 60) * (110 - h)
else:
    wh = (w0 / 45) * (90 - h)

if wa < 0:
    wa = 0
if wa > 1:
    wa = 1
if wh < 0:
    wh = 0
if wh > 1:
    wh = 1

if wa >= wh:
    w = wh
else:
    w = wa

print('{:.2f}'.format(w))

if w >= v:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")