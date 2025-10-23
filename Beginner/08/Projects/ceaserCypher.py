# How does the game work: 
'''
    A B C D E F G 
lets say we want to encode E, at the moment lets say shift is 1 so it becomes F.. so it changes based on the shift amount
  A B C D E F G H
'''

from art import logo

alphabet = ['a','b','c','d','e','f','g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input('Type "encode" to encrpt or type "decode" to decrypt:\n'.lower())
text = input('Enter your text message here:\n')
shift = int(input('Type the shift number: \n'))
choice = " "

def encrypt(original_text,shift_amount):
# Shifting each letter in original text by a certain shift amount a
# we got the alphabets list, what we can do is take the word in our word input by user, find its position in the list and add the shift amount to it, after getting the new letters in a list
# just join them back into a string. 
# i might have to convert stuff to list and join them back as a word. 
# print(logo)

    cipher_text = " "
    for letter in original_text:                                            # we are taking an indiviual letter from original text
        shifted_position = alphabet.index(letter) + shift_amount            # finding the position of it in the alphabet.. so maybe the 
                                                                            # og text is hello and our letter currently is h, so our position is 8
        cipher_text += alphabet(shifted_position % 26)                           # 8 gets added to whatever the shift amount is# we find the new letter for this old letter with help of alphabet and the 
                                                                            #index value we found.. we use modulo because
                                                                            # if you try to shift letter z it causes an index error.. 
                                                                            # #using modulo like 26%9 gives us reminder 8 which will be used as the index number                                    # finally to store the new letter somewhere cipher text exists
    print(f"The encrypted version of your message is{cipher_text}")
encrypt(original_text=text,shift_amount=shift)    


def decrypt(cipher_text,shift_amount):
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position % 26]
        cipher_text += new_letter

decrypt(cipher_text=cipher_text,shift_amount=shift)
    
