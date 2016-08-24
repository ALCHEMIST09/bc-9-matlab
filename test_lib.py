from __future__ import unicode_literals
from prompt_toolkit import prompt

def main():

	text = prompt('Give me some input: ')
	print('You said: %s' % text)
	
if __name__ == '__main__':
	main()

