class cycle_graph():

	class __cg_Node():
		def __init__(self, val):
			self.prev = None
			self.next = None
			self.val = val
			self.spin = 0
			self.pos = 0
			self.n = 0

		def __gt__(self, other):
			s = self.spin - other.spin
			d = other.pos - self.pos
			if other.pos > self.pos:
				if s > d:
					return True
			if other.pos < self.pos:
				if s > d + self.n:
					return True
			return False

	def __init__(self, list, n = 0):
		self.__base_node = None
		self.__standing = None
		self.__length = 0
		self.__steps = 0
		self.__input(list, n)


	def __input(self, list, n = 0):
		for i in list:
			self.__insert(i)
		self.__pos_assign(n)
		self.__spin_assign()
		self.__standing = self.__base_node

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
		current = self.__base_node
		for i in range(self.__length):
			current.n = self.__length
			current = current.next

	def __pos_assign(self, n):
		current = self.__base_node
		for i in range(1,self.__length+1):
			if i + n > self.__length:
				current.pos = i + n - self.__length
			else:
				current.pos = i + n
			current = current.next

	def __spin_assign(self):
		current = self.__base_node
		for i in range(1, self.__length + 1):
			current.spin = current.val - current.pos
			current = current.next
		self.optimize()

	#PROPERTY FUNCTIONS
	def __len__(self):
		return self.__length

	def __str__(self):
		if self.__length == 0:
			return ""
		else:
			current = self.__base_node
			string = ""
			for i in range(self.__length - 1):
				string = string + str(current.val) + "-> "
				current = current.next
			string = string + str(current.val)
			return string

	def dist(self):
		if self.__length == 0:
			return ""
		else:
			current = self.__base_node
			list_ = []

			for i in range(self.__length - 1):
				list_.append(current.spin)
				current = current.next

			list_.append(current.spin)
			return list_

	def total_spin(self):
		current = self.__base_node
		total = 0
		for i in range(self.__length):
			total = total + abs(current.spin)
			current = current.next
		return total

	def terms(self):
		current = self.__base_node
		out = []
		for i in range(self.__length):
			out.append(current.val)
			current = current.next
		return out

	def not_ordered(self):
		current = self.__base_node
		for i in range(self.__length):
			if current.pos != current.val:
				return True
			current = current.next
		return False

	def value(self):
		return self.__standing.val

	def next_value(self):
		return self.__standing.next.val

	def spin(self):
		return self.__standing.spin

	def next_spin(self):
		return self.__standing.next.spin

	def position(self):
		return self.__standing.pos

	def steps(self):
		return self.__steps

	def compare(self):
		return self.__standing > self.__standing.next


	#SORTING FUNCTIONS
	def optimize(self):
		temp = self.dist()
		if sum(temp) == 0:
			while max(temp) - min(temp) > self.__length:
				a = max(temp) - self.__length
				b = min(temp) + self.__length
				temp[temp.index(max(temp))] = a
				temp[temp.index(min(temp))] = b

			current = self.__base_node
			for i in temp:
				current.spin = i
				current = current.next

	def step_counter(self):
		self.__steps = self.__steps + 1

	def next_node(self):
		self.__standing = self.__standing.next

	def prev_node(self):
		self.__standing = self.__standing.next

	def reset(self):
		self.__standing = self.__base_node

	def swap(self):
		if self.compare():
			p_1 = self.__standing
			p_2 = self.__standing.next
			p_1.next = p_2.next
			p_2.prev = p_1.prev
			p_1.prev.next = p_2
			p_2.next.prev = p_1
			p_1.prev = p_2
			p_2.next = p_1
			if p_1 == self.__base_node:
				self.__base_node = p_2
			elif p_2 == self.__base_node:
				self.__base_node = p_1
			self.step_counter()
			self.__pos_assign(0)
			self.__spin_assign()	

	#other
	'''
	def __set_base(self):
		current = self.__base_node
		for i in range(self.__length):
			if self.__base_node.val > current.val:
				self.__base_node = current
			self.__standing = self.__base_node
			current = current.next
	'''