import string
x=input("give a sentence: ")
list_rot13=[]
for i in x:
    if i in string.ascii_letters:
        if i in string.ascii_uppercase:
            if ord(i)>=ord('N'):
                y= chr(ord(i)-13)
            else:
                y= chr(ord(i)+13)
        else:
            if ord(i) >= ord('n'):
                y= chr(ord(i)-13)
            else:
                y= chr(ord(i)+13)
    else:
        y=i
    list_rot13.append(y)
print("".join(list_rot13))
