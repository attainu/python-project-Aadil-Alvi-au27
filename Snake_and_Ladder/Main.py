import Game

# function start will create instance of the call game and call's the method.
def start():
    # creating instance of the class Game from the module snake_and_ladder
    game_one = Game.Game()

    # running the game 
    input('Hit enter to start the game')
    game_one.play()

# calling the function start 
start()