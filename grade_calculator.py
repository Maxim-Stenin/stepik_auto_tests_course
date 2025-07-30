s = input()
num = ""
res_2 = ""
count = s.count("[u-")
print(count)
for с in range(count):
    num = ""
    res_2 = ""
    if "[u-" not in s:
        break
    if "[u-" in s:
        s_index = s.find("[u-")
        print(s_index)
        for i in range(s_index+3, s_index + 7, 1):
            num += s[i]
        print(num)
        res = chr(int(num))
        for j in range(s_index, s_index + 8, 1):
            res_2 += s[j]
        print(res)
        print(res_2)
    s = s.replace(res_2, res)
print(s)