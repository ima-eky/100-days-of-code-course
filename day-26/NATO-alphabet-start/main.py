import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")

# # Keyword Method with iterrows()
nato_alphabets={row.letter:row.code for (index, row) in data.iterrows()}
 #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input=input(f'Enter a name :\n').upper().strip()
phonetic_code_words =[nato_alphabets[letter] for letter in user_input ]
print(phonetic_code_words)