""" Unit Testing the code """
"""This is for testing the functionalities of the elevator object only. It tests singl elevator functionalities"""

import unittest
from elevatorSystem import Elevator


class ElevatorTest(unittest.TestCase):
    def test_elevator_movement(self):
        """This tests set target floor and current floor functionality"""
        elevator_id = 0
        current_floor = 0
        el = Elevator(elevator_id, current_floor)
        self.assertEqual(el.get_current_floor(),0)
        el.set_target_floor(5)
        self.assertEqual(el.get_target_floor(),5)
        self.assertEqual(el.get_direction(),1)
        el.step()
        self.assertEqual(el.get_current_floor(),1)
        el.step()
        el.step()
        el.step()
        self.assertEqual(el.get_current_floor(),4)
        el.step()
        self.assertEqual(el.get_current_floor(),5)

    def test_match_request_method(self):
        """This tests matches request functionality and checks whether elevator is going in right direction or not"""
        elevator_id = 1
        current_floor = 4
        el = Elevator(elevator_id, current_floor)
        # right now the target floor is None
        direction_up = 1
        direction_down = -1

        floor = 2
        self.assertEqual(el.matches_request(floor,direction_up),True)
        floor = -2
        self.assertEqual(el.matches_request(floor,direction_up),True)
        el.set_target_floor(10)
        floor = 4
        self.assertEqual(el.matches_request(floor,direction_up),False)
        floor = 5
        self.assertEqual(el.matches_request(floor,direction_up),True)
        floor = 8
        self.assertEqual(el.matches_request(floor,direction_down),False)


if __name__ == "__main__":
    unittest.main()
