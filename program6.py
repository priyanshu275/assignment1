a = input("the string is ")
length = len(a)
if length < 3 :
    print(a)
elif a[-3:] == "ing":
    print(a+"ly")
elif a[-3:] != "ing":
    print(a+"ing")