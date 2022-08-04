import random
tries = 1 # essentially controls the main while loop
wrong=[]#stores all the wrong letters
trish ='skagfkhasgowuofosfajsaf'# this variable is just a bunch of random words so that when it runs it doesn't compact it all together in the console
guessed = [] #stores all the correct letters
questions = ''# i made this before currentGuess and couldnt be bothered to change it. sorry
word = input('Player One please enter a word') #input for player one
str(word) # converts the word to a string just in case
wordLength = len(word) # creates a variable of it to make it easier
currentGuess = ''
#############################################################################
def gen(length, char):
    string = ''
    for i in range(0, length):
        string = string +char
    return string
#############################################################################
for i in range (100):
    print(random.choice(trish) +   ' hiding the word' )# these two lines clear the console so player 2 can't see the word
    
#############################################################################
def replace(word, currentGuess, character): #this function helps to replace the question marks with the correct letters entered
    smth = ''
    i = 0
    for smthelse in currentGuess:
        if smthelse == '?':
            if word[i] == character:
                smth = smth + character
            else:
                smth = smth + '?'
        else:
            smth = smth + smthelse
        i += 1
    return smth
#############################################################################
def print_scaffold():
    if (tries == 0):
        print ("_________")# these are all the displays for the hangmen
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
        print(questions)
        print('WRONG LETTERS:')
        print(wrong)
    elif (tries == 1):# helps control the order the displays come in
        print ("_________")
        print( "|	 |")
        print( "|	 O")
        print ("|")
        print( "|")
        print ("|")
        print ("|________")
        print(questions)# prints the question marks
        print('WRONG LETTERS:')
        print(wrong)
    elif (tries == 2):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	 |")
        print ("|	 |")
        print ("|")
        print ("|________")
        print(questions)
        print('WRONG LETTERS:')# prints the wrong letters to help avoid repeats
        print(wrong)
    elif (tries == 3):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|")
        print ("|	 |")
        print ("|")
        print ("|________")
        print(questions)
        print('WRONG LETTERS:')
        print(wrong)
    elif (tries == 4):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|")
        print ("|________")
        print(questions)
        print('WRONG LETTERS:')
        print(wrong)
    elif (tries == 5):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ ")
        print ("|________")
        print(questions)
        print('WRONG LETTERS:')
        print(wrong)
    elif (tries == 6):
        print ("_________")
        print ("|	 |")
        print ("|	 O")
        print ("|	\|/")
        print ("|	 |")
        print ("|	/ \ ")
        print ("|________")
        print ("")
        print(questions)
        print('WRONG LETTERS:')
        print(wrong)
        return

print('The length of the word is', len(word)) #shows the length of the word

currentGuess = gen(wordLength, '?') #created a new variable because i was lazy (line 6)

################################################################################
while tries < 7:# the main while loop
    selection = ''
    for letter in word:
        if letter in guessed:
            selection = selection + letter
        else:
            selection = selection + '_'
        if selection == word:
            break
    guess = input('Player two please guess a letter') 
    if guess in guessed or guess in wrong: # acknowledges repeated letters
        print('Already guessed', guess)
    elif guess in word:
        print('Correct')
        guessed.append(guess)# adds the correct guessed words to the array (line 5)
        currentGuess = replace(word, currentGuess, guess) # uses the replace function to replace the question marks
    else:
        print('Wrong')
        tries = tries + 1 # limits the amount of guesses
        wrong.append(guess) # adds the wrong guesses to the list
    if currentGuess == word:
        print('The word was', word)
        quit() # exits the console
    questions = currentGuess # lazy fix to line 6 and line 105
    print_scaffold() #defined function
    print()
if tries < 7: # stops the loop
    
    print('You guessed', word)
else:
    print('The word was', word)
#################################################################################
