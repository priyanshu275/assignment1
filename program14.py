items = input("Input comma separated sequence of words") # dog,cat,dog,bird
words = sorted(set(items.split(',')))
print(words)