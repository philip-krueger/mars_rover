
import time

class Rover:

    move_command = []

    def __init__(self, x, y, direction):

        self.x = x
        self.y = y
        self.direction = direction

    def checkStartingPoint(self, start_x, start_y, start_direction):

        possible_directions = ['N', 'S', 'W', 'E']
        if start_x >= 0 <= 10 and start_y >= 0 <= 10 and start_direction in possible_directions:
            return True
        else:
            return False

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

    def print_obstacle_detected(self):
        print("obstacle detected")
        print("staying at last possible location")
        self.print_current_location()
        exit()

    def print_current_location(self):
        print("Facing Direction: "+self.direction)
        print("Location: %d,%d" % (self.x, self.y))

    def detect_obstacle(self, moving):
        obstacle2 = ([3, 3], [2, 2], [5, 5], [4, 5], [6, 8])

        if self.direction == 'N':
            if moving == 'f':
                tempy = self.y
                tempy =+ 1
                if [self.x, tempy] in obstacle2:
                    return True
                else:
                    return False
            else:
                tempy = self.y
                tempy =- 1
                if [self.x, tempy] in obstacle2:
                    return True
                else:
                    return False
        elif self.direction == 'S':
            if moving == 'f':
                tempy = self.y
                tempy =- 1
                if [self.x, tempy] in obstacle2:
                    return True
                else:
                    return False
            else:
                tempy = self.y
                tempy =+ 1
                if [self.x, tempy] in obstacle2:
                    return True
                else:
                    return False
        elif self.direction == 'W':
            if moving == 'f':
                tempx = self.x
                tempx =- 1
                if [tempx, self.y] in obstacle2:
                    return True
                else:
                    return False
            else:
                tempx = self.x
                tempx =+ 1
                if [tempx, self.y] in obstacle2:
                    return True
                else:
                    return False
        elif self.direction == 'E':
            if moving == 'f':
                tempx = self.x
                tempx =+ 1
                if [tempx, self.y] in obstacle2:
                    return True
                else:
                    return False
            else:
                tempx = self.x
                tempx =- 1
                if [tempx, self.y] in obstacle2:
                    return True
                else:
                    return False

    def move_rover(self, move_command):
        self.print_current_location()
        for moving in move_command:

            #   North
            if self.direction == 'N':
                #   This is for wrapping the grid around a sphere
                #   When the Rover reaches the end of the grid it will continue on the other side, grid will be 10x10
                #   Will be the first check on every direction
                if moving == 'f' and self.x > 10:
                    self.x = 0
                #   Before every movement wether its back or forward, it will check for obstacles
                #   in function detect_obstacles is a predefined array of obstacles
                if moving == 'f':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected
                    else:
                        self.y += 1
                if moving == 'b':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected()
                    else:
                        self.y -= 1
                if moving == 'r':
                    self.direction = 'E'
                if moving == 'l':
                    self.direction = 'W'
            #   South
            elif self.direction == 'S':
                if moving == 'f' and self.y < 0:
                    self.y = 10

                if moving == 'f':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected()
                    else:
                        self.y -= 1
                if moving == 'b':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected()
                    else:
                        self.y += 1
                if moving == 'r':
                    self.direction = 'W'
                if moving == 'l':
                    self.direction = 'E'
            #   East
            elif self.direction == 'E':
                if moving == 'f' and self.x > 10:
                    self.x = 0

                if moving == 'f':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected()
                    else:
                        self.x += 1
                if moving == 'b':
                    if self.detect_obstacle(moving):
                        self.print_obstacle_detected()
                    else:
                        self.x -= 1
                if moving == 'r':
                    self.direction = 'S'
                if moving == 'l':
                    self.direction = 'N'
            #   West
            elif self.direction == 'W':
                if moving == 'f' and self.x < 0:
                    self.x = 10

                if moving == 'f':
                    if self.detect_obstacle():
                        self.print_obstacle_detected()
                    else:
                        self.x -= 1
                if moving == 'b':
                    if self.detect_obstacle():
                        self.print_obstacle_detected()
                    else:
                        self.x += 1
                if moving == 'r':
                    self.direction = 'N'
                if moving == 'l':
                    self.direction = 'S'

        # One problem is when the rover reaches the end of the grid and goes over the grid
        # If its the last value in the array it will not go in the check of the loop again
        # So I implemented a check after the for-loop to set the values if out of grid
        if self.direction == 'N' and self.y > 10:
            self.y = 0
        elif self.direction == 'S' and self.y < 0:
            self.y = 10
        elif self.direction == 'W'and self.x < 0:
            self.x = 10
        elif self.direction == 'E' and self.x > 10:
            self.x = 0
        self.print_current_location()



