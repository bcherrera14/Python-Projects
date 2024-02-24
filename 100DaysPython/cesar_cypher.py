alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encrypted_message = ""
    for letter in text:
        if letter.lower() in alphabet:
            index = alphabet.index(letter)
            shifted_index = index + shift
            if shifted_index <= len(alphabet) - 1:
                encrypted_message += alphabet[shifted_index]
            else:
                encrypted_message += alphabet[shifted_index - len(alphabet)]
        else:
            encrypted_message += letter
    print(encrypted_message)
            
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def decode(text, shift):
    message = ""
    for letter in text:
        if letter.lower() in alphabet:
            shifted_index = alphabet.index(letter)
            unshifted_index = shifted_index - shift
            if unshifted_index >= 0:
                message += alphabet[unshifted_index]
            else:
                message += alphabet[unshifted_index]
        else:
            message += letter
    print(message)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decode(text, shift)