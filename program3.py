string=input("give your string plz")
length=len(string)
if length>2:
    print(string[0:2]+string[-2:])
elif length==2:
    print(string[0:2]+string[0:2])
else:
    print(" ")