#!/usr/bin/python3



# Todo:
# create backup of collection on startup
# extend card not found path in non-card addition path
# extend data you can provide (i.e. mana color, mana cost, etc.)

import sys

collection = {}

def main():
    # Creating dictionary out of collection storage file.
    with open('collection.txt', 'r') as f: 
        for line in f:
            tokens = line.strip().split()
            collection[' '.join(tokens[:-1])] = tokens[-1]
        print('Collection')
        print('-' * 30 + ' \n')
        for k, v in collection.items():
            print('{:<30s}|  {:>10s}x'.format(k, v))
        print('\n')
    
    #initialising the input
    print('Type "exit" to exit the program.')
    sys.stdout.write('Enter a card name [+ number]: ')
    card = ''
    while card == '':
        card = input().strip().lower()

    #input loop
    while card != 'exit':
        #non-card addition path
        if not card.split()[-1].isdigit() and not card.split()[-1][0] == '-':
            try:
                print('{}(s): {}'.format(card.capitalize(), collection[card.lower()]))
            except KeyError:
                print('{} not found, would you like to add it to your collection? (y/n)'.format(card.capitalize()))
        #card-addition path
        else:
            card = card.split()
            card_name = ' '.join(card[:-1]).lower()
            card_value = ''.join(card[-1])
            if card_name not in collection:
                collection[card_name] = 0
            collection[card_name] = str(int(collection[card_name]) + int(card_value))
            print('{}(s): {}'.format(card_name.capitalize(), collection[card_name]))

        card = ''

        while card == '':
            card = input()
    
    # Truncating collection.txt and saving the new dictionary to the file.
    with open('collection.txt', 'w') as f:
        for cards in sorted(collection):
            f.write(str(cards) + ' ' + str(collection[cards]) + '\n')




if __name__ == '__main__':
    main()