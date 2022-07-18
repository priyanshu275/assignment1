def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'island'))
print(add_tags('b', 'adventure'))