#!/usr/bin/env python
# coding: utf-8

# In[3]:


word_list=["Austrailia","Bangladesh","Canada","Denmark","Egypt","France","Greece","Haiti","India","Japan"]
import random
def getRandom():
    word=random.choice(word_list)
    return word.upper()
def play():
    word_completion='_'*len(word)
    guessed=False
    guessed_letter=[]
    guessed_word=[]
    tries=6
    print('Lets play Hangman!')
    print(word_completion)
    while not guessed and tries>0:
        guess=input('Enter your guess: ').upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("Good job", guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed=True
        elif len(guess)==len(word):
            pass
        else:
            print('Game Over')
def display_hangman(tries):
    stages=[ #final state:head,torso,both arms and both legs
            """
               __________
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               _
            
            """,
            #head,torso,both arms and one leg
            """
              __________
               |      |
               |      O
               |     \\|/
               |      |
               |     / \
               _
            
            """,
            #head,torso and both arms
            """
              __________
               |      |
               |      O
               |    \\|/
               |      |
               |     
               _
               
            """,
            #head,torso and one arm
            """
              __________
               |      |
               |      O
               |    \\|
               |      |
               |     
               _
               
            """,
            #head and torso
            """
              __________
               |      |
               |      O
               |      |
               |      |
               |     
               _
               
            """,
            #head
            """
              __________
               |      |
               |      O
               |    
               |      
               |      
               _
               
            """,
            #initial starting state
            """
              __________
               |      |
               |      
               |    
               |      
               |     
               _
               
            """]
def main():
    word=getRandom()
    play(word)
    again=input('Do you want to play again(Y/N): ').upper()
    while again=='Y':
        play(word)
    
        


# In[ ]:




