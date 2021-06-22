import random
from phrase import Phrase



#The Game instance might be responsible for things like: starting the game loop,
#getting player's input() guesses to pass to a Phrase object to perform its
#responsibilities against, determining if a win/loss happens after the player
#runs out of turns or the phrase is completely guessed.


class Game:
    def __init__(self):
        #missed: used to track the number of incorrect guesses by the user.
        #The initial value is 0 since no guesses have been made at the start of the game.
        self.missed = 0
        #phrases: a list of five Phrase objects to use with the game.
        #A phrase should only include letters and spaces -- no numbers,
        #puntuation or other special characters.
        self.phrases = [
        "All your base are belong to us",
        "FINISH HIM",
        "War never changes",
        "Endure and survive",
        "Stay awhile and listen"
        ]
        #active_phrase: This is the Phrase object that's currently in play.
        #The initial value will be None. Within the start() method,
        #this property will be set to the Phrase object returned from a
        #call to the get_random_phrase() method.
        self.active_phrase = None
        #guesses: This is a list that contains the letters guessed by the user.
        self.guesses = []

    def get_random_phrase(self):
        #get_random_phrase(): this method randomly retrieves one of
        #the phrases stored in the phrases list and returns it.
        random_phrase = self.phrases[random.randint(0,len(self.phrases)-1)]
        self.active_phrase = Phrase(random_phrase)
        return self.active_phrase

    def start(self):
        #start(): Calls the welcome method, creates the game loop,
        #calls the get_guess method, adds the user's guess to guesses,
        #increments the number of missed by one if the guess is incorrect,
        #calls the game_over method.
        #self.welcome()
        #while :
        #    Phrase.display()
        return self.get_random_phrase()

    def welcome():
        #welcome(): this method prints a friendly welcome message to
        #the user at the start of the game
        pass

    def get_guess():
        #get_guess(): this method gets the guess from a user and
        #records it in the guesses attribute
        pass

    def game_over():
        #game_over(): this method displays a friendly win or loss message and ends the game.
        pass
