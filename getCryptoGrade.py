# author: ranbir aulakh

from bs4 import BeautifulSoup
import requests

def decrypt(key, ciphertext):
	key = hexToByteArray(key)
	if(key == None or len(key) != 8):
		print("Key is empty... Or more than 8")
		return

	ct = hexToByteArray(ciphertext)
	if(ct == None or len(ct) < 24):
		print("ct is empty... Or less than 24")
		return

	nonce = ct[0:8]
	noncePlusKey = nonce + key

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


	for i in range(8, len(ct)):
		x = (x + 1) & 255

		y = (y + S[x]) & 255
		
		t = S[x];
		S[x] = S[y]
		S[y] = t;

		ct[i] ^= S[(S[x] + S[y]) & 255]

	for i in range(8, 24, 2):
		if(ct[i] != ct[i+1]):
			print("wrong key")
			return

	print((byteArrayToString(ct[24:len(ct)])).encode('utf-8'))

def hexToByteArray(s):
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
	s = "";
	for i in range(0, len(buf)):
		s += ''.join(map(unichr, [buf[i]]))
	return s

def hexToNibble(c):
	u = c.upper()
	if(u == "0"):
		return 0
	elif (u == "1"):
		return 1
	elif (u == "2"):
		return 2
	elif (u == "3"):
		return 3
	elif (u == "4"):
		return 4
	elif (u == "5"):
		return 5
	elif (u == "6"):
		return 6
	elif (u == "7"):
		return 7
	elif (u == "8"):
		return 8
	elif (u == "9"):
		return 9
	elif (u == "A"):
		return 10
	elif (u == "B"):
		return 11
	elif (u == "C"):
		return 12
	elif (u == "D"):
		return 13
	elif (u == "E"):
		return 14
	elif (u == "F"):
		return 15
	else:
		return -1

def main():
	# go to https://www.cs.rit.edu/~ark/462/encryptedgrades.shtml and find your username,
	# click on it and in the URL, you will see your userID
	userId = "YOUR USER ID GOES HERE" 
	url = r"https://www.cs.rit.edu/~ark/462/grades/grades.php?user=" + str(userId)
	key = "YOUR KEY GOES HERE"

	r  = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data, "html.parser")

	ciphertext = soup.find('input', {"name": "Ciphertext"})['value']

	decrypt(key, ciphertext)

main()

