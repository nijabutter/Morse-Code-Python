import sys
import os

# morse to text and vice versa dictionaries
m={
	'a':".-",
	'b':"-...",
	'c':"-.-.",
	'd':"-..",
	'e':".",
	'f':"..-.",
	'g':"--.",
	'h':"....",
	'i':"..",
	'j':".---",
	'k':"-.-",
	'l':".-..",
	'm':"--",
	'n':"-.",
	'o':"---",
	'p':".--.",
	'q':"--.-",
	'r':".-.",
	's':"...",
	't':"-",
	'u':"..-",
	'v':"...-",
	'w':".--",
	'x':"-..-",
	'y':"-.--",
	'z':"--..",
	'A':".-",
	'B':"-...",
	'C':"-.-.",
	'D':"-..",
	'E':".",
	'F':"..-.",
	'G':"--.",
	'H':"....",
	'I':"..",
	'J':".---",
	'K':"-.-",
	'L':".-..",
	'M':"--",
	'N':"-.",
	'O':"---",
	'P':".--.",
	'Q':"--.-",
	'R':".-.",
	'S':"...",
	'T':"-",
	'U':"..-",
	'V':"...-",
	'W':".--",
	'X':"-..-",
	'Y':"-.--",
	'Z':"--..",
	'1':".----",
	'2':"..---",
	'3':"...--",
	'4':"....-",
	'5':".....",
	'6':"-....",
	'7':"--...",
	'8':"---..",
	'9':"----.",
	'0':"-----",
	'!':"-.-.--",
	'?':"..--..",
	'.':".-.-.-",
	',':"--..--",
	'\'':".----.",
	'"':".-..-.",
	'(':"-.--.",
	')':"-.--.-",
	'-':"-....-",
	'=':"-...-",
	'+':".-.-.",
	'/':"-..-."
}
md={
	'.-':"a",
	'-...':"b",
	'-.-.':"c",
	'-..':"d",
	'.':"e",
	'..-.':"f",
	'--.':"g",
	'....':"h",
	'..':"i",
	'.---':"j",
	'-.-':"k",
	'.-..':"l",
	'--':"m",
	'-.':"n",
	'---':"o",
	'.--.':"p",
	'--.-':"q",
	'.-.':"r",
	'...':"s",
	'-':"t",
	'..-':"u",
	'...-':"v",
	'.--':"w",
	'-..-':"x",
	'-.--':"y",
	'--..':"z",
	'.-':"A",
	'-...':"B",
	'-.-.':"C",
	'-..':"D",
	'.':"E",
	'..-.':"F",
	'--.':"G",
	'....':"H",
	'..':"I",
	'.---':"J",
	'-.-':"K",
	'.-..':"L",
	'--':"M",
	'-.':"N",
	'---':"O",
	'.--.':"P",
	'--.-':"Q",
	'.-.':"R",
	'...':"S",
	'-':"T",
	'..-':"U",
	'...-':"V",
	'.--':"W",
	'-..-':"X",
	'-.--':"Y",
	'--..':"Z",
	'.----':"1",
	'..---':"2",
	'...--':"3",
	'....-':"4",
	'.....':"5",
	'-....':"6",
	'--...':"7",
	'---..':"8",
	'----.':"9",
	'-----':"0",
	'-.-.--':"!",
	'..--..':"?",
	'.-.-.-':".",
	'--..--':",",
	'.----.':"'",
	'.-..-.':"\"",
	'-.--.':"(",
	'-.--.-':")",
	'-....-':"-",
	'-...-':"=",
	'.-.-.':"+",
	'-..-.':"/"
}



doDecode = False
ignoreBad = False
ignoreChar = '?'
spaceChar = '/'


msg = []

def encode(msg):
	morse = ""
	for e, l in enumerate(msg):
		for j, i in enumerate(l):

			if i=='\n':
				morse += '\n'
			elif i == ' ':
				morse += spaceChar + ' '
			elif i not in m:
				morse += ignoreChar + " "
			else:
				morse += m[i] + " "
	print(morse)

def decode(msg, isFile):
	decoded = ""
	for l in msg:
		for j, i in enumerate(l.split()):
			if i == spaceChar:
				decoded += ' '
			elif i not in md:
				decoded += ignoreChar
			else:
				decoded += md[i]

	print(decoded)

def showHelp():
	print("\nUsage: morse [-d] [-i_character] text/file")
	print("Example: morse -i# Path/To/File/encode_me.txt")
	print("\nOptions:")
	print("%*s %*s" % (6, "-d", 74, "Decode from morse code to text. Decoded letters will be capitalised\n"))
	print("%*s %*s" % (6, "-i[character]", 74, "Specify custom character immediately after to repleace unrecognized characters."))
	print("%*s" %(58, "Default is '?'. Use -i to ignore completely.\n"))


if (len(sys.argv) == 1):
	showHelp()
	exit(0)

for j, i in enumerate(sys.argv):
	if i == "-h":
		showHelp()
		exit(0)
	elif j==len(sys.argv)-1:
		msg = i
	elif i == "-d":
		doDecode = True
	elif i.startswith("-i"):
		ignoreChar = i.replace('-i', '')
		ignoreBad = True


if doDecode:
	if os.path.exists(msg):
		isFile = True
		with open(msg) as f:
			msg = f.readlines()
	else:
		msg = msg.split()
		isFile=False
	decode(msg, isFile)
else:

	if os.path.exists(msg):
		with open(msg, 'r') as f:
			msg = []
			for i in f.readlines():
				msg.append(i)
	encode(msg)



