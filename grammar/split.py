f = open('grammar.txt', 'r')

text = ""

line = f.readline()
while(line):
    print(line)
    tmp = line.split()
    if(len(tmp) != 0):
        rule = ""
        rule += ('"' + tmp[0] + '"')
        rule += (': ')
        rule += '[["'
        cnt = 0
        for i in range(2, len(tmp)):
            if(tmp[i] != '|'):
                if(cnt != 0):
                    rule += '","'
                rule += tmp[i]
                cnt += 1
            else:
                rule += '"],["'
                cnt = 0

        rule += '"]],'
        text += rule + '\n'
    else:
        text += '\n'
    
    line = f.readline()


fr = open("grammarout.txt", 'w')
fr.writelines(text)