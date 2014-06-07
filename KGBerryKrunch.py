#  KGBerryKrunch
#  Not Your Average Cereal Box Cipher
#
#  Author: Ryan Kramlich

import sys

class KGBerryKrunch:

	letterArray = ['G', 'x', '6', 's', 'd', 'Y', 'W', 'U', 'e', 'f', 'n', 'H', 'Q', 'F', 'X', 'j', 'R', 
		'a', 'm', 'i', '7', 'Z', 'z', 'C', '9', 'h', 'V', 'T', 'I', 'D', '3', 'l', 'g', 'O', 'p', 't', 
		'y', '2', '4', 'E', 'K', '0', 'P', 'A', 'N', 'S', 'M', 'v', 'B', 'w', 'o', 'q', '1', 'L', 'J', 
		'8', 'u', 'k', 'b', 'r', '5', 'c']
	space_code = 'q34'
	manual = '''
	USAGE: python LibKGBerryKrunch.py [Operation] [Message] [Password]

	[Operation] - E for Encrypt, D for decrypt.

	[Message] - Depending on operation, message to be encoded or encoded message.
	(If the message is more than 1 word, put it in quotes)

	[Password] - Password
	'''

	final_phrase = ''
	#  Methods

	def __init__(self, in_option1, in_phrase, in_key):
		#check_params()
		option1 = in_option1
		option1 = option1.upper()
		phrase = in_phrase
		key = in_key

		if option1 == 'E':
			phrase = self.cleanse(phrase)
			phrase = phrase.replace(' ',self.space_code)
			key2 = self.cleanse(key)
			if key != key2:
				print 'Invalid password. Letters and numbers only.'
				sys.exit()
			self.encrypt(phrase,key)
		else:
			self.decrypt(phrase,key)

	def get_result(self):
		return self.final_phrase

	def check_params(self):
		if len(sys.argv) != 4:
			print self.manual
			sys.exit()
		if sys.argv[1] != 'E' and sys.argv[1] != 'D':
			print self.manual
			sys.exit()
		if sys.argv[1] == 'D' and ' ' in sys.argv[2]:
			print self.manual
			sys.exit()

	def cleanse(self, phrase):
		phrase = phrase.replace('&','')
		phrase = phrase.replace('/','')
		phrase = phrase.replace('*','')
		phrase = phrase.replace('_','')
		phrase = phrase.replace('?','')
		phrase = phrase.replace('!','')
		phrase = phrase.replace(',','')
		phrase = phrase.replace('.','')
		return phrase

	def encrypt(self, phrase, key):
		finalPhrase = ''
		finalPhrase_dashes = ''
		keyLength = len(key)
		for i in range(len(phrase)):
			finalPhrase += self.addLetters(phrase[i], key[i%keyLength])
		finalPhrase_dashes = '-'.join(finalPhrase[i:i+4] for i in range(0, len(finalPhrase), 4))
		# for i in range(len(finalPhrase)):
		# 	finalPhrase_dashes += finalPhrase[i]
		# 	if i != 0 and i+1 % 4 == 0:
		# 		finalPhrase_dashes += '-'
		if finalPhrase_dashes[len(finalPhrase_dashes) - 1] == '-':
			finalPhrase_dashes = finalPhrase_dashes[:len(finalPhrase_dashes) - 1]
		self.final_phrase = finalPhrase_dashes
		return finalPhrase_dashes

	def decrypt(self, phrase, key):
		phrase = phrase.replace('-','')
		phrase = phrase.replace(' ','')
		finalPhrase = ''
		keyLength = len(key)
		for i in range(len(phrase)):
			finalPhrase += self.subtractLetters(phrase[i], key[i%keyLength])
		finalPhrase = finalPhrase.replace(self.space_code,' ')
		self.final_phrase = finalPhrase
		return finalPhrase

	def addLetters(self, a, b):
		abSum = self.letterArray.index(a) + self.letterArray.index(b)
		sumLetter = self.letterArray[abSum % len(self.letterArray)]
		return sumLetter

	def subtractLetters(self, a, b):
		if self.letterArray.index(a) > self.letterArray.index(b):
			abDiff = self.letterArray.index(a) - self.letterArray.index(b)
		else:
			abDiff = len(self.letterArray) - (self.letterArray.index(b) - self.letterArray.index(a))
		diffLetter = self.letterArray[abDiff % len(self.letterArray)]
		return diffLetter

if __name__ == '__main__':
	main()