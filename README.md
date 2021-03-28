# ElevatorSystem Design 
** Requirements : Python version 3 or above.**

### Basic Elevator
**`class Elevator`**


The class represent single elevator only and has the following properties for solving the challenge given:

1. ***elevator_id***: An identity assigned to the elevator. in the range 0 to number_of_elevators - 1.
2. ***current_floor***: The current floor on which the elevator is present at the moment.
3. ***target_floor***: Current target floor where elevator is moving towards.
4. ***Running direction***: if the elevator is moving UP, then running direction is +1, if elevator is moving DOWN then -1. If the elevator is not moving at all then 0.

#### Helper functions 
Following are some of the helper functions with their functionality explanation

1. **`def matches_request(self, pickup_floor: int, direction: [1,-1])`** : This returns true if elevator is free or moving in the reqested direction.
2. **`def is_coming_to(self, pickup_floor: int)`**: this returns true if the elevator is coming in the direction of the pickup floor.


## Elevator System
**`class ElevatorSystem`**

This is our main class that utilises the Elevator objects and create a controller system for multiple elevators to work effeciently. Following are members of the class and uses:

1. ***lowest_floor***: The lowest floor in the elevator system(in building in the real world scenario).
2. ***highest_floor***: The highest floor in the elevator system(in building in the real world scenario).
3. ***elevators[]***: This list stores elevator objects.
4. ***elevators_queues = {}***: This stores the queu(note its a double ended queue for processing from both ends) for each individual elevator in the system.
5. ***pickup_requests***: This is also a double ended queue to store the requests coming from outside the elevators(i.e from the diffreent floors)

Following are the functions within the ElevatorSystem class along with their explanation and use:

* **`def status(self):`** It prints the status of the elevators in the system like current floor, target floor, direction. The door open and close print has been commented out n the step() function. But can be uncommented to use that functionality as well. This solves (3.b ) in the problem statement
* **`def get_floor_and_target(self,elevator_id : int)`**: This returns the current and the target floor of the elevator id passed.
* **`def pickup_request(self, pickup_floor : int , direction:[-1,1])`**: This processes the pickup requests made by different people on different floors and are stored in a dequeu(pickup_requests).
* **`def target_floor_request(self,elevator_id: int, target_floor: int)`**: This processes the floor requests made from *** within the elevator ***.
* **`hard_set(self,elevator_id:int, current_floor: int, target_floor = None)`** : This is for setting elevator to particular current floor and target floor. Useful in case of fault in elevator so that it can be rectified or for testing.
* **`def step(self)`** : For continous working of the elevator system as the time tick by and it can be synced with clock as well for advanced uses. This solves(3.a and 3.c) in the problem statement.

### Target floor request for the elevators, design and implementation explanation###
