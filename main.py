#!python3

import sys

def adjusted_key(text, key):
  # Concatenates the key to the approximate length of the text. 
  adjusted_key = key * int((len(text)/len(key)))

  # Adds the rest at the end and returns.
  adjusted_key += key[0:int((len(text) % len(key)))]
  return adjusted_key

def encryptVignere():
  input_file = input("Enter the name of the file to be encrypted: ")
  input_key = input("Enter the encryption key: ")
  output_file = input("Enter the name of the file to be exported: ")

  cipherfile = open(input_file)
  input_text = str(open(input_file).read()).lower()

  output_key = adjusted_key(input_text, input_key)
  output_text = ''

  for text_char, key_char in zip(input_text, output_key):
    output_text += encrypt_char(text_char, key_char)
  
  print("The file ", input_file, " has been encrypted.")

  with open(output_file, 'w') as export_file:
    export_file.write(output_text)
  
  print("The file ", output_file, " has been exported.")

  cipherfile.close()
  export_file.close()

def encrypt_char(text_char, key_char):
  if text_char.isalpha() == True:
    # Find the relevant ords.
    first_letter_ord = ord('a')
    text_char_ord = ord(text_char)
    key_char_ord = ord(key_char)

    # Calculate the amount to shift by.
    text_shift = text_char_ord - first_letter_ord
    key_shift = key_char_ord - first_letter_ord

    # Shift and encrypt the character.
    encrypted_char = chr(((text_shift + key_shift) % 26) + first_letter_ord)
    return encrypted_char
  else:
    # If it's not a letter, return the character.
    return text_char

def decryptVignere():
  input_file = input("Enter the name of the file to be encrypted: ")
  input_key = input("Enter the encryption key: ")
  output_file = input("Enter the name of the file to be exported: ")

  cipherfile = open(input_file)
  input_text = str(open(input_file).read()).lower()

  output_key = adjusted_key(input_text, input_key)
  output_text = ''

  for text_char, key_char in zip(input_text, output_key):
    output_text += decrypt_char(text_char, key_char)
  
  print("The file ", input_file, " has been decrypted.")

  with open(output_file, 'w') as export_file:
    export_file.write(output_text)
  
  print("The file ", output_file, " has been exported.")

  cipherfile.close()
  export_file.close()

def decrypt_char(text_char, key_char):
  if text_char.isalpha() == True:
    # Find the relevant ords.
    first_letter_ord = ord('a')
    text_char_ord = ord(text_char)
    key_char_ord = ord(key_char)

    # Calculate the amount to shift by.
    text_shift = text_char_ord - first_letter_ord
    key_shift = key_char_ord - first_letter_ord

    # Shift and encrypt the character.
    decrypted_char = chr(((text_shift - key_shift + 26) % 26) + first_letter_ord)
    return decrypted_char
  else:
    # If it's not a letter, return the character.
    return text_char

def menu():
  option = int(input("\nSelect an operation: \n 1) Encrypt Text \n 2) Decrypt Text \n 9) Quit \n:"))
  return option

def main():
  while True:
    operation = menu()
    if operation == 1:
      encryptVignere()
    elif operation == 2:
      decryptVignere()
    elif operation == 9:
      print('Exiting the program.')
      sys.exit(1)
    else:
      print('Invalid option. Try again.')

main()

#if __name__ == "__main__":
#  encryptVignere()
