# ElevatorSystem Design 
** Requirements : Python version 3 or above.**

### Basic Elevator(elevator.py)
**`class Elevator`**


The class represent single elevator only, i sbeing used by elevator system and has the following properties for solving the challenge given:

1. ***elevator_id***: An identity assigned to the elevator. in the range 0 to number_of_elevators - 1.
2. ***current_floor***: The current floor on which the elevator is present at the moment.
3. ***target_floor***: Current target floor where elevator is moving towards.
4. ***Running direction***: if the elevator is moving UP, then running direction is +1, if elevator is moving DOWN then -1. If the elevator is not moving at all then 0.

#### Helper functions 
Following are some of the helper functions with their functionality explanation

1. **`def matches_request(self, pickup_floor: int, direction: [1,-1])`** : This returns true if elevator is free or moving in the reqested direction.
2. **`def is_coming_to(self, pickup_floor: int)`**: this returns true if the elevator is coming in the direction of the pickup floor.


## Elevator System(elevatorSystem.py)
**`class ElevatorSystem`**

This is our **main class** that utilises the Elevator objects and create a controller system for multiple elevators to work effeciently. Following are members of the class and their uses:

1. ***lowest_floor***: The lowest floor in the elevator system(in building in the real world scenario).
2. ***highest_floor***: The highest floor in the elevator system(in building in the real world scenario).
3. ***elevators[]***: This list stores elevator objects. The total number of elevator in the system are passed to the init method.
4. ***elevators_queues = {}***: This stores the queue (note its a double ended queue for processing from both ends) for each individual elevator in the system.
5. ***pickup_requests***: This is also a double ended queue to store the requests coming from outside the elevators(i.e from the diffreent floors)

Following are the functions within the ElevatorSystem class along with their explanation and use:

* **`def status(self):`** It prints the status of the elevators in the system like current floor, target floor, direction. The door open and close print has been commented out in the step() function. But can be uncommented to use that functionality as well. 
* **`def get_floor_and_target(self,elevator_id : int)`**: This returns the current and the target floor of the elevator id passed.
* **`def pickup_request(self, pickup_floor : int , direction:[-1,1])`**: This processes the pickup requests made by different people on different floors and are stored in a dequeu(pickup_requests).
* **`def target_floor_request(self,elevator_id: int, target_floor: int)`**: This processes the floor requests made from *** within the elevator ***.
* **`hard_set(self,elevator_id:int, current_floor: int, target_floor = None)`** : This is for setting elevator to particular current floor and target floor. Useful in case of fault in elevator in real world so that it can be rectified or for testing.
* **`def step(self)`** : For continous working of the elevator system as the time tick by and it can be synced with clock as well for advanced uses.

### Target floor request for the elevators, design and implementation explanation

For assigning different floors to elevator, modified first come first serve basis is used within the target_floor_request method. So for example if an elevator gets request to go to floors 5, 8 and 6 then the modfied first come first serve will stop the elevator at 6 after going from floor 5. The logic is explained below: 

If new request for floor is between the current floor and the current target floor then the requested floor is appended to the left of the deque for that particular elevator so that within its way it stops in that floor. Otherwise it is normally appended to the end.

### Handling pickup requests

With each step(in real world with time passing by), each request is looked up and assigned proper elevator using the target_floor_request. The logic that is being used is that for each request, free elevators that are closest to the floor is looked up and assigned the floor. If not, then the elevators that are moving in same direction as floor and is closest to the requested floor is assigned.

If both the above scenario finds no match elevators, then the request is kept in the queue and is processed in the further step functions(time).

if request is served, it is removed from the pickup_requests.

### Unit tests

Unit tests have been written to test both the elevator functionality and elevator system(multiple elevator). To run the tests use the following commands 

**`python test_elevator.py`**

**`python test_elevatorsystem.py`**

### Simulations 

Basic simulations have been implemented to see the pickup_request functionality from outside the elevators and target floor request to see the request from the eelevators as well.

To run both the simulation and see the sample working, please use the following commands 

**`python simulate_floorrequest.py`**

**`python simulate_pickuprequest.py`**

**Note**: While runing the programs, make sure the files are within the same directory as modules are imported from elevator and elevatorSystem classes.
