import os

# x will give error if file is present.
path = "/home/night_fury/python/file-handling/" + "hello1.txt"
f = open(path, 'x')

# w will create if not present and open.
path = "/home/night_fury/python/file-handling/" + "hello2.txt"
f = open(path, 'w')

os.remove(path)
