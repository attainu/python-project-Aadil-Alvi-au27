class Snakes:
    
    def snakes_entries(self):
        snakes = {}
        no_of_snakes = int(input('Enter total number of snakes in the game '))
        print('Head position of snake should be greater than Tail position of the snake')
        for i in range(no_of_snakes):
            key=int(input('Enter Head position of snake '+ str(i+1)+'\t'))
            value=int(input('Enter Tail position of snake '+ str(i+1)+'\t'))
            if value < key:
                snakes[key]=value
                return snakes
            else:
                print('Invalid input, Head position of snake should be greater than Tail position of the snake')
                break
            
   
