name=input("the string we want to change ")
def change_string(name):
    return name[-1:]+name[1:-1]+name[:1]
print(change_string('abcd'))
