import time
import random
from elevatorSystem import ElevatorSystem


def simulate_pickuprequest():
    """ This method simulate the requests coming from each floor from different people, on different floors to go in different floors"""
    num_elevators = 4
    first_elevator = 0
    second_elevator = 1
    lowest_floor = 0
    highest_floor = 20
    es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)

    index = 0
    print("############################################################")
    while index <= 15:
        print("############################################################")
        """ Randomly select the floor from where the request is coming, and direction. If the floor is lowest or highest than direction of request is not randomly selected."""
        floor = random.randint(lowest_floor,highest_floor)
        if floor == lowest_floor:
            direction = 1
        elif floor == highest_floor:
            direction = -1
        else:
            direction = random.choice((-1,1))

        es.status()
        print("Request from floor " + str(floor) + " in the direction " + str(direction))
        es.pickup_request(floor,direction)
        print(es.pickup_requests)
        """ For just simulation purposes we assume for n randome seconds between 2 and 10, no new requests comes"""
        n = random.randint(2,10)

        for time in range(1,n):
            print("AT  TIME  ", index+time)
            es.step()
            es.status()
            print(es.pickup_requests)
            print(es.elevator_queues[0])

        index +=1
    print("############################################################")

if __name__ == "__main__":
    simulate_pickuprequest()
