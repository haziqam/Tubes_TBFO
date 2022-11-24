# belum selesai

ignore = ["\n", "\t", " "]
reserved = []

def fileToLines(fileName) :
    buffer = []
    ctr = 0
    try :
        f = open(fileName, 'r')
        line = f.readline()
        while (line) :
            buffer.append(line)
            ctr += 1
            line = f.readline()
        return buffer
    except FileNotFoundError:
        print("\nFile Tidak Ditemukan!\n")
        return False

def convertLineToList(line) :
    buffer = []
    word = ""
    for char in line :
        if (char not in ignore) :
            if (char != '{' and char != '}') :
                word += char
            else :
                buffer.append(word)
                word = ""
                buffer.append(char)
        else :
            if (len(word) == 0) :
                continue
            else :
                buffer.append(word)
                word = ""
    return buffer



if __name__ == "__main__" :
    #text = fileToLines("inputAcc.js")
    w = "function foo(x) { \n {x = 1} \n}"
    print(w)
    print(convertLineToList(w))

    #["function foo(x)", "{", "{", "x = 1", "}", "}"]