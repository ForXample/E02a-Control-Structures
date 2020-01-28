#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')#
colors = ['red','orange','yellow','green','blue','violet','purple']
play_again = ''
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors)  
    print(match_color)        #the computer will assign one of the element in "colors" to match_color
    count = 0                        #the count is "0" in the beginning
    color = ''                       #color is an empty string
    while (color != match_color):               #a whileloop: when the color does not equal to match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()               #convert all the input letters into lower cases, then ignore the leading and trailing whitespaces
        count += 1              #  1 count
        if (color == match_color):             #if the color does equal to the match_color
            print('Correct!')                           # print "correct" 
        else:                                   
            print('Sorry, try again. You have guessed {} times.'.format(count))  #
    
    print('\nYou guessed it in {} tries!'.format(count))

    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing!')