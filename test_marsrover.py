from marsrover import Rover
import time


class testrover():

        move_command1 = ['f', 'r', 'f', 'l', 'f', 'r', 'f']  # output should be 2,2 E
        move_command2 = ['f', 'r', 'f', 'l', 'f', 'l', 'f', 'f']  # try to go over the grid in negativ
        move_command3 = ['f', 'f', 'f', 'r', 'f', 'f' 'f']  # Should reach an obstacle

        # Function checkStartinPoint takes initial pararmeters and checks them for their validity
        start_x = 0
        start_y = 0
        start_direction = 'N'

        if Rover.checkStartingPoint(Rover, start_x, start_y, start_direction):

            erover = Rover(start_x, start_y, start_direction)
            Rover.move_rover(erover, move_command1)

        else:
            print("Wrong Starting Points and/or direction")
            exit()

