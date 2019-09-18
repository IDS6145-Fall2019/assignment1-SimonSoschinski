from train import train

class small(train):
    ''' This is a small train '''

    def __init__(self, n):
        ''' Initializes the small train '''
        self.name = n
        self.length = 1
        self.capacity = 50


    def getLength(self):
        ''' Returning the length of the train '''
        return self.length


    def getCapacity(self):
        ''' Returning the passenger capacity of the train '''
        return self.capacity