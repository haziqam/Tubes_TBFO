# belum selesai

def fileToLines(fileName) :
    buffer = []
    f = open(fileName, 'r')
    contents = f.readline()
    while (contents) :
        buffer.append(contents)
        contents = f.readline()
    return buffer

print(fileToLines("inputAcc.js"))


