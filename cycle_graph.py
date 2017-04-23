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
		self.__length = 0
		self.__steps = 0

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


	def __set_base(self):
		current = self.__base_node
		for i in range(self.__length):
			if self.__base_node.val > current.val:
				self.__base_node = current
			current = current.next

	def __pos_assign(self):
		current = self.__base_node
		for i in range(1,self.__length+1):
			current.pos = i
			current = current.next

	def __spin_assignment(self):
		current = self.__base_node
		for i in range(self.__length):
			x = current.val - current.pos
			if abs(x) > self.__length//2:
				if x > 0:
					x = x - self.__length
				elif x < 0:
					x = x + self.__length
			current.spin = x
			current = current.next

	def input(self, list):
		for i in list:
			self.__insert(i)
		self.__set_base()
		self.__pos_assign()
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
				string = string + str(current.val) + ",(spin: " + str(current.spin) + ") -> "
				current = current.next
			string = string + str(current.val)
			return string

	def step_counter(self):
		self.__steps = self.__steps + 1

	def __spin(self, p_1, p_2):
		p_1.val, p_2.val = p_2.val, p_1.val

	def __is_even(self):
		if self.__length % 2 == 0:
			return True
		else:
			return False

	def __is_ordered(self):
		current = self.__base_node
		for i in range(self.__length):
			if current.val < current.next.val:
				print(current.val, current.next.val)
				test = True
			else:
				return False
			current = current.next
		return test

	def sort_alg(self):
		pass

