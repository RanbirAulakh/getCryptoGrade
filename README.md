## getCryptoGrade

This software is designed to work for all sections/classes that are taught by professor Alan Kaminsky. To fetch your own grades go to Config.py and edit your userid and key and course number. It is compatiable with Mac OS, Linux, & Windows


### Requirements

* Python 2.7+
* Beautifulsoup4 and requests library
* Be in Alan's class


###Manual Installation

* Required Python Libraries

		$ pip install beautifulsoup4

		$ pip install requests
		
* In `Config.py`, 

	- userId --- go to Alan's Encrypted Grades website, find your username, click on it, and in the URL, you will see your userID. For example: [https://www.cs.rit.edu/~ark/462/grades/grades.php?user=##](https://www.cs.rit.edu/~ark/462/grades/grades.php?user=##)
	
	- key --- encryped key that was provided in class

	- course number --- just the course number, do not need section number

	
### How to Run

There are two ways to run this program. One is by python and other one is by bash script.

1. Go to `getCryptoGrade` folder you just cloned/downloaded it.
2. `$ python getCryptoGrade.py`

OR

1. Create a folder, `getCryptoGrade` in:
	- `~/bin` (If you do not have that folder, you can make directory `mkdir ~/bin`)
	- Inside that folder, copy all `*.py` files
2. Copy `getCryptoGrade.sh` to the root directory of `~/bin`
3. Then execute `$ getCryptoGrade.sh `
	* If returning an error due to permission. Then do `chmod 755 getCryptoGrade.sh`
	
	
### Test the code:
To test the software, leave it as it is and just run. It uses the default user 0 and the key
found for the example user as found on https://cs.rit.edu/~ark/462/encryptedgrades.shtml in the example 
grade file section


### License
This project is under MIT License. Copy of the license is in this repo.