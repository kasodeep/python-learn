# Reading the file in read mode.
# 1) Method: 1
f = open("hello.txt", "r")
cont = f.read()

print(type(cont), cont)
f.close()
print()

# 2) Method: 2
with open('hello.txt', 'r') as f:
	cont = f.read()
print(cont)
