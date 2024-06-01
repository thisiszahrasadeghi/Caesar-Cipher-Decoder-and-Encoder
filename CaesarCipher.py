from CaesarCipher_art import CaesarCipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar (text , shift , direction):
    new_text = ""
    for char in text :
        if char in alphabet : 
            position = alphabet.index(char)
            if direction == 'encode' :
                new_position = position + shift
            elif direction == 'decode' :
                new_position = position - shift
            new_text += alphabet[new_position]
        else :
            new_text += char
    print(f"the {direction}d message is : {new_text}")


print(CaesarCipher)
continue_game = True
while continue_game:
    direction = input('Type \"encode\" to encrypt, and type "decode" to decrypt: \n').lower()
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n "))
    shift = shift % 26
    caesar(text, shift, direction)
    try_again = input(" Do you want to try again? yes or no.").lower()
    if try_again == 'no' :
        continue_game = False
        print("Good Bye!")
