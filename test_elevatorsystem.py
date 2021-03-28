""" Unit Testing the code """
"""This tests the functionality of the elevator systems."""

import unittest
from elevatorSystem import ElevatorSystem


class ElevatorSystemTest(unittest.TestCase):
    def test_parameterssetting(self):
        """This tests getter setter functionality"""
        num_elevators = 1
        elevator_id = 0
        lowest_floor = 0
        highest_floor = 10
        es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
        self.assertEqual(len(es.elevators),num_elevators)
        self.assertEqual(es.lowest_floor,lowest_floor)
        self.assertEqual(es.highest_floor,highest_floor)

    def test_singleelevator_singlerequest(self):
        """This tests the requests from within the elevator for a system of one elevator only"""
        num_elevators = 1
        elevator_id = 0
        lowest_floor = 0
        highest_floor = 10
        es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
        es.target_floor_request(elevator_id,2)
        es.step()
        self.assertEqual(es.get_floor_and_target(elevator_id),(1,2))
        es.step()
        self.assertEqual(es.get_floor_and_target(elevator_id),(2,None))

    def test_two_elevators_same_direction(self):
        """This tests the requests from within the elevator for a system of two elevators, checking one elevator"""
        num_elevators = 2
        first_elevator = 0
        second_elevator = 1
        lowest_floor = 0
        highest_floor = 10
        es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
        es.target_floor_request(first_elevator,5)
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(1,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(2,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(3,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(4,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(5,None))
        es.target_floor_request(first_elevator,10) #this goes in the queue for the elevator
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(6,10))
        self.assertEqual(es.elevator_queues[first_elevator][0],10)
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(7,10))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(8,10))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(9,10))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(10,None))

    def test_two_elevators_different_direction(self):
        """This tests the requests from within the elevator for a system of two elevators, checking both elevator"""
        num_elevators = 2
        first_elevator = 0
        second_elevator = 1
        lowest_floor = 0
        highest_floor = 10
        es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
        es.target_floor_request(first_elevator,5)
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(1,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(2,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(3,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(4,5))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(5,None))
        es.target_floor_request(second_elevator,2)
        es.step()
        self.assertEqual(es.get_floor_and_target(second_elevator),(1,2))
        es.step()
        self.assertEqual(es.get_floor_and_target(second_elevator),(2,None))

    def test_pickup_request_two_elevators(self):
        """This tests the requests from different floors outside the elevator with direction."""
        num_elevators = 2
        first_elevator = 0
        second_elevator = 1
        lowest_floor = 0
        highest_floor = 10
        es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
        es.pickup_request(9,-1)
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(1,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(2,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(3,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(4,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(5,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(6,9))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(7,9))
        es.pickup_request(2,-1)
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(8,9))
        self.assertEqual(es.get_floor_and_target(second_elevator),(1,2))
        es.step()
        self.assertEqual(es.get_floor_and_target(first_elevator),(9,None))
        self.assertEqual(es.get_floor_and_target(second_elevator),(2,None))


if __name__ == "__main__":
    unittest.main()
