import random,sys

HEARTS = chr(9829)#Character 9829 is '♥'
DIAMONDS =chr(9830)# Character 9830 is '♦'.
SPADES =chr(9824) # Character 9824 is '♠'.
CLUBS =chr(9827) # Character 9827 is '♣'.


BACKSIDE='backside'

def main ():
    print (
        """
        Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.

         """
    )
    money = 5000
    while True:
        if money<=0:
            print('You are broke')
            print('You are out')
            sys.exit()
        #let the player enter their bet for this round
        print('Money:',money)
        bet= getBet(money)

        #give the delera and pleayer two cards form deck each
        deck =getDeck()
        dealerHand=[deck.pop(),deck.pop()]
        playerHand=[deck.pop(),deck.pop()]

        #handle player actions
        print('Bet',bet)
        while True:
            displayHands(playerHand,dealerHand,False)
            print()
            #check if the player has a burst
            if getHandValue(playerHand)>21:
                break
            #get the players move either H,S,OR D
            move = getMover(playerHand,money-bet)

            #handle the playe acttions
            if move =='D':
                #player is doubling down, they can increase theri bet
                additionalBet=getBet(min(bet,(money-bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:',bet)
            if move in ('H','D'):
                #hit /doubling down takes another card
                newCard=deck.pop()
                rank,suit=newCard
                print('You drew a {} of {}. '.format(rank,suit))
                playerHand.append(newCard)
            if getHandHandValue(playerHand)>21:
                #the player has busted
                continue
            if move in ('S','D'):
                #stand / doubling down stops the players turn
                break
        if getHandValue(playerHand)<=21:
            while getHandValue(dealerHand)<17:
                #the dealer hits
                print('Delaer HIt')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand)>21:
                    break # bursted
                input('Press Enter to continue')
                print('\n\n')
        displayHands(playerHand,dealerHand,True)
        playerValue =getHandValue(playerHand)
        dealerValue=getHandValue(dealerHand)
        #Handle wheter the player won ,lost,ties

        if dealerValue>21:
            print('Dealer bursts! You win${}!'.format(bet))
            money+=bet
        elif(playerValuea>21)or (playerValue<dealerValue):
            print('You lost! ')
            money+=bet
        elif playerValue==dealerValue:
            print('You tie')
        input('Press enter to continue')
        print('\n\n')


def getBet(maxBet):
 #ask the player how much they wan to bet for this round
 while True:
     print('How much do you bet ? (1- {},or Quit)'.format(maxBet))
     bet = input('>').upper().strip()
     if bet =='QUIT':
         print('THanks for playing')
         sys.exit()
     if not bet.decimal():
         continue #if player dint enteta number ask again
     bet = int(bet)
     if 1<=bet <=maxBet:
         return bet
                    
main()