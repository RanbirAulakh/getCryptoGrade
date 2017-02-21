# author: ranbir aulakh
# author: Kemoy Campbell

from Config import*
from RC4 import*
from Byte import*

from bs4 import BeautifulSoup
import requests, sys



def scrap_website(user):
	url = r"https://www.cs.rit.edu/~ark/462/grades/grades.php?user="+str(user)
	
	try:
		r = requests.get(url)

		#we get 404 or som other bad gateway code
		if r.status_code!=200:
			raise requests.exceptions.RequestException

		#otherwise return the request object
		return r
	except requests.exceptions.RequestException as e:  
		print("Webpage not avaiable. Cannot fetch ciphertext. Please check if the website is running and you are connected to the Internet")
		print e
		sys.exit(1)


def parsing_key_ciphertext(key,ciphertext):
	byte = Byte()

	#convert key
	key = byte.hexToByteArray(key)
	if(key==None or len(key)!=8):
		print("Key must not be empty or less than 8")
		print("fix your key in config")
		return 

	#convert ciphertext to hextoByteArray
	ct = byte.hexToByteArray(ciphertext)
	if(ct == None or len(ct) < 24):
		print("ct is  empty or less than 24")
		return

	# Get nonce (first 8 bytes of ciphertext), append key.
	nonce = ct[0:8]
	key = nonce+key

	return ct[8:len(ct)], key

def main():

	#get the config instance
	config = Config()

	scrap = scrap_website(config.getUserId())
	soup = BeautifulSoup(scrap.text, "html.parser")
	ciphertext = soup.find('input', {"name": "Ciphertext"})['value']

	if ciphertext:
		key = config.getKey()
		ciphertext,key = parsing_key_ciphertext(key,ciphertext)

		rc4 = RC4()

		rc4.set_key(key)

		for i in range( len(ciphertext) ):
			ciphertext[i]^=rc4.decrypt(i)

		#verify our key
		for i in range(20, 2):
			if(ciphertext[i] != ciphertext[i+1]):
				print("wrong key")
				return

		byte = Byte()
		print((byte.byteArrayToString(ciphertext[20:len(ciphertext)])).encode('utf-8'))

	elif ciphertext==None:
		print("We couldnt find any input text called ciphertext")
		print("Check to ensure you have the right website")
		return

	else:
		print("No grade to show at the moment")


main()