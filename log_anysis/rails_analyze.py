import re
f = open('rails_log', 'r', encoding='utf-8')

i = 1

while True:
    line = f.readline()
    if line:
        str_text = re.findall('/app/(.*?)', line, re.S)
        if str_text:
            print("--------i: ", i)
            print(line)
    i += 1

f.close()

