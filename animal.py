import sys

def default():
	print('Hello')
def dog():
	print('Guau')


def cat():
	print('Miauuu')

def main(): 

	if sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == 'dog':
		dog()
	else:
		default()


if __name__ == '__main__':
	main()


