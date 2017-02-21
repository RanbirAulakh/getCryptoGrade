# author: ranbir aulakh

from bs4 import BeautifulSoup
import requests, sys

def decrypt(key, ciphertext):
	"""
	Decrypt with provided ciphertext and key
	Prints out your grade and other important information
	"""

	# get key
	key = hexToByteArray(key)
	if(key == None or len(key) != 8):
		print("Key is empty... Or more than 8")
		return

	# get ciphertext
	ct = hexToByteArray(ciphertext)
	if(ct == None or len(ct) < 24):
		print("ct is empty... Or less than 24")
		return

	# Get nonce (first 8 bytes of ciphertext), append key.
	nonce = ct[0:8]
	noncePlusKey = nonce + key


	# Initialize RC4 keystream generator.
	S = [None] * 256
	for i in range(0, 256):
		S[i] = i

	j = 0
	for i in range(0, 256):
		j = (j + S[i] + noncePlusKey[i & 15]) & 255
		t = S[i]
		S[i] = S[j]
		S[j] = t

	x = 0
	y = 0


	# Decrypt ciphertext, omitting nonce.
	for i in range(8, len(ct)):
		x = (x + 1) & 255

		y = (y + S[x]) & 255
		
		t = S[x];
		S[x] = S[y]
		S[y] = t;

		ct[i] ^= S[(S[x] + S[y]) & 255]


	# Check key verification string.
	for i in range(8, 24, 2):
		if(ct[i] != ct[i+1]):
			print("wrong key")
			return

	# display plaintext
	print((byteArrayToString(ct[24:len(ct)])).encode('utf-8'))


def hexToByteArray(s):
	"""
	Converts Hex to Byte Array
	"""
	if( (len(s) % 2 ) != 0):
		return None

	length = len(s) / 2
	buf = [None] * length

	for i in range(0, length):
		x = hexToNibble( s[2*i] )
		if(x == -1):
			return None

		y = hexToNibble( s[2*i+1] )
		if(y == -1):
			return None

		buf[i] = (x << 4) | y

	return buf

def byteArrayToString(buf):
	"""
	Converts Byte Array To String
	"""
	s = "";
	for i in range(0, len(buf)):
		s += ''.join(map(unichr, [buf[i]]))
	return s

def hexToNibble(c):
	"""
	Converts Hex to Nibble
	"""
	u = c.upper().strip()
	dic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
	if(u in dic.keys()):
		return int(dic[u])
	else:
		return -1

def main():
	"""
	1. Gets URL, userId, and key
	2. Check if page is LIVE, then get ciphertext
	3. Execute decrypt function
	"""

	# go to https://www.cs.rit.edu/~ark/462/encryptedgrades.shtml and find your username,
	# click on it and in the URL, you will see your userID
	userId = "YOUR USER ID GOES HERE" 
	url = r"https://www.cs.rit.edu/~ark/462/grades/grades.php?user=" + str(userId)
	key = "YOUR KEY GOES HERE"

	# check if website is live and running
	try:
		r = requests.get(url)
	except requests.exceptions.RequestException as e:  # website is not live
		print("Webpage not avaiable. Cannot fetch ciphertext. Please check if the website is running and you are connected to the Internet")
		print e
		sys.exit(1)


	# go to URL
	r  = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data, "html.parser")

	# get ciphertext
	ciphertext = soup.find('input', {"name": "Ciphertext"})['value']

	decrypt(key, ciphertext) # go to decrypt function

main()

