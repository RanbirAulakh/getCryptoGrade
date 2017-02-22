# getCryptoGrade

Requirements:
- Python2.7 +
- beautifulsoup4
- requests
- your userId + key

Where to find your userId? 
- go to https://www.cs.rit.edu/~ark/462/encryptedgrades.shtml and find your username,
click on it and in the URL, you will see your userID
ex) https://www.cs.rit.edu/~ark/462/grades/grades.php?user=##

#####Test the code:
To test the software, leave it as it is and just run. It uses the default user 0 and the key
found for the example user as found on https://cs.rit.edu/~ark/462/encryptedgrades.shtml in the example 
grade file section

#####Fetch your own grade:
This software is designed to work for all sections/classes that are taught by professor Alan Kaminsky 
To fetch your own grades go to  Config.py and edit your userid and key and course number. Professor Alan website is in the format
https://cs.rit.edu/~ark/##courseNumber. That is the number you should put in the config

#####How to run:
$ python getCryptoGrade.py

