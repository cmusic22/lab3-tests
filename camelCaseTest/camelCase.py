def camelcase(sentence):
	#punctuations variable
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	#what to replace punctuations with
	no_punct = ''
	for char in sentence:
		if char not in punctuations:
			no_punct = no_punct + char
			
	""" Convert sentence to camelCase, for example, "Display all books" 
	is converted to "displayAllBooks" """
	title_case = no_punct.title() # Uppercase first letter of each word 
	upper_camel_cased = title_case.replace(' ', '') # remove spaces

	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, strings of length 1
	return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def display_banner():
	"""Display program name in banner"""
	msg = 'AWSOME comelCaseGenerator PROGRAM'
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n')

def display_instructions():
	msg = "Enter a sentence and we will convert it into camelCase"
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n')

def main():
	display_banner()
	display_instructions()
	sentence = input('Enter your sentence: ')
	output = camelcase(sentence)
	print(output)

if __name__ == '__main__':
	main()
