class Robot:

    # magic / dunder method on creating a new robot
    def __init__(self, name:str, color:str, operating_system:str):
        print("BUILDING A NEW ROBOT")
        self.name = name
        self.color = color
        self.operating_system = operating_system

    # magic / dunder method on looking at a robot directly (for example `print(r2d2)` )
    def __repr__(self):
        return f"Robot(name={self.name} color={self.color} operating_system={self.operating_system})"

    # shows the robot itself
    def see_myself(self):
        return self
        
    # this method is called when we call r2d2.operating_system
    @property
    def operating_system(self):
        return self._operating_system.upper()

    # this method is called when we call r2d2.operating_system = ""
    @operating_system.setter
    def operating_system(self, value:str):
        if type(value) == str:
            self._operating_system = value
        else:
            raise TypeError("Robot operating_system must be a string")