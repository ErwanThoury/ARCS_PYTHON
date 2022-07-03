class fib:
    def __init__(self):
    	self.ni = None
	self.ni1 = None
    def __iter__(self):
	return self
    def __next__(self):
	if self.ni is None:
		self.ni = 0
		return self.ni
	if self.ni1 is None:
		self.ni1 = 1
		return 1
	ni2 = self.ni1 + self.ni
	self.ni = self.ni1
	self.ni1 = ni2
	return ni2

	
for i in fib():
	print(i)
	if i > 100:
		break
