import random
from phrase import Phrase
import pdb



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
        #the phrase to compare to
        self.user_phrase = []
        #guesses: This is a list that contains the letters guessed by the user.
        self.guesses = []

    def get_random_phrase(self):
        #get_random_phrase(): this method randomly retrieves one of
        #the phrases stored in the phrases list and returns it.
        random_phrase = self.phrases[random.randint(0,4)]
        self.active_phrase = Phrase(random_phrase)
        return self.active_phrase

    def start(self):
        self.get_random_phrase()
        self.welcome()
        while self.missed < 5:
            #or (self.user_phrase = self.active_phrase)
            #add the user_phrase variable when it's set instead of the xxxx
            self.get_guess()
            if self.guesses[len(self.guesses)-1] not in self.active_phrase:
                self.missed += 1
                print(f"Ouch, that hurt, only {5-self.missed} lives left")
        #calls the get_guess method, adds the user's guess to guesses,
        #increments the number of missed by one if the guess is incorrect,
        #calls the game_over method.
        self.game_over()
        #self.welcome()
        #while :
        #    Phrase.display()


    def welcome(self):
        print("*********************************************************************")
        print("*******                                                       *******")
        print("*******              Welcome to PHRASE HUNTERSSS              *******")
        print("*******                                                       *******")
        print("*******  Where all your favorite game quotes can kill you ;)  *******\n")
        #welcome(): this method prints a friendly welcome message to
        #the user at the start of the game

    def get_guess(self):
        try:
            user_letter_guess = input("What letter would you like to try?\n").lower()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if len(user_letter_guess) == 1 and user_letter_guess in alphabet:
                self.guesses.append(user_letter_guess)
            else:
                raise ValueError
        except:
            print("Uh, oh.... that doesn't seem to be a single letter, please try again")
            self.get_guess()


    def game_over(self):
        if self.missed < 5:
            print("Congratulations you've won!")
            self.try_again()
        else:
            print ("You're dead, oh noes!")
            self.try_again()

    def try_again(self):
        try:
            pdb.set_trace()
            user_try_again = input("Would you like to play again... (y)es or (n)o\n").lower()
            if user_try_again == "y" or "yes":
                self.missed = 0
                self.active_phrase = None
                self.user_phrase = []
                self.guesses = []
                self.start()
            elif user_try_again == "n" or "no":
                print("Thank you for playing Phrase Hunters")
            else:
                raise ValueError
        except:
            print("You seem to have filled in something other than (y)es or (n)o. Please try again")
