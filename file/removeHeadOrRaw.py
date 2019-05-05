f = open("removeHeadOfRaw.txt", "r", encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line[line.index(".") + 1:], end='')

f.close()
