#!/usr/bin/python3
""" Cards: The war game """
import random
from copy import copy
import sys

### <INITIALIZATIONS> ###
suit = ["diamonds", "hearts", "Spades", "Clubs"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
rank = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "King", "Queen", "Jack", "Ace"]
cards = []
### </INITIALIZATIONS> ###

### <CLASSES> ###


class Player():
    """
        Gives info of the player.
        e.g: name, collected points, cards
    """

##############################################################################################################################################################################################
    def __init__(self, name, cards, board, face_up=None, points=0): #points are useless for "war" game
        self.name = name
        self.points = points
        self.cards = cards
        self.face_up = face_up ##the drawn face-up card in WAR
        self.board = board

##############################################################################################################################################################################################
    def win(self):
        """
            Announces the winner.
            Ends the game.
        """
        print(f"{self.name} Won the game! Amazing!")
        self.board.end()
        return

##############################################################################################################################################################################################
    def show_face_up(self):
        """
            Shows the last put card by the player
            Not so useful but I'm leaving it here
        """
        return (self.face_up)


class Board():
    """
        This is the game's layout.
        There's a command line interpreter here for playing, resuming, quitting, naming the players.
    """

##############################################################################################################################################################################################
    def __init__(self, reset=0):
        """
            Initializes/resets the game's setup.
                Shuffles cards
                names players
                distributes cards to players
            Starts the game.
        """
        self.cards_on_board = []
        random.shuffle(cards)
        self.player1_name = input("Enter player 1's name: ")
        self.player2_name = input("Enter player 2's name: ")
        self.player1 = Player(self.player1_name, cards[:26], self)
        self.player2 = Player(self.player2_name, cards[26:], self)
        self.reset = reset
        self.draw = 0
        self.start()

##############################################################################################################################################################################################
    def display(self):
        """
            Displays the cards which players have put on the board.
            Might not be useful much but can be used to see how game went
        """
        print("Cards on board are:\n", self.cards_on_board)

##############################################################################################################################################################################################    
    def start(self):
        """
            Starts the game. Asks before starting the execution.
        """
        start = input("Ready? (y/n): ")
        if start == "y":
            print("\n\nLet's get started!\n")
            self.play()
            return
        elif start == "n":
            print("Thank you for playing.\n")
        else:
            print("\n\nInvalid choice. Please try again\n")
            self.start()
            return

##############################################################################################################################################################################################    
    def play(self):
        """
            The main gameplay.
            1. Each player draws face up.
            2. They compare the values of ranks.
            3. If:
                A. player 1 > player 2
                    He takes all cards in his stack.
                    The game plays again
                B. player 1 = player 2
                    War is declared
                    Method war() starts
            4. Whoever runs out of cards loses.
        """
        while len(self.player1.cards) > 0 and len(self.player2.cards) > 0:
            self.player1.face_up = self.player1.cards.pop(0) ## Player 1 draws face up
            print(f"{self.player1.name} draws {self.player1.face_up}\n")
            self.player2.face_up = self.player2.cards.pop(0) ## Player 2 draws face up
            print(f"{self.player2.name} draws {self.player2.face_up}\n")
            self.cards_on_board += [self.player1.face_up, self.player2.face_up]
            self.compare()
            self.draw += 1
            if self.draw == 100: ## LIMIT the number of turns played without a war.
                print("DRAW!! PLAYERS HAVEN'T HAD WARS SINCE 100 TURNS AND GAME HAD TO END IN A DRAW BY DEFAULT")
                self.end()
                return
        if len(self.player1.cards) == 0:
            self.player2.win()
        else:
            self.player1.win()

##############################################################################################################################################################################################
    def compare(self):
        if self.player1.face_up.value == self.player2.face_up.value: ## Tie
            self.draw = 0
            self.tie() ## War declared
            return
        elif max(self.player1.face_up.value, self.player2.face_up.value) == self.player1.face_up.value: ## if player 1's card value > player 2's card value
            print(f"{self.player1.name} has won this round, and took all cards")
            self.player1.cards += [copy(crd) for crd in self.cards_on_board] ## Player 1 gets the cards
            self.cards_on_board = []
            print(f"{self.player1.name}'s cards are {len(self.player1.cards)} and they are:\n")
            print(f"{[str(crd) for crd in self.player1.cards]}" + "\n\n--\n")
            print(f"meanwhile {self.player2.name} has {len(self.player2.cards)} cards.\n")
        elif max(self.player1.face_up.value, self.player2.face_up.value) == self.player2.face_up.value: ## if player 2's card value > player 1's card value
            print(f"{self.player2.name} has won this round, and took all cards")
            self.player2.cards += [copy(crd) for crd in self.cards_on_board] ## Player 2 gets the cards
            self.cards_on_board = []
            print(f"{self.player2.name}'s cards are {len(self.player2.cards)} and they are:\n")
            print(f"{[str(crd) for crd in self.player2.cards]}" + "\n\n--\n")
            print(f"meanwhile {self.player1.name} has {len(self.player1.cards)} cards.\n")

