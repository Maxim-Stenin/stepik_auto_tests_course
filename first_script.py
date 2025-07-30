start = ord("a")
finish = ord("z")
mnozh = 1
spisok = list()
for i in range(start, finish+1):
    bukv = chr(i)*mnozh
    spisok.append(bukv)
    mnozh += 1
print(spisok)