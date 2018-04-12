import unittest
from marsrover import Rover


class mytest(unittest.TestCase):

    def setUp(self):
         self.erover = Rover(0, 0, 'N')

    def will_rover_move(self):
        move_command = ['f', 'f', 'f', 'r', 'f', 'l', 'f']  # output should be 1,4 E
        self.assertTrue(self.rover.move_rover(self.erover, move_command), msg=Rover.print_current_location())

    def rover_detects_obstacles(self):
        move_command = ['f', 'f', 'r', 'f', 'f']
        self.assertTrue(self.rover.move_rover(self.erover, move_command), msg=Rover.print_current_location())

    def check_wrong_commands(self):
        move_command = ['f', 'u', 'as', 'k', 'f']
        self.assertTrue(self.rover.move_rover(self.erover, move_command), msg=Rover.print_current_location())

    def planet_is_a_sphere(self):
        move_command = ['f', 'l', 'f', 'f']
        self.assertTrue(self.rover.move_rover(self.erover, move_command), msg=Rover.print_current_location())


if __name__ == '__main__':
    unittest.main()