##############################################################################################################################################################################################
    def tie(self):
        """
            Declares the war.
            Checks if players have enough cards to draw 3 cards
                Win if ran out of cards (0 cards before drawing 3 cards)
                Leave one card and draw the rest face down if lower than or equal to 3
            Each player Draws 3 cards
            Then players start playing again over all the cards
        """
        print(f"WAR DECLARED")

        ### CHECKS IF PLAYER 1 HAS ENOUGH CARDS TO DRAW THE FACE DOWN CARDS. PLAYER 2 WINS IF NO CARDS BEFORE DRAWING ###

        if len(self.player1.cards) <= 3 and len(self.player1.cards) != 0: ## When player 1 has cards but lower than 3
            self.cards_on_board += [copy(crd) for crd in self.player1.cards[:len(self.player1.cards) - 1]] ## player 1 draws cards and leaves one with him
            print(f"{self.player1.name} is running out of cards and is drawing {len(self.player1.cards) - 1} cards")
            del self.player1.cards[:len(self.player1.cards) - 1]
        elif len(self.player1.cards) == 0: ## When player 1 has no cards in the war
            print(f"{self.player1.name} ran out of cards.\n")
        else:
            self.cards_on_board += [copy(crd) for crd in self.player1.cards[:3]] ## Player 1 draws 3 cards normally and continues playing
            del self.player1.cards[:3]
            print(f"{self.player1.name} draws 3 cards face down")
        
        ### CHECKS IF PLAYER 2 HAS ENOUGH CARDS TO DRAW THE FACE DOWN CARDS. PLAYER 1 WINS IF NO CARDS BEFORE DRAWING ###

        if len(self.player2.cards) <= 3 and len(self.player2.cards) != 0: ## When player 2 has cards but lower than 3
            self.cards_on_board += [copy(crd) for crd in self.player2.cards[:len(self.player2.cards) - 1]] ## player 2 draws cards and leaves one with him
            print(f"{self.player2.name} is running out of cards and is drawing {len(self.player2.cards) - 1} cards")
            del self.player2.cards[:len(self.player2.cards) - 1]
        elif len(self.player2.cards) == 0: ## When player 2 has no cards in the war
            print(f"{self.player2.name} ran out of cards.\n")
        else:
            self.cards_on_board += [copy(crd) for crd in self.player2.cards[:3]] ## Player 2 draws 3 cards normally and continues playing
            del self.player2.cards[:3]
            print(f"{self.player2.name} draws 3 cards face down")

##############################################################################################################################################################################################    
    def end(self):
        """
            Ends the game and prompts if the game wants to be replayed or not
        """
        prompt = input("Game over! Want to play again? (y/n): ")
        if prompt == 'n':
            print("Thank you for playing.\n")
            return
        elif prompt == 'y':
            print("Awesome!\n")
            self.reset = 1
            return
        else:
            print("Invalid choice. Try again.\n")
            self.end()
            return
    
##############################################################################################################################################################################################
    def __repr__(self):
        return ("Game ended.")


class Card():
    """
        This is the class where all cards have identification
    """

##############################################################################################################################################################################################
    def __init__(self, rank, suit, value):
        """
            Initializes the attributes of the cards
        """
        self.suit = suit
        self.rank = rank
        self.value = value

##############################################################################################################################################################################################    
    def create(self):
        """ 
            Creates the cards. (I think this is unused after the __str__ method has proven being better)
        """
        return (f"{self.rank} of {self.suit}")

##############################################################################################################################################################################################
    def __str__(self):
        """
            Cards' identification
        """
        return (f"{self.rank} of {self.suit}")


### </CLASSES> ###

def create_cards(cards):
    """
        Creates 52 instances of the class 'card' with all names and values
    """
    cards = []
    for i in range(len(suit)):
        for j in range(13):
            cards.append(Card(rank[j], suit[i], value[j]))
    return (cards)

cards = create_cards(cards) #appends all the class objects to the "cards" list
Start_Game = Board()
while Start_Game.reset == 1:
    print("GON RESET NOW\n")
    Start_Game = Board()
print("\n\nTHE END REACHES HERE\n")
