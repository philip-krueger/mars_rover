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
                    self.y += 1
                if(moving == 'b'):
                    self.y -= 1
                if(moving == 'r'):
                    self.direction = 'E'
                if(moving == 'l'):
                    self.direction = 'W'

            elif(direction == 'S'):

                if(moving == 'f'):
                    self.y -= 1
                if(moving == 'b'):
                    self.y += 1
                if(moving == 'r'):
                    self.direction = 'W'
                if(moving == 'l'):
                   self.direction = 'E'

            elif (direction == 'E'):

                if(moving == 'f'):
                    self.x += 1
                if(moving == 'b'):
                    self.x -= 1
                if(moving == 'r'):
                    self.direction = 'S'
                if(moving == 'l'):
                    self.direction = 'N'

            elif (direction == 'W'):

                if(moving == 'f'):
                    self.x -= '1'
                if(moving == 'b'):
                    #doshit
                if(moving == 'r'):
                    #doshit
                if(moving == 'l'):
                    #doshit

    def print_current_location(self):



    def detect_obstacles(self):