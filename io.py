# belum selesai

ignore = ["\n", "\t", " "]
reserved = []

def fileToLines(fileName) :
    buffer = []
    ctr = 0
    f = open(fileName, 'r')
    line = f.readline()
    while (line) :
        buffer.append(line)
        ctr += 1
        line = f.readline()
    return buffer

def convertLineToList(line) :
    buffer = []
    word = ""
    for char in line :
        if (char not in ignore) :
            word += char
        else :
            if (len(word) == 0) :
                continue
            else :
                buffer.append(word)
                word = ""
    return buffer

if __name__ == "__main__" :
    print(convertLineToList("\t Hello    semuanya!\n"))