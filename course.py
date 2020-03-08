class Course(Department):
	def __init__(self, Cname, Dname, Dhead,Section):
		super().__init__(self, Dname, Dhead, Section)
		self.Cname = Cname
	
	
	def toString(self):
		print( " Course name | " + Cname)
		
c1 = Course