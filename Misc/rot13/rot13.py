def rot13(message):
    newMessage = ''
    for i in message:
        if i.isalpha():
            if i.islower():
                char = (ord(i)+13) - 123 + 97 if (ord(i)+13) > 122 else (ord(i)+13)
                newMessage += chr(char)
            else: # if i upper
                char = (ord(i)+13) - 123 + 97 if (ord(i)+13) > 90 else (ord(i)+13)
                newMessage += chr(char)
        else:
            newMessage += i
    return(newMessage)

print(rot13("EBG13 rknzcyr.")) # -> "ROT13 example."
print(rot13("@[`{")) # -> "@[`{"
print(rot13("123")) # -> "123"