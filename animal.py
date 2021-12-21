import sys

def default():
	print('Hello')
def dog():
	print('Guau')


def main(): 
	if sys.argv[1] == 'dog':
		dog()
	else:
		default()

if __name__ == '__main__':
	main()


