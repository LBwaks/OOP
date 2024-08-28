import random

MAX_GUESES =10
NUM_DIGITS =3

def main():
    print('''Bagels, a deductive logic game.
  By Al Sweigart al@inventwithpython.com
 
 I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
 When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
  
  For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True: #Main Loop
        secrectNum=getsecretNum()
        print('I have thought up a number')
        print('You have{} guesses to get it'.format(MAX_GUESES))
        numGueses =1
        while numGueses<=MAX_GUESES:
            guess=''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGueses))
                guess=input('> ')
            clues=getclues(guess,secrectNum)
            print(clues)
            numGueses+=1
            if guess==secrectNum:
                break
            if numGueses>MAX_GUESES:
                print('You ran out of guess.')
                print('The answer is {}'.format(secrectNum))
        
        print('Do you want to play again? (yes or no )')
        if not input('>').lower().startswith('y'):
            break
        print('Thanks for playing')


def getsecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secrectNum=''
    for i in range(NUM_DIGITS):
        secrectNum +=str(numbers[i])
    return secrectNum

def getclues(guess,SecretNum):
    if guess==SecretNum:
        return 'You got it.'
    clues =[]
    for i in range(len(guess)):
        if guess[i]==SecretNum[i]:
            #correct digit in the correct place
            clues.append('Fermi')
        elif guess[i] in SecretNum:
            #correct digit in a wrong place
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'#No correct digits
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        return ''.join(clues)

if __name__=='__main__':
    main()

       
    