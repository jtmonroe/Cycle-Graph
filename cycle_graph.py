class cycle_graph():

	class __cg_Node():
		def __init__(self, val):
			self.prev = None
			self.next = None
			self.val = val
			self.spin = 0
			self.pos = 0

	def __init__(self):
		self.__base_node = None
		self.__standing = None
		self.__length = 0
		self.__steps = 0

	def __set_base(self):
		current = self.__base_node
		for i in range(self.__length):
			if self.__base_node.val > current.val:
				self.__base_node = current
			self.__standing = self.__base_node
			current = current.next

	def __pos_assign(self, n):
		current = self.__base_node
		for i in range(1,self.__length+1):
			if i + n > self.__length:
				current.pos = i + n - self.__length
			else:
				current.pos = i + n
			current = current.next

	def __spin_assignment(self):
		current = self.__base_node
		for i in range(1, self.__length + 1):
			current.spin = current.pos - current.val 
			current = current.next

	def __insert(self, val):
		new_node = self.__cg_Node(val)
		if self.__length == 0:
			new_node.next = new_node
			new_node.prev = new_node
			self.__base_node = new_node
		else:
			self.__base_node.prev.next = new_node
			new_node.prev = self.__base_node.prev
			self.__base_node.prev = new_node
			new_node.next = self.__base_node
		self.__length = self.__length + 1

	def input(self, list, n = 0):
		for i in list:
			self.__insert(i)
		self.__set_base()
		self.__pos_assign(n)
		self.__spin_assignment()

	def __len__(self):
		return self.__length

	def __str__(self):
		if self.__length == 0:
			return ""
		else:
			current = self.__base_node
			string = ""
			for i in range(self.__length):
				string = string + str(current.val) + "-> "
				current = current.next
			string = string + str(current.val)
			return string

	#PROPERTY FUNCTIONS
	def disp(self):
		total = 0
		if self.__length == 0:
			return ""
		else:
			current = self.__base_node
			string = ""
			for i in range(self.__length):
				string = string + str(current.spin) + "-> "
				total = total + current.spin
				current = current.next
			string = string + str(current.val)
			if total == 0:
				return string
			else:
				return total

	def total_spin(self):
		current = self.__base_node
		total = 0
		for i in range(self.__length):
			total = total + abs(current.spin)
			current = current.next
		return total

	#SORTING FUNCTIONS
	def step_counter(self):
		self.__steps = self.__steps + 1

	def next_node(self):
		self.__standing = self.__standing.next

	def print_current(self):
		print(self.__standing.val)

	def spin(self, p_1, p_2):
		p_1.next = p_2.next
		p_2.prev = p_2.prev
		p_1.prev.next = p_2
		p_2.next.prev = p_1 
		p_1.prev = p_2
		p_2.next = p_1
		self.__pos_assign(0)
		self.__spin_assignment()	