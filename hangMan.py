import random
import time
from os import system, name

hangman = [r'''
             ____
            |    |
                 |
                 |
                 |
                _|_''',r'''
             ____
            |    |
            o    |
                 |
                 |
                _|_''',r'''
             ____
            |    |
            o    |
            |    |
                 |
                _|_''',r'''
             ____
            |    |
            o    |
            |    |
           /     |
                _|_''',r'''
             ____
            |    |
            o    |
            |    |
           / \   |
                _|_''',r'''
             ____
            |    |
            o    |
            |\   |
           / \   |
                _|_''',r'''
             ____
            |    |
            o    |
           /|\   |
           / \   |
                _|_''']
jobs =[]
user_choice=1
lotery_word=[]
locked_word=[]
duplicated_char=[]
countries_capitals = []

def clear():
    system('clear')

def splitting_countries():
    for line in open('countries-and-capitals.txt'):
        line = line.split('|')
        countries_capitals.append(line)

def choose_category():
    user_choice=input("Pls select your category (1 - Jobs)(2 - Countries)(3 - Capitals)" )
    return user_choice

def data_bases(categories):
    if categories==1:
        jobs=['programmer', 'baker', 'mentor', 'fireman', 'policeman', 'gardener']
        return jobs 
    elif categories == 2 or 3:
        return countries_capitals

def random_word(x):
    if x == 1:
        jobs= data_bases(x)
        random.shuffle(jobs)
        lotery_word=list(jobs[0])
        return lotery_word
    elif x == 2:
        countries_capitals= data_bases(x)
        random.shuffle(countries_capitals)
        lotery_word=list(countries_capitals[0][0])
        del lotery_word[-1]
        print(lotery_word)
        return lotery_word
    elif x == 3:
        countries_capitals= data_bases(x)
        random.shuffle(countries_capitals)
        lotery_word=list(countries_capitals[0][1])
        del lotery_word[0]
        del lotery_word[-1]
        print(lotery_word)
        return lotery_word

def locking_word(z):
    word_size=len(z)
    for x in range(word_size):
        locked_word.append("_")
    return locked_word

def checking_char(x, y): #zwraca false jezeli nie ma znaku w slowie
    if len([i for i, val in enumerate(y) if val.lower()==x.lower()])==0:
        return False
    else:
        duplicated_char=[i for i,val in enumerate(y) if val.lower()==x.lower()]
        return duplicated_char #zwraca liste indeksow gdzie nasz char jest 

def unlocking_char(x, list, lock, duplicated_char):
    index_to_unlock=1
    lenght=len(duplicated_char)
    while lenght !=0:
        index_to_unlock=duplicated_char[lenght-1]
        lock[index_to_unlock]=x
        lenght=lenght-1
    return lock 

def play_again():
    question = ""
    while question != 'a' or 'q':
        question = input("press 'a' to play again or 'q' to quit: ")
        if question == 'a':
            main()
        elif question == 'q':
            quit()
        else:
            play_again()

def starting_time():
    start = time.time()
    return start
def ending_time(start_time):
    end = round(time.time() - start_time)
    return end



def finish(correct_guess, start_time, counter, lotery_word):
    if '_' not in locked_word:
        print(lotery_word)
        print("CONGRATULATION YOU WON")
        print(f"You played {ending_time(start_time)} seconds and tried giving correct letter {counter} times!")
    else:
        print(f"You played {ending_time(start_time)} seconds and tried giving correct letter {counter} times!")
        print(f"You lost! your word was {lotery_word}")


def main():
    correct_guess = 0
    counter = 0
    live = 0
    start_time = starting_time()
    user_choice = int(choose_category())
    print("You've selected category: ", + user_choice)
    lotery_word=random_word(user_choice)
    locked_word=locking_word(lotery_word)
    print(locked_word)
    while live <= 6:
        if '_' not in locked_word:
            break
        char = input(" Please give me a char: ")
        clear()
        counter += 1
        if checking_char(char, lotery_word) is not False:
            print(hangman[live])
            print(correct_guess)
            print("Congratulation!!!")
            duplicated_char=checking_char(char, lotery_word)
            print(unlocking_char(char, lotery_word, locked_word, duplicated_char))
        else:
            print("-1 live!")
            print(hangman[live])
            print(locked_word)
            live += 1
    finish(correct_guess, start_time, counter, lotery_word)

splitting_countries()
main()
play_again()