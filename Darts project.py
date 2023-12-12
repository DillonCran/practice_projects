# Scope: run through the ability to play Match or Cricket Darts

#base variables
test = False
game_on = True
game_over = False
num_of_players = 0
game_mode = '#'
players = {
    'Legend':['name','score','wins'],
    'Player1':['name','0',0],
    'Player2':['name','0',0],
    'Player3':['name','0',0],
    'Player4':['name','0',0],
    'Player5':['name','0',0],
    'Player6':['name','0',0],
    'Player7':['name','0',0],
    'Player8':['name','0',0],
    }


#base definitions for overall functionality
def choose_game():
    global game_mode
    while True:
        try:
            game_mode = input('what game would you like to play? (Cricket or Match): ').capitalize()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if game_mode not in ['Cricket', 'Match']:
            print('Not a supported game type')
            continue
        else:
            break

def player_count():
    #asks for number of players
    global num_of_players
    global players
    num_of_players = 0
    count = 1
    while True:
        try:
            num_of_players = int(input('How many players will be playing? (1-8): '))
        except ValueError:
            if num_of_players not in range(1,8+1):
                print('Not an accepted input, please select number of players (1-8): ')
                continue

        #asks for each players name and assigns them a class
        else:
            for x in range(1,num_of_players+1):
                name = input(f'Player {x}, What is your name? ')
                players[f'Player{count}'][0] = name
                count += 1
            break

def show_players():
    count = 1
    for num in range(1,num_of_players+1):
        player_key = f'Player{num}'
        player_stats = players[player_key]
        print(f'{player_stats[0]} has a score of {player_stats[1]}')
        count +=1

def clear_score():
    for num in range(1,num_of_players+1):
        player_key = f'Player{num}'
        player_stats = players[player_key]
        player_stats[1] = 0

def play_again():
    global game_over
    while True:
        try:
            play = input('Would you like to play again? (Yes/No): ').capitalize()

        except ValueError:
            print('An error has occured')
            continue

        if play not in ['Yes','No']:
            print('Please use a valid response (Yes/No)')
            continue
        if play == 'Yes':
            print('Okay!')
            game_mode = 'starting'
            break
        if play == 'No':
            print('Okay, hope you had fun!')
            game_over = True
            break
    
#classes for specific functions based on gametype
class Match():

    def __init__(self):
        pass

    def set_score():
        while True:
            try:
                score = int(input('What would you like your score to start at? (101,201, ... 701): '))

            except ValueError:
                if score not in [101,201,301,401,501,601,701]:
                    print('Please input an acceptable score (101,201, ... 701)')
                    continue
            else:
                for num in range(1,num_of_players+1):
                    player_key = f'Player{num}'
                    player_stats = players[player_key]
                    player_stats[1] = score
                break
        
    def turns():
        while True:
            for num in range(1,num_of_players+1):
                player_key = f'Player{num}'
                player_stats = players[player_key]
                try:
                    score = int(input(f'{player_stats[0]} What did you score?: '))
                except ValueError:
                    if int(score) == False:
                        print('Please input a valid score.')
                        continue
                if score > player_stats[1]:
                    print(f'You cannot score more than your current points ({player_stats[1]}), please input a valid score.')
                    continue
                if score < 1:
                    print('Please input a positive number.')
                    continue
                if player_stats[1] == 0:
                    player_stats[2] += 1
                    print(f'{player_stats[0]} now has a score of 0 and wins!')
                    return
                else:
                    player_stats[1] -= score
                    print(f'{player_stats[0]} now has a score of {player_stats[1]}')
                    if player_stats[1] <= 0:
                        players[player_key][2] += 1
                        print(f'{player_stats[0]} now has a score of 0 and wins!')
                        return

