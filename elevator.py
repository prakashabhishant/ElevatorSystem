class Elevator(object):
    
    """"this class represnt the blue print of one elevator only.
    Class members are as follows :
    elevator_id : number greater than or equal to zero 
    current_floor: the current floor of the elevator in range[lowest_floor, highest_floor]
    running direction : [1,0,-1] with 1 meaning upwards, 0 means not moving and -1 meaning going downwards 
    target_floor: the floor on which the elevator is going towards """
    
    def __init__(self, elevator_id: int, current_floor: int):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.target_floor = None
        self.running_direction = 0 
        
    
    def status(self):
        """Reperesnt the status of the elevator"""
        print(self.__repr__())
        
    def __repr__(self):
        """print the representation of the elevator"""
        dirn = "UP" if self.running_direction == 1 else "DOWN" if self.running_direction == -1 else "STOP"
        return "id :{}, current_floor :{}, target_floor:{}, direction: {}".format(self.elevator_id, self.current_floor, self.target_floor,dirn)
    
    def set_target_floor(self, target_floor: int):
        """method to set the target floor and change the running direction"""
        
        self.target_floor = target_floor
        """check whether the elevator has direction or not, it can be unset by the controller of the elevator"""
        
        if self.target_floor is not None:
            if self.target_floor > self.current_floor:
                self.running_direction = 1
            elif self.target_floor < self.current_floor:
                self.running_direction = -1
            else:
                self.running_direction = 0
    
        else:
            self.running_direction = 0
            
    
    def get_current_floor(self):
        return self.current_floor
    
    
    def get_target_floor(self):
        return self.target_floor
    
    
    def get_direction(self):
        return self.running_direction
    
    
    def matches_request(self, pickup_floor: int, direction: [1,-1]):
        """ this would return true if elevator is free or runs along the request direction """
        
        if self.target_floor is None: 
            return True 
        
        if direction == self.running_direction:
            if direction > 0 and pickup_floor > self.current_floor:
                return True 
            if direction < 0 and pickup_floor < self.current_floor:
                return True 
        return False
    
    def is_coming_to(self, pickup_floor: int):
        """Return true if elevator is coming in the direction of the floor where request for elevator was made"""
        
        if pickup_floor < self.current_floor and self.running_direction < 0:
            return True 
        
        if pickup_floor > self.current_floor and self.running_direction > 0:
            return True 
        
        return False
    
    def step(self):
        """ Move the elevator in the right dirn as per the direction"""
        
        """ This can be removed just for the printing purpose"""
#         if self.running_direction < 0:
#             print("DOWN_1")
#         elif self.running_direction > 0:
#             print("UP_1")

        self.current_floor += self.running_direction
    
    def hard_set_current_floor(self, current_floor : int):
        """This can be used for testing where you want to bring elevator to certain floor in real world forcefully."""
        self.current_floor = current_floor
