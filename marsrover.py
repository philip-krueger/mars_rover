class rover:

    move_command = []

    def __init__(self, x, y, direction):

        self.x = x
        self.y = y
        self.direction = direction

    def move_rover(self, direction, move_command):

        for moving in move_command:

            if(direction == 'N'):
                if(moving == 'f'):
                    #doshit
                if(moving == 'b'):
                    #doshit
                if(moving == 'r'):
                    #doshit
                if(moving == 'l'):
                    #doshit
            elif(direction == 'S'):

                if(moving == 'f'):
                    #doshit
                if(moving == 'b'):
                    #doshit
                if(moving == 'r'):
                    #doshit
                if(moving == 'l'):
                    #doshit
            elif (direction == 'E'):

                if(moving == 'f'):
                    #doshit
                if(moving == 'b'):
                    #doshit
                if(moving == 'r'):
                    #doshit
                if(moving == 'l'):
                    #doshit
            elif (direction == 'W'):

                if(moving == 'f'):
                    #doshit
                if(moving == 'b'):
                    #doshit
                if(moving == 'r'):
                    #doshit
                if(moving == 'l'):
                    #doshit

    def print_current_location(self):



    def detect_obstacles(self):