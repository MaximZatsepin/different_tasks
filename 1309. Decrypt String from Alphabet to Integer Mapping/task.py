#a-z 97-122
def freqAlphabets(s: str) -> str:
    newStr = ''
    for i in range(len(s)):
        if s[i] == '#':
            newStr = newStr[:-2:]
            newStr += chr(int(s[i-2] + s[i-1]) + 96)
        else:
            newStr += chr(int(s[i]) + 96)
    return newStr


print(freqAlphabets('10#11#12')) # -> jkab