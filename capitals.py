#!/usr/bin/env python
# -*- coding: utf-8 -*-

from csv import DictReader
from random import choice, choices
import sys
import os

DATAFLE = 'capitals.tsv'
EXIT_WORDS = ['quit', 'exit', 'bye', 'done']
HELP_WORDS = ['help', 'cheat']

def quit(n_right, n_wrong):
    print('# correct: {}'.format(n_right))
    print('# wrong: {}'.format(n_wrong))
    sys.exit()

def print_all(selection):
    for q in selection:
        country, capital = q['country'], q['capital']
        print('{}: {}'.format(country, capital))

def main():

    with open(DATAFLE) as f:
        lines = f.readlines()

    data = []
    for line in lines[1:]:
        city, country = line.split('\t')
        data.append({
            'country': country.strip(),
            'capital': city.strip(),
        })
        
    
    selection = choices(data, k=10)
    right = []
    wrong = list(selection)
    n_right, n_wrong  = 0, 0

    while True:
        if len(wrong) == 0:
            print('You have finished another exciting game of capitals.py!')
            quit(n_right, n_wrong)
        q = choice(wrong)
        country, capital = q['country'], q['capital']
        os.system('cls' if os.name == 'nt' else 'clear')
        a = input('What is the capital of {}?: '.format(country))
        if a.lower() in EXIT_WORDS:
            quit(n_right, n_wrong)
        elif a.lower() in HELP_WORDS:
            print_all(selection)
        elif a == capital:
            wrong.remove(q)
            right.append(q)
            n_right =+ 1
            print('✓')
        else:
            n_wrong += 1
            print('✗ {}'.format(capital))
        input('Press Enter when ready for next exciting question!')



if __name__ == '__main__':
    main()