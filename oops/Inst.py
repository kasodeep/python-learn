class Inst:
	"""
	A class for Institue/University
	"""
	
   # Constructor
	def __init__(self, name, id_number, email_id):
		"""
		Information about the stakeholders of the institute
		"""
		self.name = name
		self.id_number = id_number
		self.email_id = email_id	
	
   # To String
	def __str__(self):
		"""
		Print the representation of data.
		"""
		
		return '{}\n{}\n{}'.format(self.name, self.id_number, self.email_id)

# Inheritance
class Faculty(Inst):
	"""
	Creating the information for the faculty members of the institute
	"""
	
	def __init__(self, name, id_number, email_id, salary):
		"""
		Information about the faculty of the institute
		"""
		
		super().__init__(name, id_number, email_id)
		self.salary = salary

# Inheritance
class Student(Inst):
	"""
	Creating the information for the students members of the institute
	"""
	
	def __init__(self, name, id_number, email_id, perc):
		"""
		Information about the students of the institute
		"""
		Inst.__init__(self, name, id_number, email_id)
		self.perc = perc
		self.gy = 2022

sandeep = Faculty('Sandeep Udmale', 1659, 'ssudmale@gmail.com', 100)
print(sandeep.name, sandeep.salary)

deep = Student('Kasodariya Deep', 1, 'dskaso@gmail.com', 90.95)
print(deep)
		
		
