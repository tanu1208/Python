#!/usr/bin/env python
import sys
import os
from sys import argv

def countLine(f):
	file = open(f, "r", encoding='latin-1');
	lines = len(file.readlines());
	return lines;

def countWords(f):
	file = open(f, "r", encoding='latin-1');
	
	count = 0;
	for line in file:
		for word in line.split():
			count+=1;
	return count;

def countChar(f):
	file = open(f, "r", encoding='latin-1');
	count = 0;
	for line in file:
		for i in range(0, len(line)):
				count+=1;
	return count;

arg=len(argv);

if arg <= 1:
	print("File missing, pass the file to be read")
else:
	if arg > 2:
		arguments = argv[1:];

		totalLines=0;
		totalWord=0;
		totalChar=0;

		for filename in arguments:
			if os.path.isdir(filename):
				continue

			lineCount = countLine(filename);
			totalLines += lineCount;

			wordCount = countWords(filename);
			totalWord += wordCount;

			charCount = countChar(filename);
			totalChar += charCount;

			fileName = filename;
			print(" 	" + str(lineCount) + " 	" + str(wordCount) + " 	" + str(charCount) + " 	" + fileName);
		print(" 	" + str(totalLines) + " 	" + str(totalWord) + " 	" + str(totalChar) + " 	" + "total");

	else:
		argument = sys.argv[1];
		lineCount = countLine(argument);
		wordCount = countWords(argument);
		charCount = countChar(argument);
		fileName = argument;
		print(" 	" + str(lineCount) + " 	" + str(wordCount) + " 	" + str(charCount) + " 	" + fileName)
