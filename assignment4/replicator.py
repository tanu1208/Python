#!/usr/bin/env python
import os
from sys import argv

def repeat_bad(word):
	#just a longer method compared to the other, but I believe the run time would be the same
	i=0;
	output="";
	for letter in word:
		if letter == word[0]:
			output=letter.upper();
			i+=1;
		elif letter == word[i]:
			firstLetter = letter.upper();
			secondLetter = (letter.lower() * i);
			output2 = "-" + firstLetter + secondLetter;
			output += output2
			i+=1;

	return output;

def repeat_good(word):
	output = "";
	for i, c in enumerate(word):
		if c == word[0]:
			output = c.upper();
		elif c == word[i]:
			output += ("-" + c.upper() + (c.lower()*i));

	return output;

if len(argv) < 2:
	print("Missing input");
else:
	if len(argv) == 2:
		arguments = argv[1];

		good = repeat_good(arguments);
		bad = repeat_bad(arguments);

		print("Good: " + good);
		print("Bad: " + bad);
	else:
		print("To many arguments, it can only take 1 word");