import random
from phrase import Phrase


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
        random_phrase = self.phrases[random.randint(0,4)]
        self.active_phrase = Phrase(random_phrase)
        return self.active_phrase

    def start(self):
        #self.welcome()
        #while :
        #    Phrase.display()
        return self.get_random_phrase()

    def welcome():
        pass

    def get_guess():
        pass

    def game_over():
        pass

game = Game()
print(game.phrases)
#print(game.get_random_phrase())
print(game.start())
