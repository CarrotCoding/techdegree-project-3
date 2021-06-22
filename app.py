import game


#Import your Game class from the phrasehunter package.
#Create a new instance of the Game class and store this instance in a game variable.
#Call the start() method you create for your Game instance that kicks off the game loop,
#this should start the game in the console.
#Ensure you place your instance creation and method calls inside a Dunder Main statement.
#You must use OOP principles for the entire constructions game meaning no helper functions
#should be used outside of the classes built above.
#The entire game should run solely on creating an instance of a
#Game class and method calls within that instance.
if __name__ == '__main__':
    game = game.Game()
    print(game.phrases)
    #print(game.get_random_phrase())
    print(game.start())
