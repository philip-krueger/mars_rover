from marsrover import Rover
import time

class testrover():

        erover = Rover(0, 0, 'N')
        move_command1 = ['f', 'r', 'f', 'l', 'f', 'r', 'f']  # output should be 2,2 E
        move_command2 = ['f', 'r', 'f', 'l', 'f', 'l', 'f', 'f']  # try to go over the grid in negativ
        Rover.move_rover(erover, move_command2)

        obstacle1 = [2, 2]
        obstacle2 = ([3, 3], [2, 2], [5, 5], [4, 5], [6, 8],)
