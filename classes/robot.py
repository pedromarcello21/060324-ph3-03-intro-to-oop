class Robot:

    def __init__(self, name, battery_life, wd40):
        print("I AM MAKING A ROBOT")
        # print("I AM: ", self)
        self.name = name
        self.battery_life = battery_life
        self.wd40 = wd40
    
    def __repr__(self): ###represent itself
        return f"Robot(name={self.name} battery_life={self.battery_life} wd40={self.wd40}"
    
    def build(self, item): ###custom method
        return f"Building some good quality {item}"
    
    @property  ###getter.  need getter for setter
    def battery_life(self):
        return f"{self._battery_life}%"
    

    @battery_life.setter ###setter
    def battery_life(self, value):
        if type(value) == int and 100 >= value >= 1:
            self._battery_life = value
        else:
            raise TypeError("battery life must be an integer between 100 and 1 inclusive")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise TypeError("You may not rename this bot")
        else:
            self._name = value

        # pass