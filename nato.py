import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# for (index, row) in data.iterrows():
#     my_dict = {row.letter : row.code}

my_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter your name : ").upper().strip()
word_list = [letter for letter in word]

for letter in word_list:
    print(f"{letter} for {my_dict[letter]}")

