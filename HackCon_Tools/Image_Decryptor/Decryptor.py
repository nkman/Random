# ------ ----- ------- #
# Date - 2 March 2014
# Time - 5:40 PM
# Author - NKMAN
# It decrypts the encripted Image by Brute Force algorithm.
# ------ ----- ------- #

import sys

def remove(message):			#Remove """ , . ' ; " < > / ? ] [ { } | \ = - _ + * & ^ % $ # 2 ! """#
	q = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ \t\n'
	f = ''
	message = message.upper()
	for t in message:
		if t in q:
			f = f + t
	return f.split()

def DictionaryLoader():
	f = open('dictionary.txt','r')
	words = []
	for t in f.read().split('\n'):
		words.append(t)
	f.close()
	return words

def CountWords(message):
	#First remove the special characters
	wordList = remove(message)

	#If Null then abort
	if wordList == []:
		return 0

	#No of matching word initially = 0
	count = 0

	#Load the Dictionary
	wo = DictionaryLoader()

	#Check How many words are English word in message
	for t in wordList:
		if t in wo:
			#If found increase the number of words encountered
			count += 1

	#Return total fraction of english words in message
	return float(count)/len(wordList)

#<No_Brute>#
def ReturnBinary():
	f = open('Workspace.bmp','rb')
	f.read(100)

	byte = f.read(1)
	l = []
	l.append(str(ord(byte)%2))

	while byte != "":
		byte = f.read(3)
		try:
			l.append(str(ord(byte[2])%2))
		except IndexError:
			pass
	f = open('Intermediate.txt','w')
	f.write(''.join(l))

def Text():				#Text from Binary
	ReturnBinary()
	f = open('Intermediate.txt','r')
	l = []
	size = len(f.read())
	f.close()

	f = open('Intermediate.txt','r')
	i = 0
	while (i<size):
		r = int(str(f.read(8)),2)
		l.append(chr(r))
		i += 8

	h = ''
	for t in l:
		h = h + str(t)
	print h

#</No_Brute>#

def BruteBinary(i):

	#Open the file in binary mode.
	f = open('Workspace.bmp','rb')

	#initialize list to zero currently, ie an Empty list.
	l = []

	#Start reading the file from the very first byte.
	byte = f.read(i)

	#Until the end of document.
	while byte != "":

		#read the i'th character(Or whatever is that)
		

		#If possible then get the binary last of the least significant digit/character.
		try:
			#ord --> ASCII of that character
			#str --> list is of string type, so it is necessary to convert integer to a string.
			decimal = ord(byte[i-1])
			remainder = decimal%2
			string_ = str(remainder)
			l.append(string_)  #assuming least significant polluted.
		
		except IndexError:
			"""
			f = open('Intermediate.txt','w')
			f.write(''.join(l))
			return 1
			"""
			pass
		byte = f.read(i)
	f.close()
	#Open the intermediate file to write the binary form obtained.
	qw = open('Intermediate.txt','w')

	#Write in this file
	qw.write(''.join(l))

	#Close the file.
	qw.close()
	#print ''.join(l)
	#Anyway loop is going to terminate here.
	return 1

def BruteText(i):				#Text from Binary
	
	sys.stdout.write('Trying with %s\n' % str(i)) 
	#Write the file i. e. Intermediate.txt which contains the binary form of chars
	BruteBinary(i)

	#Now since the file Intermediate.txt is being written, it is available to be read.
	f = open('Intermediate.txt','r')

	#Total size of that file.
	size = len(f.read())

	#Close the file.
	f.close()

	l = []
	f = open('Intermediate.txt','r')
	i = 0
	while (i<size):
		#Take first 8-bits and convert it to decimal.
		r = int(str(f.read(8)),2)

		#Get the character representing that decimal number.
		l.append(chr(r))

		#Increment i by 8 to read another 8-digit pair.
		i += 8

	h = ''
	for t in l:
		h = h + str(t)
	return h

def GetSize():
	f = open('Workspace.bmp','rb')
	t = len(f.read())
	f.close()
	return t

def Worker():
	size = GetSize()
	for i in range(0,size):
		if (CountWords(BruteText(i))>0.2):
			print BruteText(i)
			t = raw_input()
			pass
def main():
	Worker()
if __name__ == '__main__':
	main()