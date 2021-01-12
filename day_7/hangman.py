import random
import hangman_art
import hangman_words
from replit import clear

print(hangman_art.logo)
chosen_word=random.choice(hangman_words.word_list)
chosen_word_len=len(chosen_word)
lives=6

guess_list=[]
#Create blanks
for i in range(chosen_word_len):
    guess_list.append("_")

#Check guessed letters
finished=False
guessed_letters=[]
while not finished:
    guess=input("Guess a letter: ").lower()
    clear()
    print(hangman_art.logo)
    index=0
    for letter in chosen_word:
        if guess == letter:
            guess_list[index]=letter
            correct_guess=True
        index+=1
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}. Which is incorrect")
    elif guess in guessed_letters:
         print(f"You've already guessed {guess}.")
    else:
        print(f"You've guessed {guess} correctly")

    if guess not in guessed_letters:
        guessed_letters.append(guess)
    print(f"Lives Remaining: {lives}")
    print(hangman_art.stages[lives])
    print(f"{' '.join(guess_list)}")

    if  lives==0:
        finished=True
        print("\nGame Over. You lose")
    elif  '_'  not in guess_list:
        finished=True
        print("\nYou Win")