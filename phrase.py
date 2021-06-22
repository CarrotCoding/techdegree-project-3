import game


class Phrase:

    def __init__(self, phrase):
        #The class should include an initializer or def __init__ that receives a
        #phrase parameter and holds this phrase in an instance attribute on the Phrase object.
        self.phrase = phrase.lower()
        #phrase: this is the actual phrase the Phrase object is representing.
        #This attribute should be set to the phrase parameter but converted to all lower case.

    def __str__(self):
        return self.phrase

    def __iter__(self):
        yield from self.phrase

    def display(self, phrase, letter):
        #display(): this prints out the phrase to the console with guessed letters
        #visibile and unguessed letters as underscores. For example, if the current
        #phrase is "hello world" and the user has guessed the letter "o", the output
        #should look like this: _ _ _ _ o    _ o _ _ _
        #display_phrase = []



        # phrase = blablabla
        # replaced_phrase
        # for letter in phrase:
            # letter = _
            # replaced_phrase.append(letter)
        # ' '.join(replaced_phrase)
        pass

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
