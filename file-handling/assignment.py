path = '/home/night_fury/python/file-handling/'

# Read the contents of the file.
while(True):
	try:
		name = input("Please enter file name: ")
		path = path + name
		
      # Reading lines.
		with open(path, 'r') as f:
			lines = f.readlines()
		
      # Reading characters.
		with open(path, 'r') as f:
			cont = f.read()
		break;
	except(FileNotFoundError):
		print("Please Enter valid file name.")
		path = '/home/vjti/'
	except():
		print("Unknown Error")

def isEmpty(cont):
	"""
	Checks wheter the file is empty or not.
	"""
	return len(cont) == 0			
	
def noOfLines(lines):
	"""
	Returns the number of lines.
	"""
	return len(lines)
	

def func(cont):
	if ('\n' in cont):
		return False
	else:
		return True
		
def noOfCharacters(cont):
	"""
	Prints the number of characters in a file.
	"""
	
	data = cont.replace(" ","")
	data = filter(func, data)
	data = list(data)
	print("Number of characters without spaces:", len(data))

def noOfWords(cont):
	"""
	Prints the number of words.
	"""
	
	print("Number of words are:", len(cont.split()))

def noOfUniqueWords(cont):
	"""
	Prints the number of unique words.
	"""
		
	temp = set(cont.split())
	print("Number of unique words are:", len(temp))
	

def helper(cont):
	"""
	Counts the frequncy of all the words.
	"""
	
	word_counter = {}
	temp = cont.split()
	for word in temp:
		if word in word_counter:
			word_counter[word] += 1
		else: 
			word_counter[word] = 1
	return word_counter

def fiveMostCommon(cont):
	"""
	Prints 5 most common words.
	"""
	word_counter = helper(cont)
	
	popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
	print("Most common words: ", popular_words[:5])

def fiveLeastCommon(cont):
	"""
	Prints 5 least common words.
	"""
	word_counter = helper(cont)
	
	popular_words = sorted(word_counter, key = word_counter.get)
	print("Least common words: ", popular_words[:5])

def firstLastCapital(lines):
	"""
	Capitalizes first and last characters of each line.
	"""
	ans = []
	for line in lines:
		temp = line.split()
		
		if(len(temp) > 0):
			temp[0] = temp[0][0].upper() + temp[0][1:]
			temp[len(temp) - 1] = temp[len(temp) - 1][:len(temp[len(temp) - 1]) - 1] + temp[len(temp) - 1][len(temp[len(temp) - 1]) - 1].upper()
         
		s = ' '.join(temp)
		ans.append(s)
		
	s = '\n'.join(ans)
	f = open(path, "w")
	f.write(s)
	f.close()

fiveLeastCommon(cont)
fiveMostCommon(cont)

noOfUniqueWords(cont)
noOfWords(cont)
noOfCharacters(cont)

print("No of lines are:", noOfLines(lines))
print("File is empty:", isEmpty(cont))

firstLastCapital(lines)
# Go to terminal: man ls >> test.txt

