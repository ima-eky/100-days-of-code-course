from data import  MORSE_CODE_DICT,REVERSE_MORSE_CODE_DICT


class Cryptology:

    def __init__(self,message):
        self.message=message

    # Method that  encrypts string input to morse code

    def encrypt(message):
        message = message.upper()
        encrypted_word = ""

        ''' Checks dictionary and adds corresponding code to the encrypted
         word,using a space to separate characters '''
        for letter in message:
            if letter != " ":
                encrypted_word += MORSE_CODE_DICT[letter] + " "
            else:
                '''If a space is found,then it's the start of another word
                in the message.Double space is used to separate words '''
                encrypted_word += " "

        return encrypted_word
    # Method that  decrypts  morse code to english

    def decrypt(message):
        message += ' '

        decrypted_word = ""
        citext = ""
        for symbol in message:
            if symbol != " ":

                # keeps count of space (space separates character in morse code)
                space_count = 0

                # removing space from morse code
                citext += symbol
            # in the case of a space
            else:
                # A single space indicates a new character
                space_count += 1

                # Double space indicates the start of a new word,space needs to be added  to decrypted word
                if space_count == 2:

                    decrypted_word += " "
                else:
                    decrypted_word += REVERSE_MORSE_CODE_DICT[citext]
                    citext=""

        return decrypted_word

