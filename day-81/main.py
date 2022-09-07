# A text-based (command line) program that takes any String input and converts it into Morse Code

from morse_translator import Cryptology

def main():

    SHOULD_CONTINUE = True
    actions = ['encrypt', 'decrypt', 'exit']

    while(SHOULD_CONTINUE):
        try:
            action_to_do=int(input(f"Would you like to encrypt or decrypt text? Type 1 to encrypt text"
                           f", 2 to decrpyt text and 3 to exit:"))
            if action_to_do == 3:
                SHOULD_CONTINUE=False
            if action_to_do <= 0:
                print(f"No operation/action exists for given input. Type either 1,2 or 3 as instructed")
                continue


            else:
                message=input(f"What's the text?:\n")
                if action_to_do == 1 and message:
                    response=Cryptology.encrypt(message.strip())
                elif action_to_do ==2:
                    response=Cryptology.decrypt(message.strip()).capitalize()
        except ValueError:
            print("Invalid Input.Given input must be integers.")
        except IndexError:
            print(f"No operation/action exists for given input. Type either 1,2 or 3 as instructed")
        else:
            print(response)

if __name__ == '__main__':
    main()








