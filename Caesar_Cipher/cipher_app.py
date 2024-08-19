import tkinter as Tk
from tkinter import *
#from PIL import ImageTk,Image 

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_message():
	'''
    This function retrieves the message input and uses the key entered to encrypt the message using a shift cipher
	and renders it in the app.


    Parameters
    -----------
    None

    Return
    ------
    None
    '''

	key_entered = int(key.get())
	message_entered = message.get(0.0, 'end')
	enc_msg = ''
	for letter in message_entered:
		index = letters.find(letter.lower())
		if index == -1:
			enc_msg += " "
			continue
		else:
			new_index = (index + key_entered) % 26
			new_letter = letters[new_index]
			enc_msg += new_letter
		output.delete(0.0, 'end')
		key.delete(0, 'end')
		output.insert('end', enc_msg)

def decrypt_message():
	'''
    This function retrieves the message input and applies every combination possible for a shift cipher and returns the results to the output box.


    Parameters
    -----------
    None

    Return
    ------
    None
    '''

	
	message_entered = message.get(0.0, 'end')
	dec_msg = ''
	output.delete(0.0, 'end')
	keys = range(1, 27)
	for k in keys:
		for letter in message_entered:
			i = letters.find(letter.lower())
			if i == -1:
				dec_msg += ' '
			else:
				new_i = (i - k) % 26
				new_l = letters[new_i]
				dec_msg += new_l
		output.insert('end', f"{dec_msg}\n")
		dec_msg = ''



window = Tk()
window.title("Cipher")
window.geometry('500x1000')
window.configure(background = 'black')

frame_1 = Frame(window, bg = 'black')
frame_1.pack()
frame_2 = Frame(window, bg = 'black')
frame_2.pack()

# img = ImageTk.PhotoImage(Image.open('mask.jpg'))
# label_img = Label(frame_1, image = img, bg = 'black')
# label_img.pack()


lbl = Label(frame_1, bg = 'black', fg = 'white', text = "Input message to be encrypted/decrypted:\n", font = (25))
lbl.pack()

lbl_2 = Label(frame_2, text = "\nOutput:", bg = 'black', fg = 'white', font = (50))
lbl_2.pack()

message = Text(frame_1, width = 65, height = 10)
message.pack()

cipher_selected = StringVar(value='caeser')

select_caeser = Radiobutton(frame_1, value="caesar", text="caesar", variable=cipher_selected)
select_caeser.pack()
select_transposition = Radiobutton(frame_1, value="transposition", text="Transposition", variable=cipher_selected, state='disabled')
select_transposition.pack()

lbl_3 = Label(frame_1, bg = 'black', fg = 'white', text = "Key:")
lbl_3.pack()


key = Entry(frame_1, width = 3)
key.pack()

btn_1 = Button(frame_1, text = "Encrypt", bg = "green", fg = "black", command = encrypt_message)
btn_1.pack()
btn_2 = Button(frame_1, text = "Decrypt", bg = 'red', fg = 'black', command = decrypt_message)
btn_2.pack()

output = Text(frame_2, width = 65, height = 26)
output.pack()

window.mainloop()