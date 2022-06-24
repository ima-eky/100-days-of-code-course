import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")

# # Keyword Method with iterrows()
nato_alphabets={row.letter:row.code for (index, row) in data.iterrows()}
 #TCreate a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input=input(f'Enter a name :\n').upper().strip()
    try:
        phonetic_code_words =[nato_alphabets[letter] for letter in user_input]
    except KeyError:
        print(f'Sorry,only letters in alphabet please')
        generate_phonetic()
    else:
        print(phonetic_code_words)
generate_phonetic()