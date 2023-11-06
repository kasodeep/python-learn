class Book:
	"""
	Information about the books in the library
	"""
	
   # Constructor function
	def __init__(self, title, author, price, publisher):
		"""
		Create a new book with title, author, price and publisher information
		"""	
		self.title = title
		self.author = author[:]
		self.price = price
		self.publisher = publisher
		
   # Member functions
	def number_of_authors(self):
		"""
		(Book) -> int
		Returns the number of authors of the book
		"""
		
		return len(self.author)

	def print_price(abc):
		"""
		Printing the cost of the book.
		"""
		
		print(abc.price)

   # Overriden Methods
	def __str__(self):
		"""
		Print the human readable output
		"""
		
		return """Title: {0}
		Authors: {1}
		Price: {2}
		Publisher: {3}""".format(self.title, ",".join(self.author), self.price, self.publisher)
		
	def __eq__(self, other):
		"""
		Returns true if book and other book has same publisher
		"""
	
		return self.publisher == other.publisher
	

python_book1 = Book('Python', ["ABC", "XYZ", "UVW"], 299, "THM")
print(python_book1)
		
print(Book.number_of_authors(python_book1))	
print(Book.print_price(python_book1))
print(python_book1.print_price())
		
		