class Cricket():
    none_point = ' '
    one_point = '/'
    two_point = 'X'
    three_point = '⦻'

    top_score = 0
    leader = ''

    cricket_marks = {
        'Legend':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],'full marks'],
        'Player1':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player2':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player3':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player4':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player5':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'player6':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player7':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
        'Player8':[['name'],['Score',0],['bullseye',f'{none_point}'],['20',f'{none_point}'],['19',f'{none_point}'],['18',f'{none_point}'],['17',f'{none_point}'],['16',f'{none_point}'],['15',f'{none_point}'],0],
    }

    def __init__(self):
        pass

    def reset_cricketboard(self):
        for player in self.cricket_marks.keys():
            #reapplies the NONE MARK to all the data points past score, with a dummy last item
            self.cricket_marks[player][2:] = [[mark, self.none_point] for mark in ['bullseye','20', '19', '18', '17', '16', '15', '#']]
            #replace the dummy last item with the ALL MARKS flag
            self.cricket_marks[player][-1] = 0


    def apply_names(self):
        global num_of_players
        global players
        count = 1
        while True:
            for x in range(1,num_of_players+1):
                self.cricket_marks[f'Player{count}'][0][0] = players[f'Player{count}'][0]
                count += 1
            break


    def highlander(self):
        head = None
        for player in self.cricket_marks:
            #applies highest score to TOP SCORE variable
            if self.cricket_marks[player][1][1] > self.top_score:
                self.top_score = self.cricket_marks[player][1][1]
                head = player
            self.leader = self.cricket_marks[head][0][0] if head else None

    def full_marks(self):
        for player in self.cricket_marks:
            #determines if player has all their marks, and if so triggers flag
            if self.cricket_marks[player][2][1] == self.three_point and self.cricket_marks[player][3][1] == self.three_point and self.cricket_marks[player][4][1] == self.three_point and self.cricket_marks[player][5][1] == self.three_point and self.cricket_marks[player][6][1] == self.three_point and self.cricket_marks[player][7][1] == self.three_point and self.cricket_marks[player][8][1] == self.three_point:
                self.cricket_marks[player][9] = 1

    def gameplay(self):
        breakoff = False

        while not breakoff:
            for num in range(1,num_of_players+1):
                #asignes player info to variable
                player_key = f'Player{num}'
                player_stats = self.cricket_marks[player_key]
                try:
                    while True:
                        #determines top scores, leader, full marks flag
                        self.highlander()
                        self.full_marks()
                        #prints player info and requests board hit
                        print(f"{player_stats[0][0]}'s current score is {player_stats[1][1]} | bullseye:{player_stats[2][1]} 20:{player_stats[3][1]} 19:{player_stats[4][1]} 18:{player_stats[5][1]} 17:{player_stats[6][1]} 16:{player_stats[7][1]} 15:{player_stats[8][1]}" )
                        hit = input(f'{player_stats[0][0]} What did you hit?: ')
                        if hit not in ['bullseye','20','19','18','17','16','15']:
                            print('Please input a valid target on the board.')
                        else:
                            break

                except ValueError:
                    print('Please use a valid input')
                    continue
                
                #checks to see if player has win conditions before applying points
                if player_stats[0][0] == self.leader and player_stats[9] == 1:
                    players[player_key][2] += 1
                    print(f'{player_stats[0][0]} wins with a score of {player_stats[1][1]}!.')
                    print(f'They now have {str(players[player_key][2])} wins!')
                    print('Congratulations!')
                    breakoff = True
                    break
                
                #applies marks/score hit
                if hit.lower() == 'bullseye':
                    if player_stats[2][1] == self.none_point:
                        player_stats[2][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[2][1]} mark for bullseye')
                        continue
                    if player_stats[2][1] == self.one_point:
                        player_stats[2][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[2][1]} mark for bullseye')
                        continue
                    if player_stats[2][1] == self.two_point:
                        player_stats[2][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[2][1]} mark for bullseye')
                        continue
                    if player_stats[2][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for bullseye!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '20':
                    if player_stats[3][1] == self.none_point:
                        player_stats[3][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[3][1]} mark for 20s')
                        continue
                    if player_stats[3][1] == self.one_point:
                        player_stats[3][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[3][1]} mark for 20s')
                        continue
                    if player_stats[3][1] == self.two_point:
                        player_stats[3][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[3][1]} mark for 20s')
                        continue
                    if player_stats[3][1] == self.three_point:
                        while True:
                            score = input('You have all your marks for 20s!  How much did you score?: ')
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '19':
                    if player_stats[4][1] == self.none_point:
                        player_stats[4][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[4][1]} mark for 19s')
                        continue
                    if player_stats[4][1] == self.one_point:
                        player_stats[4][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[4][1]} mark for 19s')
                        continue
                    if player_stats[4][1] == self.two_point:
                        player_stats[4][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[4][1]} mark for 19s')
                        continue
                    if player_stats[4][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for 19s!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '18':
                    if player_stats[5][1] == self.none_point:
                        player_stats[5][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[5][1]} mark for 18s')
                        continue
                    if player_stats[5][1] == self.one_point:
                        player_stats[5][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[5][1]} mark for 18s')
                        continue
                    if player_stats[5][1] == self.two_point:
                        player_stats[5][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[5][1]} mark for 18s')
                        continue
                    if player_stats[5][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for 18s!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '17':
                    if player_stats[6][1] == self.none_point:
                        player_stats[6][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[6][1]} mark for 17s')
                        continue
                    if player_stats[6][1] == self.one_point:
                        player_stats[6][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[6][1]} mark for 17s')
                        continue
                    if player_stats[6][1] == self.two_point:
                        player_stats[6][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[6][1]} mark for 17s')
                        continue
                    if player_stats[6][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for 17s!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '16':
                    if player_stats[7][1] == self.none_point:
                        player_stats[7][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[7][1]} mark for 16s')
                        continue
                    if player_stats[7][1] == self.one_point:
                        player_stats[7][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[7][1]} mark for 16s')
                        continue
                    if player_stats[7][1] == self.two_point:
                        player_stats[7][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[7][1]} mark for 16s')
                        continue
                    if player_stats[7][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for 16s!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue
                if hit == '15':
                    if player_stats[8][1] == self.none_point:
                        player_stats[8][1] = self.one_point
                        print(f'{player_stats[0][0]} now has {player_stats[8][1]} mark for 15s')
                        continue
                    if player_stats[8][1] == self.one_point:
                        player_stats[8][1] = self.two_point
                        print(f'{player_stats[0][0]} now has {player_stats[8][1]} mark for 15s')
                        continue
                    if player_stats[8][1] == self.two_point:
                        player_stats[8][1] = self.three_point
                        print(f'{player_stats[0][0]} now has {player_stats[8][1]} mark for 15s')
                        continue
                    if player_stats[8][1] == self.three_point:
                        while True:
                            score = int(input('You have all your marks for 15s!  How much did you score?: '))
                            try:
                                score = int(score)
                                break
                            except ValueError:
                                print('Please input a number')

                        player_stats[1][1] += score
                        print(f'{player_stats[0][0]} now has a score of {player_stats[1][1]}')
                        continue


# Game logic starts here
print('\n')
print('\n')
print('Welcome to Darts!')

while game_on:

    #logic to quit game
    if game_over:
        print('Game over')
        break

    #asks for # of users
    player_count()

    game_mode = 'starting'

    if game_mode == 'starting':
        #Asks user to pick game mode
        choose_game()
        
    #game logic for Cricket
    if game_mode == 'Cricket':
        cricket = Cricket()
        cricket.apply_names()
        cricket.gameplay()
        cricket.reset_cricketboard()
        play_again()

    #game logic for Match
    if game_mode == 'Match':
        Match.set_score()
        show_players()
        Match.turns()
        clear_score()
        play_again()
    
