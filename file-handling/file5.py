path = "/home/night_fury/python/file-handling/" + "hello.txt"

# Append Mode
f = open(path, "a")
f.write("\nThird Line")
f.close()

# Read Mode
f = open(path, "r")
print(f.read())
f.close()

# Write Mode
f = open(path, "w")
f.write("Over-written")
f.close()

f = open(path, "r")
print(f.read())
f.close()
