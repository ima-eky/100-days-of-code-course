from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > 25:
                new_position = new_position % 26
            while (new_position < 0):
                new_position = 26 + new_position
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text.capitalize()}")


should_not_end = True
while (should_not_end):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    should_continue = input(f"Type 'yes' if you want to continue.Otherwise type 'no' :")
    if should_continue.lower() == "no":
        should_not_end= False
        print(f"Goodbye")