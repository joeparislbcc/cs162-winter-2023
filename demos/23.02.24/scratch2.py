from string import ascii_lowercase

rotation = 17

text_from_textbox = ascii_lowercase

cipher_alphabet = text_from_textbox[rotation:] + text_from_textbox[:rotation]

print(cipher_alphabet)
