import random

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
word=[]
duplicated_char=[]
index_to_unlock=1
countries_capitals = []


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
        print(lotery_word)
        return lotery_word
    elif x == 3:
        countries_capitals= data_bases(x)
        random.shuffle(countries_capitals)
        lotery_word=list(countries_capitals[0][1])
        print(lotery_word)
        return lotery_word

def locking_word(z):
    word_size=len(z)
    for x in range(word_size):
        locked_word.append("_")
    return locked_word

def checking_char(x, y):
    if len([i for i,val in enumerate(y) if val==x])==0:
        return False
    else:
        duplicated_char=[i for i,val in enumerate(y) if val==x]
        return duplicated_char

def unlocking_char(x, list, lock, duplicated_char):
    lenght=len(duplicated_char)
    while lenght !=0:
        index_to_unlock=duplicated_char[lenght-1]
        lock[index_to_unlock]=x
        lenght=lenght-1
    return lock 

def play_again():
    question = "j"
    while question != 'a' or 'q':
        question = input("press 'a' to play again or 'q' to quit: ")
        if question == 'a':
            main()
        elif question == 'q':
            quit()


def main():
    live = 0
    splitting_countries()
    user_choice = int(choose_category())
    print("You've selected category: ", +user_choice)
    lotery_word=random_word(user_choice)
    locked_word=locking_word(lotery_word)
    print(locked_word)
    while live <= 6:
        char = input(" Please give me a char: ")
        if checking_char(char, lotery_word) is not False:
            print("Congratulation!!!")
            duplicated_char=checking_char(char, lotery_word)
            print(unlocking_char(char, lotery_word, locked_word, duplicated_char))
        else:
                print("kasujemy zycie")
                print(hangman[live])
                live += 1
    print("You lost!")
            


main()
play_again()
