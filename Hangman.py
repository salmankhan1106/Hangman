import random
import stages
import words

lives = 6
chosen_word=random.choice(words.word_list)
print("------------------")
print(chosen_word)
print("------------------")

#to add the dash in the place of the letter 
display = []
print(" ")
print(" ")
for letter in chosen_word:
    display += '_'

print(display)
game_over = False
print(" ")
print(" ")
while not game_over: # while true
    guessed_letter= input("enter the letter : ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(" ")        
    print (display)

    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print(" ")
            print(" ")
            print(" ")
            print("------------")
            print("You Lose")
            print("------------")            
    if '_' not in display :
        game_over = True
        print("You Win !")    

    print(stages.stages[lives])         
               