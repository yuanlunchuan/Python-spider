import re
f = open('accessLog.txt', 'r', encoding='utf-8')

i = 1;
line = f.readline()
result = {}
while line:
    line = f.readline()
    msg = "----------:"+str(i)+"------: "+line.split(' - - ')[0]
    if line.split(' - - ')[0] in result:
        result[line.split(' - - ')[0]] = result[line.split(' - - ')[0]]+1
    else:
        result[line.split(' - - ')[0]] = 0
    print(msg)
    i += 1
print(result)
f.close()


