from train import train

class large(train):
    ''' This is a large train '''

    def __init__(self, n):
        ''' Initializes the large train '''
        self.name = n
        self.length = 3
        self.capacity = 100


    def getLength(self):
        ''' Returning the length of the train '''
        return self.length


    def getCapacity(self):
        ''' Returning the passenger capacity of the train '''
        return self.capacity
