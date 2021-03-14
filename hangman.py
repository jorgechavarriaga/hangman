import draw
from wordlist import word_list

from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

counter = 0
wrong = 0
wrong_letters = []
right_letters = []
end = False
play_again = False
while not play_again:
  chosen_word = random.choice(word_list).lower()
  word_length = len(chosen_word)
  display = []
  for _ in range(word_length):
      display += "_"
  while not end:
    print(draw.logo)
    print(55*"*")
    print("         Welcome to my Hangman Game - By: Papá")
    print(55*"*")
    print(display)
    if wrong == 0:
        print(draw.stages[0])
    elif wrong == 1:
        print(draw.stages[1])
    elif wrong == 2:
        print(draw.stages[2])
    elif wrong == 3:
        print(draw.stages[3])
    elif wrong == 4:
        print(draw.stages[4])
    elif wrong == 5:
        print(draw.stages[5])
    elif wrong == 6:
        print(draw.stages[6])
    elif wrong == 7:
        print(draw.stages[7])
        end = True
        print(f"You Lose! The word was {chosen_word}")
        break
    guess = input("Guess a letter: ").lower()
    
    if guess not in letters:
      print("Invalid Character")
    if guess not in chosen_word:
        wrong +=1
        counter +=1
        wrong_letters += guess
    else:
        right_letters += guess
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # counter +=1
    # print(f"Display: {display}")
    final = ""
    for letter in display:
      final += letter
    clear()
    if final == chosen_word:
      print(f"{draw.stages[8]}\n")
      print("You WIN !!!")
      end = True
  new_game = input("Do you want to play again ? Y/N \n").lower()
  if new_game == "y":
    play_again = False
    wrong = 0
    end = False
    clear()

  else:
    print("No")
    play_again = True
