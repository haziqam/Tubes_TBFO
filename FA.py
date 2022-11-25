uppercase=[[chr(ord('A')+i)] for i in range(26)]
lowercase=[[chr(ord('a')+i)] for i in range(26)]
integer=[[chr(ord('0')+i)] for i in range(10)]
firstChar = uppercase+lowercase+[['_']]
nextChar = uppercase+lowercase+[['_']]+integer

def variableFA(s):
    state = 0
    for c in s:
        if ((state == 0) and (c in firstChar)):
            state = 1
        elif ((state == 1) and (c in nextChar)):
            state = 1
        else:
            state = 2
    if (state == 1):
        return True
    else:
        return False