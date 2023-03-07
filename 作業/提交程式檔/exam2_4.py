strin = input()
out = str()
englishcha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chinesecha = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
def trans(i):
    for k in range(len(chinesecha)):
        if i == str(englishcha[k]):
            return str(chinesecha[k])
        elif i == '+':
            return '加'
        elif i == '-':
            return '減'
        elif i == '*':
            return '乘以'
        elif i == '/':
            return '除以'
        elif i == '=':
            return '等於'
for i in range(len(strin)):
    out += trans(strin[i])

while True:
    before = out
    for i in range(len(out) - 1):
        if (out[i] in chinesecha) & (out[i + 1] in chinesecha):
            out = out[:i + 1] + '十' + out[i + 1:]

    out = out.replace("一十", "十")

    if before == out:
        break

print(out)

