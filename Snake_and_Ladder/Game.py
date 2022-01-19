# snake and ladder application
import random
import snake
import ladder
import gui_main

# class game is assigned with all the functinality of game.
class Game:
    for_Snakes = snake.Snakes()
    for_ladders = ladder.Ladders() 
    

    # welcome message 
    message = """
        Welcome to Snake and Ladder Game.
        Developed by: Mohd. Aadil Alvi

        Select Snake and Ladder data-type:
        --> Enter 1 to select GUI(Graphics User Interface) mode
        --> Enter 2 to give values manually in terminal.

        """
    print(message)

    option=int(input('\t'))
    print('\n')
    if option == 1:
        for_run=gui_main.run()
        for_run.Act()

    elif option == 2 :
        message = """
        Rules to follow for snake positions and ladder positions.
        --> There won't be a snake or ladder at 100.
        --> snake and ladder positions shouldn't exceed 100.
        --> There won't be multiple snake or ladder at the tail of the snake, or
            the end position of the ladder and the piece should go up or down accordingly.
        --> Snake and Ladder do not form an infinite loop.
        """
        print(message+'\n')

        snakes=for_Snakes.snakes_entries()
        ladders=for_ladders.ladders_entries()

        player_one_name = input('Enter player one name ')
        player_one_initial_position = 0
        player_one_final_position = 0

        player_two_name = input('Enter player two name ')
        player_two_initial_position = 0
        player_two_final_position = 0

    def play(self):
        while (self.player_one_final_position <= 100 or self.player_two_final_position <= 100) :
        # player one rolls the dice 
            print(self.player_one_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_one_final_position + dice_value <= 100 :
                self.player_one_final_position = self.player_one_final_position + dice_value
                print(self.player_one_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_one_initial_position)+' to the position '+str(self.player_one_final_position)+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # snake bite checking 
            if self.player_one_initial_position in self.snakes.keys():
                print('oh no......!!!!!!!, '+self.player_one_name+' got snake-bite by '+str(self.snakes[self.player_one_initial_position])+' positions')
                self.player_one_final_position = self.snakes[self.player_one_initial_position]
                print(self.player_one_name+' moved down to '+str(self.player_one_final_position)+' position due to snake bite'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # ladder luck checking
            if self.player_one_initial_position in self.ladders.keys():
                print('woo-hoo..!!, '+self.player_one_name+' got lucky to climb ladder to '+str(self.ladders[self.player_one_initial_position])+' position')
                self.player_one_final_position = self.ladders[self.player_one_initial_position]
                print(self.player_one_name+' moved up to '+str(self.player_one_final_position)+' position due to ladder'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # checking for winner 
            if (self.player_one_final_position == self.player_one_initial_position == 100) :
                print(self.player_one_name+' has won the game, Hurray!!!')
                break 
            

        # player two rolls the dice
            print(self.player_two_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_two_final_position + dice_value <= 100 :
                self.player_two_final_position = self.player_two_final_position + dice_value
                print(self.player_two_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_two_initial_position)+' to the position '+str(self.player_two_final_position)+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # snake bite checking 
            if self.player_two_initial_position in self.snakes.keys():
                print('oh no......!!!!!!!, '+self.player_two_name+' got snake-bite by '+str(self.snakes[self.player_two_initial_position])+' positions')
                self.player_two_final_position = self.snakes[self.player_two_initial_position]
                print(self.player_two_name+' moved down to '+str(self.player_two_final_position)+' position due to snake bite'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # ladder luck checking
            if self.player_two_initial_position in self.ladders.keys():
                print('woo-hoo..!!, '+self.player_two_name+' got lucky to climb ladder to '+str(self.ladders[self.player_two_initial_position])+' position')
                self.player_two_final_position = self.ladders[self.player_two_initial_position]
                print(self.player_two_name+' moved up to '+str(self.player_two_final_position)+' position due to ladder'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # checking for winner
            if (self.player_two_final_position == self.player_two_initial_position == 100) :
                print(self.player_two_name+' has won the game, Hurray!!!')
                break 

