def first_three(str1):
    if len(str1) > 3:
        return str1[0:3]
    else:
        return str1

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))