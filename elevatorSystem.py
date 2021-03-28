from collections import deque
from elevator import Elevator


class ElevatorSystem(object):
    """ This class respresents the elevator system
    the elevator can go from the lowest floor to the highest floor
    number of elevator in the system is greater than 1
    """

    def __init__(self,num_elevator: int, lowest_floor: int, highest_floor: int):
        assert highest_floor > lowest_floor, " The highest floor should  be greater than lowest floor"

        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        """ The elevators object are stored in the elevator list"""
        self.elevators = []

        """ This would store the queue for each individual elevator in the system """
        self.elevator_queues = {}

        default_floor = lowest_floor

        for elevator_number in range(num_elevator):
            elevator = Elevator(elevator_number, default_floor)
            self.elevators.append(elevator)
            self.elevator_queues[elevator_number] = deque()

        """ This would store the tuple in the form of tuple(pickup floor, target floor)"""
        self.pickup_requests = deque()


    def status(self):
        """ This prints the status of each elevator """
        for elevator in self.elevators:
            elevator.status()


    def get_floor_and_target(self,elevator_id : int) -> (int,int):
        """This method return the information about the elevator using the elevator id
        about its current floor and target floor """

        assert 0 <= elevator_id <= len(self.elevators)-1, "Elevator of this id not in the system"

        elevator = self.elevators[elevator_id]
        floor = elevator.get_current_floor()
        target_floor = elevator.get_target_floor()

        return floor, target_floor

    def pickup_request(self, pickup_floor : int , direction:[-1,1]):
        """ This process the pickup by humans on any floor outside the lift when they make request.
        Direction 1 means going up while -1 means going down """

        assert pickup_floor <= self.highest_floor, "pickup floor should be lesser than highest floor"
        assert pickup_floor >= self.lowest_floor, "pickup floor should be greater than lowest floor"

        if pickup_floor == self.highest_floor:
            assert direction != 1, " Cannot go from highest floor to above"
        elif pickup_floor == self.lowest_floor:
            assert direction != -1, " Cannot go from lowest floor to below"


        self.pickup_requests.append((pickup_floor, direction ))


    def target_floor_request(self,elevator_id: int, target_floor: int):
        """Processes the pickup request coming from within the elevator when people press floor buttons inside elevator """

        assert target_floor <= self.highest_floor
        assert target_floor >= self.lowest_floor

        elevator = self.elevators[elevator_id]
        current_floor = elevator.get_current_floor()
        current_target_floor = elevator.get_target_floor()

        """ If there are no target in the queue of the elevator push the target directly"""
        """if target floor is between current floor and target floor then append left, Otherwise use first come first serve"""

        if current_target_floor is not None and target_floor not in self.elevator_queues[elevator_id]:
            if current_floor < current_target_floor:
                if current_floor < target_floor < current_target_floor:
                    self.elevator_queues[elevator_id].appendleft(target_floor)
                else:
                    self.elevator_queues[elevator_id].append(target_floor)
            else:
                if current_floor > target_floor > current_target_floor:
                    self.elevator_queues[elevator_id].appendleft(target_floor)
                else:
                    self.elevator_queues[elevator_id].append(target_floor)
        else:
            self.elevator_queues[elevator_id].append(target_floor)


    def step(self):
        """ Step elevator, if it reaches the target floor then set target floor None and remove the element from queue
        of the respective elevator"""
        self.__schedule_elevators()
        for elevator_id, elevator in enumerate(self.elevators):
            elevator.step()

            if elevator.get_current_floor() == elevator.get_target_floor():
                #print("Elevator : " + str(elevator_id) + " Door Opens ")
                #print("Elevator : " + str(elevator_id) + " Door Closes ")
                self.elevator_queues[elevator_id].popleft()
                self.elevators[elevator_id].set_target_floor(None)


    def __process_pickup_requests(self):
        """Process the incoming pickup request to proper target request and assign the relevant
        elevator from the system to the request"""

        to_remove = []
        for pickup_floor, direction in self.pickup_requests:
            possible_elevator = []

            """Elevators that are free or going in the same direction"""
            for elevator in self.elevators:
                if elevator.matches_request(pickup_floor, direction):
                    possible_elevator.append(elevator)

            if len(possible_elevator) > 0:
                #find the nearest elevator
                elevator_id = self.__find_nearest_elevator_id(possible_elevator, pickup_floor)
                self.target_floor_request(elevator_id, pickup_floor)
                to_remove.append((pickup_floor, direction))
            else:
                """Elevators that are going in the direction of the request."""
                comming_elevator = []
                for elevator in self.elevators:
                    if elevator.is_coming_to(pickup_floor):
                        comming_elevator.append(elevator)

                if len(comming_elevator) > 0:
                    #find the nearest elevator
                    elevator_id = self.__find_nearest_elevator_id(comming_elevator, pickup_floor)
                    self.target_floor_request(elevator_id, pickup_floor)
                    to_remove.append((pickup_floor, direction))

        for items in to_remove:
            self.pickup_requests.remove(items)



    def __find_nearest_elevator_id(self, possible_elevator: list, pickup_floor: int):
        """Find the nearest elevator id from the possible list of elevators to the pickup floor"""
        nearest_elevator = min(possible_elevator, key = lambda el : abs(el.get_current_floor() - pickup_floor))
        return nearest_elevator.elevator_id

    def __schedule_elevators(self):
        """ This sets the target floor for each of the elevators in the elevator system """
        self.__process_pickup_requests()
        for elevator_id, elevator in enumerate(self.elevators):
            if len(self.elevator_queues[elevator_id]) > 0:
                first_element = self.elevator_queues[elevator_id][0]
                elevator.set_target_floor(first_element)

    def hard_set(self,elevator_id:int, current_floor: int, target_floor = None):
        """ Implemented for testing """
        self.elevators[elevator_id].hard_set_current_floor(current_floor)
        self.elevators[elevator_id].set_target_floor(target_floor)
