import unittest
from marsrover import Rover


class mytest(unittest.TestCase):

    def setUp(self):
         self.erover = Rover(0, 0, 'N')

    def tearDown(self):
        print(self.i)
        print('\n+++++++++++++++++++++++++\n+++++++++++++++++++++++++')



    def test_will_rover_move(self):
        self.i = '1'
        move_command = ['f', 'f', 'f', 'r', 'f', 'l', 'f']  # output should be 1,4 E
        self.assertTrue(Rover.move_rover(self.erover, move_command), msg=Rover.print_current_location(self.erover))

    def test_rover_detects_obstacles(self):
        self.i = '2'
        move_command = ['f', 'f', 'r', 'f', 'f']
        self.assertTrue(Rover.move_rover(self.erover, move_command), msg=Rover.print_current_location(self.erover))

    def test_check_wrong_commands(self):
        self.i = '3'
        move_command = ['f', 'u', 'as', 'k', 'f']
        self.assertTrue(Rover.move_rover(self.erover, move_command), msg=Rover.print_current_location(self.erover))

    def test_planet_is_a_sphere(self):
        self.i = '4'
        move_command = ['f', 'l', 'f']
        self.assertTrue(Rover.move_rover(self.erover, move_command), msg=Rover.print_current_location(self.erover))


if __name__ == '__main__':
    unittest.main()