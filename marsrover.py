
import time

class Rover:

    move_command = []

    def __init__(self, x, y, direction):

        self.x = x
        self.y = y
        self.direction = direction

    def moving_screen(self):
        print("Mars Rover starting...")
        self.print_current_location()
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("moving along mars...")
        time.sleep(2)
        print("...")
        time.sleep(2)

    def move_rover(self, move_command):

        self.moving_screen()
        if self.direction == 'N'or self.direction == 'S' or self.direction == 'W' or self.direction == 'E':

            self.moveroverfunction(move_command)
        else:
            RuntimeError("Invalid Direction")
            exit()

    def print_current_location(self):
        print("Facing Direction: "+self.direction)
        print("Location: %d,%d" % (self.x, self.y))

    def moveroverfunction(self, move_command):
        for moving in move_command:

            #   Moving to North
            if self.direction == 'N':
                #   This is for wrapping the grid around a sphere
                #   When the Rover reaches the end of the grid it will continue on the other side, grid will be 10x10
                #   Will be the first check on every direction
                if moving == 'f' and self.x == 10:
                    self.x = 0

                if moving == 'f':
                    self.y += 1
                if moving == 'b':
                        self.y -= 1
                if moving == 'r':
                    self.direction = 'E'
                if moving == 'l':
                    self.direction = 'W'

            elif self.direction == 'S':
                if moving == 'f' and self.y == 0:
                    self.y = 10
                if moving == 'f':
                        self.y -= 1
                if moving == 'b':
                    self.y += 1
                if moving == 'r':
                    self.direction = 'W'
                if moving == 'l':
                    self.direction = 'E'

            elif self.direction == 'E':
                if moving == 'f' and self.x == 10:
                    self.x = 0
                if moving == 'f':
                    self.x += 1
                if moving == 'b':
                        self.x -= 1
                if moving == 'r':
                    self.direction = 'S'
                if moving == 'l':
                    self.direction = 'N'

            elif self.direction == 'W':
                if moving == 'f' and self.x == 0:
                    self.x = 10
                if moving == 'f':
                        self.x -= 1
                if moving == 'b':
                    self.x += 1
                if moving == 'r':
                    self.direction = 'N'
                if moving == 'l':
                    self.direction = 'S'

        if self.location_is_good():
            print("destination reached")
            self.print_current_location()
        else:
            exit()

    def location_is_good(self):


    def location_is_bad(self):
        print("Reached obstacle")
        print("Stopping at last possible point")
        self.print_current_location()
