# GAME OF WAR

# game outline
# deck is shuffled and split between two players
# each round players pull a card from the top of their deck and face eachother
# higher card wins and takes both cards, ties pull 3x cards off the top of each deck (war), tie again brings out another card.  winner takes all cards.
# Game ends when one player has no cards left.


from random import shuffle

# variables for cards
card_suits = ['Hearts','Diamonds','Clubs','Spades']
card_ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 11,  
    'Queen': 12,  
    'King': 13,  
    'Ace': 14   
}

# classes
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank 
        self.value = card_values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def gen_card(self):
        shuffled_suits = shuffle(card_suits)
        shuffled_ranks = shuffle(card_ranks)
        new_card = Card(shuffled_suits[0],shuffled_ranks[0])
        return new_card

class Deck():
    global player1_obj
    global player2_obj

    def __init__(self):
        self.deck_masterlist = []
        self.shuffled_deck = []
    
    def gen_deck(self):
        for suit in card_suits:
            for rank in card_ranks:
                new_card = Card(suit,rank)
                self.deck_masterlist.append(new_card)
    
    def shuffle_deck(self):
        shuffle(self.deck_masterlist)

    def deck_split(self):
        self.shuffle_deck()
        half_deck = len(self.deck_masterlist) // 2
        player1_obj.player_deck = self.deck_masterlist[:half_deck]
        player2_obj.player_deck = self.deck_masterlist[half_deck:]

class Player():

    global player1_obj
    global player2_obj
        
    def __init__(self,name):
        self.name = name
        self.player_score = 0
        self.player_deck = []
        self.player_hand = []
        self.player_hand_value = 0

    def __str__(self):
        return f"{self.name} has {self.player_score} wins."

    def add_win(self):
        self.player_score += 1
    
    def clear_score(self):
        self.player_score = 0

    def add_card(self):
        card = self.player_deck.pop(0)
        self.player_hand.append(card)

    def lose_card(self):
        pass

    def calc_hand_value(self):
        for card in self.player_hand:
            self.player_hand_value += card.value

    def clear_hand_value(self):
        self.player_hand_value = 0

    def clear_hand(self):
        self.player_hand = []

class Board():
    global player1_obj
    global player2_obj
    
    def __init__(self):
        self.is_war = False
    
    def deal_hands(self):
        # Draw one each for regular play
        if self.is_war == False:
            player1_obj.add_card()
            player2_obj.add_card()
        # Draw three each for war
        elif self.is_war == True:
            player1_obj.add_card()
            player2_obj.add_card()
            player1_obj.add_card()
            player2_obj.add_card()
            player1_obj.add_card()
            player2_obj.add_card()
        else:
            print("Something went wrong.")
    
    def play_round(self):
        self.is_war = False
        self.deal_hands()
        player1_obj.calc_hand_value()
        player2_obj.calc_hand_value()
        self.display()
        if player1_obj.player_hand_value > player2_obj.player_hand_value:
            print(f"{player1_obj.name} wins this round!")
            player1_obj.add_win()
            player1_obj.player_deck.extend(player1_obj.player_hand)
            player1_obj.player_deck.extend(player2_obj.player_hand)
            player1_obj.clear_hand_value()
            player2_obj.clear_hand_value()
            player1_obj.clear_hand()
            player2_obj.clear_hand()
            self.is_war = False
        elif player1_obj.player_hand_value < player2_obj.player_hand_value:
            print(f"{player2_obj.name} wins this round!")
            player2_obj.add_win()
            player2_obj.player_deck.extend(player1_obj.player_hand)
            player2_obj.player_deck.extend(player2_obj.player_hand)
            player1_obj.clear_hand_value()
            player2_obj.clear_hand_value()
            player1_obj.clear_hand()
            player2_obj.clear_hand()
            self.is_war = False
        elif player1_obj.player_hand_value == player2_obj.player_hand_value:
            print("WAR!")
            self.is_war = True
            self.war()
        else:
            print("Something went wrong.")

        
    def war(self):
        self.deal_hands()
        player1_obj.calc_hand_value()
        player2_obj.calc_hand_value()
        self.display()
        if player1_obj.player_hand_value > player2_obj.player_hand_value:
            print(f"{player1_obj.name} wins this round!")
            player1_obj.add_win()
            player1_obj.player_deck.extend(player1_obj.player_hand)
            player1_obj.player_deck.extend(player2_obj.player_hand)
            player1_obj.clear_hand_value()
            player2_obj.clear_hand_value()
            player1_obj.clear_hand()
            player2_obj.clear_hand()
            self.is_war = False
        elif player1_obj.player_hand_value < player2_obj.player_hand_value:
            print(f"{player2_obj.name} wins this round!")
            player2_obj.add_win()
            player2_obj.player_deck.extend(player1_obj.player_hand)
            player2_obj.player_deck.extend(player2_obj.player_hand)
            player1_obj.clear_hand_value()
            player2_obj.clear_hand_value()
            player1_obj.clear_hand()
            player2_obj.clear_hand()
            self.is_war = False
        elif player1_obj.player_hand_value == player2_obj.player_hand_value:
            print("DOUBLE WAR!!")
            self.is_war = True
            self.war()
        else:
            print("Something went wrong.")
            self.is_war = False

    def display(self):
            # prints a display to read cards, loops through hands and prints each card
            print(f"Player 1: {player1_obj.name} Score: {player1_obj.player_score}")
            for card in player1_obj.player_hand:
                print(f"{card}")
            print(f"{player1_obj.player_hand_value}")
            print("---------- VS ----------")
            print(f"{player2_obj.player_hand_value}")
            for card in player2_obj.player_hand:
                print(f"{card}")
            print(f"Player 2: {player2_obj.name} Score: {player2_obj.player_score}")


    def instructions(self):
        global game_mode
        tutorial_input = input("Do you know how to play? Y/N: ")
        if tutorial_input.upper() == 'N':
            print("Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack. \n")
            print("If the cards are the same rank, it is War. Each player turns up three cards face down and one card face up. The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on.\n")
            print("https://en.wikipedia.org/wiki/War_(card_game)\n")
            game_mode = 'setup'
        elif tutorial_input.upper() == 'Y':
            print("No need for a tutorial then, good luck!")
            game_mode = 'setup'
        elif tutorial_input.upper() != 'Y' and tutorial_input.upper() != 'N':
            print("Please choose either Y/N.")

# game logic
game_on = True
game_mode = 'tutorial'
mydeck = Deck()
myboard = Board()

while game_on:
    print("Welcome to WAR!")
    if game_mode == 'tutorial':
        myboard.instructions()

    if game_mode == 'setup':
        player1 = input("Player 1, what is your name? ")
        player1_obj = Player(player1)
        print(f"Welcome {player1_obj.name}!")
        player2 = input("Player 2, what is your name? ")
        player2_obj = Player(player2)
        print(f"Welcome {player2_obj.name}!")
        game_mode = 'starting'

    if game_mode == 'starting':
        print("Hajime!")
        mydeck.gen_deck()
        mydeck.shuffle_deck()
        mydeck.deck_split()
        print("Cards have been dealt!")
        game_mode = 'fighting'
    
    if game_mode == 'fighting':
        while len(player1_obj.player_deck) > 0 and len(player2_obj.player_deck) > 0:
            print("WITNESSED!")
            myboard.play_round()
            input("Round over, press enter to continue.")
            print("---------- NEXT ROUND ----------")
        game_mode = 'endgame'
    
    if game_mode == 'endgame':
        print("Game over!")

        