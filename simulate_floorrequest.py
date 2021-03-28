import time
import random
from elevatorSystem import ElevatorSystem


def simulate_floorrequest():

    num_elevators = 3
    first_elevator = 0
    second_elevator = 1
    lowest_floor = 0
    highest_floor = 20
    es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)

    index = 0
    print("############################################################")
    while index <= 15:
        #print("AT  TIME  ", index)
        print("############################################################")

        """ Now we can assign some floor to any elevator randomly for simulation as well """
        floor = random.randint(lowest_floor,highest_floor)
        elevator_number = random.randint(0,num_elevators-1)
        print("Request from within the lift " + str(elevator_number) + " to go to " + str(floor))
        es.step()
        es.status()
        es.target_floor_request(elevator_number,floor)
        """ For just simulation purposes we assume for n randome seconds between 2 and 10, no new requests comes"""
        n = random.randint(2,10)

        for time in range(1,n):
            print("AT  TIME  ", index+time)
            es.step()
            es.status()
            print("Queue status for each elevator is: ")
            for elevator_number in range(len(es.elevators)):
                print(es.elevator_queues[elevator_number])

        index +=1
    print("############################################################")

if __name__ == "__main__":
    simulate_floorrequest()
