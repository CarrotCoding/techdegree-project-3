import game
import copy


class Phrase:

    def __init__(self, phrase):
        #The class should include an initializer or def __init__ that receives a
        #phrase parameter and holds this phrase in an instance attribute on the Phrase object.
        self.phrase = phrase.lower()
        #phrase: this is the actual phrase the Phrase object is representing.
        #This attribute should be set to the phrase parameter but converted to all lower case.
        self.display_phrase = []

    def __str__(self):
        return self.phrase

    def __iter__(self):
        yield from self.phrase

    def display(self, phrase, guesses):
        print(f"So far you've tried the follower letters: {', '.join(guesses).upper()}")
        self.display_phrase = []
        for letter in self.phrase:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if letter in alphabet and letter not in guesses:
                letter = "_ "
                self.display_phrase.append(letter)
            else:
                letter = letter + " "
                self.display_phrase.append(letter)
        print(''.join(self.display_phrase))


    def check_letter():

        #check_letter(): checks to see if the letter selected by the user matches a
        #letter in the phrase.

        # check to see if the letter selected by the user matches a letter in the phrase
        # letter in sentence (is True)
        # return dopamine
        # else
        # you lose a life
        # letter in guessed_letters (is True)
        # return error message
        pass

    def check_complete(self, guess, phrase):
        #check_complete(): checks to see if the whole phrase has been guessed.

        # if replaced_phrase == phrase:
            # you win
        pass
