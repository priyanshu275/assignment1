name="priyanshu sharma"
dict={}
for i in name:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print("the character in priyanshu"+str(dict))
