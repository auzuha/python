def construct(string,words):
    if string == '':
        return True
    for i in words:
        if isPrefix(i,string):
            if construct(string[len(i):],words):
                return True
    return False



def isPrefix(small,big):
    for i in range(len(small)):
        if small[i] != big[i]:
            return False
    return True

print(construct('abcdef',['ab','def','c']))