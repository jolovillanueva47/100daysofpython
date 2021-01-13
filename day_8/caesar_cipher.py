from art import logo
from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_of_alphabet=len(alphabet)

def caesar(action,text,shift):
    translated_word=""
    for letter in text:
        if letter in alphabet:
            index=alphabet.index(letter)
            if action == "encode":
                if index+shift >= num_of_alphabet:
                    translated_word+=alphabet[(index+shift)%num_of_alphabet]
                else:
                    translated_word+=alphabet[index+shift]
            elif action == "decode":
                if index-shift < 0:
                    translated_word+=alphabet[num_of_alphabet-(shift%num_of_alphabet)]
                else:
                    translated_word+=alphabet[index-shift]
        else:
            translated_word+=letter
    print(f"The {action}d text is {translated_word}")

retry=True
while retry:
    print(logo)
    action=input("Type 'encode' to encrypt, and 'decode' to decrypt:\n")
    text=input("Type your message\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(action,text,shift)
    choice=input("Do you want to try again - yes or no: ").lower()
    if choice=='no':
        retry=False
    else:
        clear()
print("-----GOODBYE CIPHER ENDED-----")