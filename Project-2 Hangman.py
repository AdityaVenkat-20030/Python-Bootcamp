#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
word_list=["Austrailia","Bangladesh","Canada","Denmark","Egypt","France","Greece","Haiti","India","Japan"]

def getRandom():
    word=random.choice(word_list)
    return word.upper()
def play(word):
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
            if guess in guessed_letter:
                print("You already guessed the letter", guess)
                display_hangman(tries)
                print(word_completion)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries=tries-1
                display_hangman(tries)
                if tries==0:
                    print("you ran out of tries and the word is",word)
                    break
                guessed_letter.append(guess)
            else:
                print("Good job", guess,"is in the word!")
                guessed_letter.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                print(word_completion)
                if "_" not in word_completion:
                    guessed=True
        elif len(guess)==len(word):
            pass
        else:
            print('Game Over')
def display_hangman(tries):
    if tries==0:
        print("""
               __________
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               _
              """)
    elif tries==1:
        print("""
               __________
               |      |
               |      O
               |     \\|/
               |      |
               |     / \
               _
              """)
    elif tries==2:        
        print("""
               __________
               |      |
               |      O
               |    \\|/
               |      |
               |     
               _
              """)
    elif tries==3:
        print("""
               __________
               |      |
               |      O
               |    \\|
               |      |
               |     
               _
              """)
    elif tries==4:       
        print("""
               __________
               |      |
               |      O
               |      |
               |      |
               |     
               _
               """)
    elif tries==5:        
        print("""
               __________
               |      |
               |      O
               |    
               |      
               |      
               _
               """)
    elif tries==6:
        print("""
               __________
               |      |
               |      
               |    
               |      
               |     
               _
              """)
def main():
    word=getRandom()
    play(word)
    again=input('Do you want to play again(Y/N): ').upper()
    while again=='Y':
        main()
        
main()
    
        


# In[ ]:




