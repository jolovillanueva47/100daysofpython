import pandas as pd
nato_data=pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index, row) in nato_data.iterrows()}
#print(nato_dict)
word_entered=input("Enter a word: ").upper()
nato_entered_word=[nato_dict[letter] for letter in word_entered]
print(nato_entered_word)