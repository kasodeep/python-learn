path = "/home/night_fury/python/file-handling/" + "hello.txt"

# Reading character by character.
with open(path, "r") as f:
	cont = f.read(10)
	cont1 = f.read(20)
	cont2 = f.read()

print("First 10: ", cont)
print("After 10, 20 Lines: ", cont1)
print("Remaining: ", cont2)
