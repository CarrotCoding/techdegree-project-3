import random
from phrase import Phrase
import pdb
#pdb.set_trace()




#The Game instance might be responsible for things like: starting the game loop,
#getting player's input() guesses to pass to a Phrase object to perform its
#responsibilities against, determining if a win/loss happens after the player
#runs out of turns or the phrase is completely guessed.


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
        "All your base are belong to us",
        "FINISH HIM",
        "War never changes",
        "Endure and survive",
        "Stay awhile and listen"
        ]
        self.active_phrase = None
        self.user_phrase = []
        self.guesses = []

    def get_random_phrase(self):
        #get_random_phrase(): this method randomly retrieves one of
        #the phrases stored in the phrases list and returns it.
        #random_phrase = self.phrases[random.randint(0,4)]
        self.active_phrase = Phrase(self.phrases[random.randint(0,4)])
        return self.active_phrase

    def start(self):
        self.get_random_phrase()
        self.welcome()
        while self.missed < 5:
            #or (self.user_phrase = self.active_phrase)
            #add the user_phrase variable when it's set instead of the xxxx
            if self.guesses:
                self.active_phrase.display(self.user_phrase, self.guesses)
            self.get_guess()
            #the len(self.guesses)-1 checks whether the last letter added to the list is in the active_phrase
            if self.guesses[len(self.guesses)-1] not in self.active_phrase:
                self.missed += 1
                self.lives_left(self.missed)
            else:
                self.user_phrase.append(self.guesses[len(self.guesses)-1])
                print("Boom, another letter down, let's go for the win")
            



    def welcome(self):
        print("*********************************************************************")
        print("*******                                                       *******")
        print("*******              Welcome to PHRASE HUNTERSSS              *******")
        print("*******                                                       *******")
        print("*******  Where all your favorite game quotes can kill you ;)  *******\n")


    def get_guess(self):
        try:
            user_letter_guess = input("What letter would you like to try?\n").lower()
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            #this is the validation to make sure the user input is:
            #1 letter long, it is a letter and it hasn't been tried before
            if len(user_letter_guess) == 1 and user_letter_guess in alphabet and user_letter_guess not in self.guesses:
                self.guesses.append(user_letter_guess)
            else:
                raise ValueError
        except:
            print("Uh, oh.... that doesn't seem to be a single letter or you've tried this letter already, please try again")
            self.get_guess()


    def lives_left(self, missed):
        if self.missed < 4:
            print(f"Ouch, that hurt, only {5-self.missed} lives left")
        elif self.missed == 4:
            print(f"Ouch, that hurt, only {5-self.missed} life left, make it count!")
        else:
            self.game_over()


    def game_over(self):
        if self.missed < 5:
            print("Congratulations you've won!")
            self.try_again()
        else:
            print ("You're dead, oh noes!")
            self.try_again()


    def try_again(self):
        try:
            user_try_again = input("Would you like to play again... (y)es or (n)o\n").lower()
            if user_try_again in ["y", "yes"]:
                self.missed = 0
                self.active_phrase = None
                self.user_phrase = []
                self.guesses = []
                self.start()
            elif user_try_again in ["n" or "no"]:
                print("Thank you for playing Phrase Hunters")
            else:
                raise ValueError
        except:
            print("You seem to have filled in something other than (y)es or (n)o. Please try again")
            self.try_again()
