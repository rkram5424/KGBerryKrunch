#  KGBerryKrunch
#  Not Your Average Cereal Box Cipher
#
#  Author: Ryan Kramlich
#  I am writing this in python so that I may easily translate it into Objective-C for my iPhone project.
#  If you are fortunate enough for me to share this code with you, then I probably trust you as this is a secret algorithm of mine ;)
#

#  imports and globals

import getpass
letterArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
	'n','o','p','q','r','s','t','u','v','w','x','y','z','-','0',
	'1','2','3','4','5','6','7','8','9']

#  Methods

def main():
	option1 = raw_input('Encrypting or Decrypting? (E or D): ')
	option1 = option1.upper()

	if option1 == 'E':
		phrase = raw_input('Message to encrypt (no symbols or punctuation): ')
		key = getpass.getpass('Passphrase: (no symbols or punctuation): ')
	else:
		phrase = raw_input('Message to decrypt (as is): ')
		key = getpass.getpass('Passphrase: ')

	phrase = phrase.lower()
	key = key.lower()

	if option1 == 'E':
		phrase = phrase.replace('&','')
		phrase = phrase.replace('\'','')
		phrase = phrase.replace('*','')
		phrase = phrase.replace('_','')
		phrase = phrase.replace('?','')
		phrase = phrase.replace('!','')
		phrase = phrase.replace(',','')
		phrase = phrase.replace('.','')
		phrase = phrase.replace(' ','-')
		print encrypt(phrase,key)
	else:
		print decrypt(phrase,key)

def encrypt(phrase,key):
	finalPhrase = ''
	keyLength = len(key)
	for i in range(len(phrase)):
		finalPhrase += addLetters(phrase[i], key[i%keyLength])

	return finalPhrase

def addLetters(a,b):
	abSum = letterArray.index(a) + letterArray.index(b)
	sumLetter = letterArray[abSum % 37]
	return sumLetter

def decrypt(phrase,key):
	finalPhrase = ''
	keyLength = len(key)
	for i in range(len(phrase)):
		finalPhrase += subtractLetters(phrase[i], key[i%keyLength])
	finalPhrase = finalPhrase.replace('-',' ')
	return finalPhrase

def subtractLetters(a,b):
	if letterArray.index(a) > letterArray.index(b):
		abDiff = letterArray.index(a) - letterArray.index(b)
	else:
		abDiff = 37 - (letterArray.index(b) - letterArray.index(a))
	diffLetter = letterArray[abDiff % 37]
	return diffLetter

if __name__ == '__main__':
	main()