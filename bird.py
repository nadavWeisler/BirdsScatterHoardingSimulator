class Bird:
    def __init__(self, name, color, key):
        self.name = name
        self.color = color
        self.key = key
        
    def getHideOut(self):
        return self.name + " is hiding out at " + self.key