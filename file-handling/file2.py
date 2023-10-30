import os
print(os.getcwd())

path = "/home/night_fury/python/file-handling/" + "hello.txt"
with open(path, 'r') as f:
	cont = f.read()
print(cont)
print()

path = os.getcwd() + "/"

# All the directories in the following path.
cont = os.listdir(path)
print(type(cont), cont)


