a = input('give your string')
b = a.find('poor')
not1 = a.find('not')
if not1 > b and not1 > 0 and b> 0:
   a = a.replace(a[not1:(b+4)], 'good')
   print(a)
else:
    print(a)

