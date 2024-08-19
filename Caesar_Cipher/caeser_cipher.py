letters = 'abcdefghijklmnopqrstuvwxyz'

def decrypt_message(message):
	new_message = ''
	keys = range(1, 27)
	for k in keys:
		for letter in message:
			i = letters.find(letter.lower())
			if i == -1:
				new_message += ' '
			else:
				new_i = (i - k) % 26
				new_l = letters[new_i]
				new_message += new_l
		print(new_message)
		new_message = ''
		


def encrypt_message(message, key):
	for letter in message:
		index = letters.find(letter.lower())
		if index == -1:
			print(" ", end='')
			continue
		else:
			new_index = (index + key) % 26
			new_letter = letters[new_index]
			print(new_letter, end='')

#encrypt_message("hello", 4)