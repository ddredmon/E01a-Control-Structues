#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #prints a greeting
colors = ['red','orange','yellow','green','blue','violet','purple'] #creates a variable titled "colors" that includes those typed colors
play_again = '' #creates a variable called "play_again"
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #Creates a condition that is met only when "play_again" does not equal n or no, which will make the lower indented lines run until the condition is no longer met.
    match_color = random.choice(colors) #creates a variable called "match_color" that becomes equal to a random color from the "colors" variable list
    count = 0 #creates a variable called "count" that becomes equal to 0
    color = '' #creates an empty variable titled "color"
    while (color != match_color): #creates a condition that is met when the variable "color" does not equal the variable "match_color," which will make the lower indented lines run until the condition is no longer met
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #changes the variable stored and makes it all lowercase and without spaces
        count += 1 #adds 1 to the variable "count"
        if (color == match_color): #creates a condition that runs the lower indented code if the variable "color" equals "match_color"
            print('Correct!') #prints the text "correct"
        else: #creates a condition that occurs if the above "if" statement is not met
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints text that lets the user see the number of times they have attempted to answer correctly, the bracketed text becoming set equal to the variable "count"
    print('\nYou guessed it in {0} tries!'.format(count)) #prints text that includes the number of tries the user has had at solving the question, where the bracketed number is set equal to the variable "count" 
    if (count < best_count): #creates a condition that runs the lower indented code if the variable "count" is less than the variable "best_count"
        print('This was your best guess so far!') #prints text
        best_count = count #sets the variable best_count equal to the variable "count"
    play_again = input("\nWould you like to play again? ").lower().strip() #prints text that the user can type next to, while creating a variable titled "play_again" that saves what the user types, which is then dropped to all lowercase letters and stripped of spaces
print('Thanks for playing!') #prints text