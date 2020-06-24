#!/usr/bin/python3

from random import choice
import os

#  Color dictionary for aesthetic use
colors = {'red': '\033[1;31m',
          'green': '\033[1;32m',
          'blue': '\033[1;36m',
          'gray': '\033[1;90m',
          'reset': '\033[m'}


def get_wordlist():

    #  Choose secret word from a wordlist file in the same directory as the script.
    #  If a wordlist file is not provided, the game exits. 
    try:
        with open(os.path.join(os.path.dirname(__file__), 'compoundwords.txt')) as w:
            lines = w.readlines()
            words = [line.strip().upper() for line in lines]
            secret = choice(words)
            return secret
    except IOError:
        return False

def hide(word, masked, hack=False):
    #  Print blanks and guessed letters
    for position, letter in enumerate(word):
        if masked[position] == letter:
            print(f'{colors["green"]}{letter}{colors["reset"]}', end=' ')
        elif word[position] == ' ':         #  This is a quick workaround (pt-BR: "gambiarra")
            masked[position] == letter      #  for open compound words.
            print('', end='')
        else:
            print('_', end=' ')
    print('', end='')
    print()

    #  If hack mode is on, game will print the secret
    if hack:
        for letter in word:
            print(f'{colors["gray"]}{letter}{colors["reset"]}', end=' ')
        print()

def play(secret):

    #  Set initial variables
    hidden = ['_' if letter.isalpha() else letter for letter in secret]
    guessed_letters = []
    turns = 6

    #  Game begins
    while turns > 0:

        hide(secret, hidden)

        #  Player wins if words match
        if ''.join(secret) == ''.join(hidden):
            print('Parabéns, você acertou!')
            break

        print()
        guess = input('Tente adivinhar qual é a palavra secreta. Digite uma letra: ').strip().upper()
        
        if guess.isalpha() and len(guess) == 1:
            
            if guess in guessed_letters:
                print('Você já jogou esta letra.')
            
            else:
                if guess in secret:
                    for position, letter in enumerate(secret):
                        if guess == letter:
                            hidden[position] = letter
                else:
                    if turns != 0:
                        turns -= 1
                        print(f'Errado! {colors["red"]}{guess.upper()}{colors["reset"]} não está na palavra.')
                    else:
                        break
                
                guessed_letters.append(guess)

            if turns > 0:        
                print(f'Letras jogadas: {colors["blue"]}{" - ".join(guessed_letters)}{colors["reset"]}')
                print(f'Você tem {colors["red"]}{turns}{colors["reset"]} chance(s) restantes.')
        
        else:
            print('Você deve digitar uma letra.')
        
        print()

    else:
        print(f'Você perdeu! A resposta correta era {colors["red"]}{secret.lower()}{colors["reset"]}')

def main():
    word = get_wordlist()
    if word:
        play(word)
    else:
        print('Nenhum dicionário foi encontrado. O programa será encerrado.')


if __name__ == '__main__':
    main()
