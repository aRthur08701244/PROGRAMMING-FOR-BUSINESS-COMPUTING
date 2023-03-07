
k = [1, 2, 3, 4 ,5]

print(k[-1])



"""
import datetime

def f1 (x):
    return x**2

list1=[3,5,1.2, 4, 9]
out1=map(f1, list1)
print(list(out1))

eng2cn = {'two': '二', 'three': '三','four': '四', 'one': '一'}
print(eng2cn)
print(eng2cn.items())

def histogram(seq):
    d = dict()
    for element in seq:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    return d


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv

hist = histogram('parrot')
print(hist)
inverted = invert_dict(hist)
print(inverted)

d5 = datetime.datetime(2000,1,1,0,0,0)
diff2 = datetime.timedelta(days=3,seconds=4)

print(d5+diff2)

b = []
def a (x, d):
    d.append(x)

a(1, b)

print(b)
"""