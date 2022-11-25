# belum selesai

#ignore = ["\t", " "]
reserved = ["break", "const", "case", "case", "catch", "class", "continue", "default", "delete", "else", "false", "finally", "for", "function", "if", "let", "null", "return", "switch", "throw", "try", "true", "var", "while"]

def fileToLines(fileName) :
    buffer = []
    # currentWord = ""
    tempCharList = []
    try :
        f = open(fileName, 'r')
        line = f.readline()
        while (line) :
            for word in (line.split()) :
                if word in reserved :
                    buffer.append(word)
                else :
                    if len(word) == 1 :
                        buffer.append(word)
                    else :
                        for char in word :
                            tempCharList.append(char)
                        buffer.append(tempCharList)
                        tempCharList = []
            buffer.append('\n')
            line = f.readline()
        return buffer
    except FileNotFoundError:
        print("\nFile Tidak Ditemukan!\n")
        return False

# def convertLineToList(line) :
#     buffer = []
#     word = ""
#     for char in line :
#         if (char not in ignore) :
#             if (char != '{' and char != '}') :
#                 word += char
#             else :
#                 buffer.append(word)
#                 word = ""
#                 buffer.append(char)
#         else :
#             if (len(word) == 0) :
#                 continue
#             else :
#                 buffer.append(word)
#                 word = ""
#     return buffer



if __name__ == "__main__" :
    text = fileToLines("test.js")
    # w = "function foo(x) { \n {x = 1} \n}"
    # print(w)
    # print(convertLineToList(w))

    print(text)