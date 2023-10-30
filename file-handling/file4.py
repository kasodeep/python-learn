path = "/home/night_fury/python/file-handling/" + "hello.txt"

# Returns list of lines.
with open(path, "r") as f:
	cout = f.readlines()

print(type(cout), cout)
for i in cout:
	print(i, end = '')
print()
	
# "\n is removed by strip"
with open(path, "r") as f:
	for i in f:
		print(len(i), len(i.strip()))	
