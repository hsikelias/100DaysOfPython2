from art import logo
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = "" 
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue
            
        if encode_or_decode == "decode":
            shift_amount = shift_amount * -1 
        
        original_position = alphabet.index(letter)
        new_position = (original_position + shift_amount) % 26
        output_text += alphabet[new_position]
    print(f"Your {encode_or_decode}d message is: {output_text}")

should_continue = True

while should_continue:
    direction = input('Type "encode" to encrypt or type "decode" to decrypt:\n').lower()
    text = input('Enter your text message here:\n').lower()
    shift = int(input('Type the shift number:\n'))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
