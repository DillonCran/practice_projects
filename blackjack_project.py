import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def draw_card(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()     

class Player():
    
    def __init__(self,name,bankroll=100):
        self.name = name
        self.bankroll = bankroll
        self.player_hand = []
        self.player_hand_value = 0

        #for split hands
        self.split_hand_one = []
        self.split_hand_two = []
        self.split_hand_one_value = 0
        self.split_hand_two_value = 0
        self.split = '#'
        
    def __str__(self):
        print(f'{self.name} has {self.bankroll} chips left.')
        
    def add_card(self,new_card):

        #deciding if aces are 11 or 1 when card is drawn rather than at the end
        if new_card.rank == 'Ace':
            print(new_card)
            ace_value = int(input('Would you like this Ace to be 11 or 1?:'))
            if ace_value == 1:
                new_card.value = 1
            elif ace_value == 11:
                new_card.value = 11

        if self.split == True:
            self.split_hand_one.append(new_card)
            self.split_hand_two.append(new_card)

        #appends new card to player hand
        else:
            self.player_hand.append(new_card)
    
    def clear_hand(self):
        self.player_hand = []
        self.split_hand_one = []
        self.split_hand_two = []

    def split_hand(self):
        #Just splits the hand into two seperate lists
        self.split = True
        self.split_hand_one = player.player_hand[0]
        self.split_hand_one = player.player_hand[1]

    def hand_value_calc(self):

        if len(self.player_hand) == 2:
            self.player_hand_value = player.player_hand[0].value + player.player_hand[1].value

        if len(self.player_hand) == 3:
            self.player_hand_value = player.player_hand[0].value + player.player_hand[1].value + player.player_hand[2].value

        if len(self.player_hand) == 4:
            self.player_hand_value = player.player_hand[0].value + player.player_hand[1].value + player.player_hand[2].value + player.player_hand[3].value

        if len(self.player_hand) == 5:
            self.player_hand_value = player.player_hand[0].value + player.player_hand[1].value + player.player_hand[2].value + player.player_hand[3].value + player.player_hand[4].value

        #for calc split hand values
        if len(self.player_hand) == 2 and self.split == True:
            self.split_hand_one_value = player.split_hand_one[0].value + player.split_hand_one[1].value
            self.split_hand_two_value = player.split_hand_two[0].value + player.split_hand_two[1].value

        if len(self.player_hand) == 3 and self.split == True:
            self.split_hand_one_value = player.split_hand_one[0].value + player.split_hand_one[1].value + player.split_hand_one[2].value
            self.split_hand_two_value = player.split_hand_two[0].value + player.split_hand_two[1].value + player.split_hand_two[2].value

        if len(self.player_hand) == 4 and self.split == True:
            self.split_hand_one_value = player.split_hand_one[0].value + player.split_hand_one[1].value + player.split_hand_one[2].value + player.split_hand_one[3].value
            self.split_hand_two_value = player.split_hand_two[0].value + player.split_hand_two[1].value + player.split_hand_two[2].value + player.split_hand_two[3].value

        elif len(self.player_hand) == 5 and self.split == True:
            self.split_hand_one_value = player.split_hand_one[0].value + player.split_hand_one[1].value + player.split_hand_one[2].value + player.split_hand_one[3].value + player.split_hand_one[4].value
            self.split_hand_two_value = player.split_hand_two[0].value + player.split_hand_two[1].value + player.split_hand_two[2].value + player.split_hand_two[3].value + player.split_hand_two[4].value

class Dealer():
    
    def __init__(self):
        self.dealer_hand = []
        self.dealer_hand_value = 0
        
    def add_card(self,new_card):
        self.dealer_hand.append(new_card)
    
    def clear_hand(self):
        self.dealer_hand = []

    def hand_value_calc(self):
        if len(self.dealer_hand) == 2:
            self.dealer_hand_value = dealer.dealer_hand[0].value + dealer.dealer_hand[1].value

        if len(self.dealer_hand) == 3:
            self.dealer_hand_value = dealer.dealer_hand[0].value + dealer.dealer_hand[1].value + dealer.dealer_hand[2].value

        if len(self.dealer_hand) == 4:
            self.dealer_hand_value = dealer.dealer_hand[0].value + dealer.dealer_hand[1].value + dealer.dealer_hand[2].value + dealer.dealer_hand[3].value

        if len(self.dealer_hand) == 5:
            self.dealer_hand_value = dealer.dealer_hand[0].value + dealer.dealer_hand[1].value + dealer.dealer_hand[2].value + dealer.dealer_hand[3].value + dealer.dealer_hand[4].value

class Table():

    def __init__(self):
        pass

    def check_win():
        global current_bet

        if game_phase != 'compare_hands':

            #Dealer BJ
            if dealer.dealer_hand_value == 21 and player.player_hand_value < 21:
                print('Dealer has blackjack!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                current_bet = 0
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Player BJ
            if player.player_hand_value == 21 and dealer.dealer_hand_value < 21:
                print(f'{player.name} has blackjack!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                player.bankroll += current_bet*2.25
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Player bust
            if player.player_hand_value > 21:
                print(f'{player.name} bust!  Dealer wins this hand.')
                print(f'Dealer wins with {dealer.dealer_hand_value}')
                current_bet = 0
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Dealer Bust
            if dealer.dealer_hand_value > 21:
                print('Dealer bust! Player wins this hand')
                print(f'{player.name} wins with {player.player_hand_value}')
                player.bankroll += current_bet*2
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Else/error message
            else:
                pass

        elif game_phase == 'compare_hands':

            #Dealer BJ
            if dealer.dealer_hand_value == 21 and player.player_hand_value < 21:
                print('Dealer has blackjack!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                current_bet = 0
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Player BJ
            if player.player_hand_value == 21 and dealer.dealer_hand_value < 21:
                print(f'{player.name} has blackjack!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                player.bankroll += current_bet*2.25
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #PUSH
            if player.player_hand_value == dealer.dealer_hand_value:
                print(f'{player.name} has {player.player_hand_value} and Dealer has {dealer.dealer_hand_value}')
                print('Its a tie!  Push hand!')
                player.bankroll += current_bet
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Player bust
            if player.player_hand_value > 21:
                print(f'{player.name} bust!  Dealer wins this hand.')
                print(f'Dealer wins with {dealer.dealer_hand_value}')
                current_bet = 0
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Dealer Bust
            if dealer.dealer_hand_value > 21:
                print('Dealer bust! Player wins this hand')
                print(f'{player.name} wins with {player.player_hand_value}')
                player.bankroll += current_bet*2
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Dealer win
            if dealer.dealer_hand_value > player.player_hand_value and dealer.dealer_hand_value < 21:
                print('Dealer wins!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                current_bet = 0
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Player win
            if dealer.dealer_hand_value < player.player_hand_value and player.player_hand_value < 21:
                print(f'{player.name} wins!')
                print(f'{player.name} had {player.player_hand_value} against Dealers {dealer.dealer_hand_value}')
                player.bankroll += current_bet*2
                print(f'New bankroll balance is {player.bankroll}')
                Table.play_again()

            #Else/error message
            else:
                pass

    def play_again():

        global game_phase

        play_again = input('Would you like to play again? Y or N: ')
        if play_again == 'Y':
            game_phase = 'startup'
            

        elif play_again == 'N':
            print('Okay, goodbye!')
            game_phase = '#'
            game_on = False

            

        else:
            print('Thats not a valid input!')
            Table.play_again()

    def print_table():

        if game_phase == 'player_turn' or game_phase == 'initial_deal':

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand: [{dealer.dealer_hand[0]}] [Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand: [{player.player_hand[0]}] [{player.player_hand[1]}]')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            elif len(dealer.dealer_hand) == 2 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]}')
                print('\n')
                print('\n')
                pass

        if game_phase == 'player_turn' or game_phase == 'initial_deal' and player.split == True:

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet hand #1: {current_bet}')
                print(f'Current bet hand #2: {current_bet}')
                print('\n')
                print(f'Dealer Hand: [{dealer.dealer_hand[0]}] [Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand #1: [{player.split_hand_one[0]}] [{player.split_hand_one[1]}]')
                print(f'{player.name} Hand #2: [{player.split_hand_two[0]}] [{player.split_hand_two[1]}]')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            elif len(dealer.dealer_hand) == 2 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--[Face Down Card]')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]}')
                print('\n')
                print('\n')
                pass


        elif game_phase != 'player_turn' and game_phase != 'initial_deal':

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 3 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 4 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 5 and len(player.player_hand) == 2:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}--{dealer.dealer_hand[4]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 3 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 4 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 5 and len(player.player_hand) == 3:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}--{dealer.dealer_hand[4]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 3 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 4 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 5 and len(player.player_hand) == 4:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}--{dealer.dealer_hand[4]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 2 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 3 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]}')
                print('\n')
                print('\n')
                pass

            if len(dealer.dealer_hand) == 4 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]}')
                print('\n')
                print('\n')
                pass

            elif len(dealer.dealer_hand) == 5 and len(player.player_hand) == 5:
                print(f'Current Bankroll: {player.bankroll}')
                print(f'Current bet: {current_bet}')
                print('\n')
                print(f'Dealer Hand:--{dealer.dealer_hand[0]}--{dealer.dealer_hand[1]}--{dealer.dealer_hand[2]}--{dealer.dealer_hand[3]}--{dealer.dealer_hand[4]}')
                print('-----------------------------------------------')
                print(f'{player.name} Hand:--{player.player_hand[0]}--{player.player_hand[1]}'--{player.player_hand[2]}--{player.player_hand[3]}--{player.player_hand[4]})
                print('\n')
                print('\n')
                pass


#Game logic starts here!

game_on = True

print('\n')
print('\n')
print('Welcome to JankJack!')
player = Player(input('What is your name? '))
dealer = Dealer()
mydeck = Deck()
hand_counter = 1
print('\n')
print(f'Welcome {player.name}!!')
print('\n')

if game_on:
    game_phase = 'startup'

#OFF state
while game_on == False:
    break

#Resets counters and requests bet
while game_on == True:

    if game_phase == '#':
        break

    if game_phase == 'startup':

        #resets bet ammount
        current_bet = 0
        
        #clear last hand
        player.clear_hand()
        dealer.clear_hand()

        #clear values for hands
        player.player_hand_value = 0
        dealer.dealer_hand_value = 0
        
        #Displays hand number and shuffles deck
        print(f'hand# {hand_counter}')
        mydeck.shuffle()
        
        #asks for bet
        print('How much would you like to bet?')
        print(f'Current Bankroll: {player.bankroll}')
        current_bet = int(input('Please place a bet: '))
        if current_bet > player.bankroll:
            print('You do not have the funds for this!')
            current_bet = 0

        elif current_bet < 0:
            print('You cant bet a negative number!')
            current_bet = 0

        else:
            player.bankroll = player.bankroll - current_bet
            print('Bet placed, dealing cards now!')
            game_phase = 'initial_deal'


    #Deals out initial hand/table
    elif game_phase == 'initial_deal':

        #Increases hand counter
        hand_counter += 1
        print('\n')
        
        #deals cards to player/dealer
        dealer.add_card(mydeck.draw_card())
        player.add_card(mydeck.draw_card())
        dealer.add_card(mydeck.draw_card())
        player.add_card(mydeck.draw_card())

        #Assigning drawn cards to hand value variable
        player.hand_value_calc()
        dealer.hand_value_calc()

        print('\n')

        #Prints out table
        Table.print_table()

        #Initial game phase and win check on default cards
        Table.check_win()
        game_phase = 'player_turn'


    #Player goes first
    elif game_phase == 'player_turn' and current_bet > 0:

        #initial hit offer
        play_choice = input('Would you like to hit, stay, DD, or split?: ')

        if play_choice == 'stay':
            Table.print_table()
            input('Okay Dealers turn, press any key to continue: ')
            game_phase = 'dealer_turn'

        if play_choice == 'DD' and len(player.player_hand) == 2:
            print('Brave! Here is your one card for double down.')

            #doubling bet for DD
            player.bankroll - current_bet
            current_bet * 2

            player.add_card(mydeck.draw_card())
            print(f'{player.name} drew {player.player_hand[len(player.player_hand)-1]}')
            input('Okay Dealers turn, press any key to continue: ')
            game_phase = 'dealer_turn'

        if play_choice == 'split' and len(player.player_hand) == 2 and player.player_hand[0].rank == player.player_hand[1].rank:

            #splitting hands into two
            player.split_hand()
            player.add_card()

            #Splits the bet into two, removes from bankroll
            player.bankroll -= current_bet
            split_bet_one = current_bet
            split_bet_two = current_bet
            print('Hand has been split, good luck!')
            print('\n')

            #twlls players what they drwe, prints table
            print(f'{player.name} drew {player.split_hand_one[1]} for the first hand')
            print(f'{player.name} drew {player.split_hand_two[1]} for the second hand')
            print('\n')
            print('PSST You can only split once ;)')
            print('\n')
            Table.print_table()

            #resolving hand one
            hit_split_one = input('Would you like to hit or stay on your first hand?: ')
            if hit_split_one == 'hit':
                while hit_split_one == 'hit':
                    if len(player.player_hand) < 5:

                        player.add_card(mydeck.draw_card())
                        player.hand_value_calc()
                        print(f'{player.name} drew {player.split_hand_one[len(player.split_hand_one)-1]}')
                        Table.check_win()
                        hit_split_one = input('Would you like to hit again or stay?: ')

                    if hit_split_one == 'stay':
                        Table.print_table()
                        input('Okay Dealers turn, press any key to continue: ')
                        game_phase = 'dealer_turn'

                    else:
                        print(f'{player.name} has hit max river')
                        Table.print_table()
                        Table.check_win()
                        input('Okay Dealers turn, press any key to continue: ')
                        hit_split_one = 'stay'



            #resolving hand two



        #hit up to 5 cards
        elif play_choice == 'hit':
            while play_choice == 'hit':

                if len(player.player_hand) < 5:

                    player.add_card(mydeck.draw_card())
                    player.hand_value_calc()
                    print(f'{player.name} drew {player.player_hand[len(player.player_hand)-1]}')
                    Table.check_win()
                    play_choice = input('Would you like to hit again or stay?: ')

                    if play_choice == 'stay':
                        Table.print_table()
                        input('Okay Dealers turn, press any key to continue: ')
                        game_phase = 'dealer_turn'

                else:
                    print(f'{player.name} has hit max river')
                    Table.print_table()
                    Table.check_win()
                    input('Okay Dealers turn, press any key to continue: ')
                    play_choice = 'stay'

        else:
            print('that is not a valid input')

    #Dealer plays out their hand
    elif game_phase == 'dealer_turn':

        #prints new table with both dealer cards visible
        print('Dealer flips face down card!')
        Table.print_table()

        #Dealer hitting if hand below 17
        while len(dealer.dealer_hand) < 5 and dealer.dealer_hand_value < 17:
            dealer.add_card(mydeck.draw_card())
            dealer.hand_value_calc()

            #if an ace would bust the dealer, its a 1 not 11
            if dealer.dealer_hand[len(dealer.dealer_hand)-1].rank == 'Ace' and dealer.dealer_hand_value > 21:
                dealer.dealer_hand[len(dealer.dealer_hand)-1].value = 1
                dealer.hand_value_calc()

            print(f'Dealer drew a {dealer.dealer_hand[len(dealer.dealer_hand)-1]}')
            input('Press any key to continue: ')
            
        #Dealer stay if hand is 17 or above
        if len(dealer.dealer_hand) < 5 and dealer.dealer_hand_value >= 17:
            print('Dealer is done drawing!')
            Table.print_table()
            input('Press any key to continue: ')
            game_phase = 'compare_hands'

        #Dealer max river
        elif len(dealer.dealer_hand) >= 5:
            print('Dealer has hit max river!')
            Table.print_table()
            input('Press any key to continue: ')
            game_phase = 'compare_hands'


    #Comparing hands where neither player bust or blackjack
    elif game_phase == 'compare_hands':

        Table.print_table()

        print(f'Dealer has hand total of {dealer.dealer_hand_value}')
        print(f'{player.name} has hand total of {player.player_hand_value}')
        print('\n')

        Table.check_win()

