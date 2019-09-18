from train import train

class medium(train):
    ''' This is a medium train '''

    def __init__(self, n):
        ''' Initializes the medium train '''
        self.name = n
        self.length = 2
        self.capacity = 75


    def getLength(self):
        ''' Returning the length of the train '''
        return self.length


    def getCapacity(self):
        ''' Returning the passenger capacity of the train '''
        return self.capacity
