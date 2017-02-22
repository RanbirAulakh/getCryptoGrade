class Byte:

	def hexToByteArray(self,s):
		if( (len(s) % 2) !=0):
			return None

		length = int(len(s) / 2)

		buf = [None] * length

		for i in range(length):
			x = self.hexToNibble( s[2*i] )

			if(x == -1):
				return None

			y = self.hexToNibble( s[2*i+1] )
			if( y == -1):
				return None

			buf[i] = (x << 4 ) | y


		return buf


	def byteArrayToString(self,buf):
		if buf == None:
			return buf

		s = ""
		for i in range( len(buf) ):
			s += ''.join(chr(buf[i]))

		return s

	def hexToNibble(self,c):
		u = c.upper().strip()
		dic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

		if u in dic.keys():
			return int( dic[u] )

		return -1

