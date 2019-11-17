#!/usr/bin/env python3
import argparse


def parse_arguments():
    """
    Parse commandline arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Usage: python3 my_diff.py <original_file> <modified_file>')

    # Set up arguments
    parser.add_argument('original_file', type=str,
                        help='The original file')

    parser.add_argument('modified_file', type=str,
                        help='The modified file')

    args = parser.parse_args()
    return args


def diff_check(orig_file, mod_file):
	"""
	Method for comparing and differentiating the original file
	from the modified file. Returning output as a variable.
	:param orig_file: The original text file
	:param mod_file: The file that has been modified
	:return:
	"""

	output = ""
	original_file = orig_file.split("\n")
	modified_file = mod_file.split("\n")

	# making two iterators that aggregates elements from each of the files
	for orig_line, mod_line in zip(original_file, modified_file):
		if orig_line == mod_line:
			output = output + " 0 " + orig_line + "\n"

		# Adds a - in the beginning of the line if a line has been deleted
		elif orig_line != mod_line and mod_line == "":
			output = output + " - " + orig_line + "\n"

		# Adds a + in the beginning of the line if a line has been added
		elif orig_line == "":
			output = output + " + " + mod_line + "\n"

		# If a line has been modified, treat as a deletion, then an addition
		elif orig_line != mod_line:
			output = output + " - " + orig_line + "\n"
			output = output + " + " + mod_line + "\n"

	return output


def write_to_file(output_text):
	"""
	Method for writing the lines to the output file.
	Will write the file to 'diff_output.txt'
	:param output_text: The result string from the diff_check function
	:return:
	"""

	filename = "diff_output.txt"
	with open(filename, 'w') as file:
		file.write(output_text)


if __name__ == '__main__':
	# Parse arguments from command line
	args = parse_arguments()

	# open and read the files
	with open(args.original_file) as original_file, open(args.modified_file) as modified_file:
		original_file = original_file.read()
		modified_file = modified_file.read()

	# Execute diff utility check
	output = diff_check(original_file, modified_file)

	# Print the result and write to a file
	print(output)
	write_to_file(output)
