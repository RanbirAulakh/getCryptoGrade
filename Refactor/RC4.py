class RC4:
	S = [None] * 256
	byte_to_int_mask = 255
	max_key = 16
	x = 0
	y = 0

	def set_key(self,key,offset=0):

		if key is None or len(key) < self.max_key:
			raise ValueError("Key length must be "+str(self.max_key))

		#initalizing the S arrays
		for i in range(256):
			self.S[i] = i

		#swapping around/mixing
		j = 0
		for i in range(256):
			j = (j + self.S[i] + key[i & 15 + offset]) & self.byte_to_int_mask
			self.swap(i,j)

	def swap(self,i,j):
		t = self.S[i]
		self.S[i] = self.S[j]
		self.S[j] = t

	def encrypt(self,b):
		return self.encryptOrDecrypt(b)

	def decrypt(self,b):
		return self.encryptOrDecrypt(b)


	def encryptOrDecrypt(self,b):
		self.x = (self.x + 1) & self.byte_to_int_mask
		self.y = (self.y + self.S[self.x]) & self.byte_to_int_mask

		self.swap(self.x,self.y)

		return self.S[(self.S[self.x] + self.S[self.y]) & self.byte_to_int_mask]



