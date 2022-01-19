class Ladders:
    def ladders_entries(self):
        # manual data entry for snake
         # manual data entry for ladder
        no_of_ladders = int(input('Enter total number of ladders in the game '))
        print('Starting position of the ladder should be lesser than the Ending position of the ladder')
        ladders = {}
        for i in range(no_of_ladders):
            key=int(input('Enter starting position of ladder '+ str(i+1)+'\t'))
            value=int(input('Enter ending position of ladder '+ str(i+1)+'\t'))
            if value > key:
                ladders[key]=value
                return ladders
            else:
                print('Invalid input, Ending position of ladder should be greater than Starting position of the ladder')
                break