import os

def list_files():
	top = os.getcwd()
	for root, dirs, files in os.walk(top):
		level = root.replace(top, '').count(os.sep)
		indent = ' ' * 4 * (level)
		if '.git' in root:
			continue

		print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			if '.DS_Store' in f:
				continue

			print('{}{}'.format(subindent, f))

if __name__ == "__main__":
	list_files();