from train import train

class max(train):
    ''' This is a max train '''

    def __init__(self, n):
        ''' Initializes the max train '''
        self.name = n
        self.length = 5
        self.capacity = 200


    def getLength(self):
        ''' Returning the length of the train '''
        return self.length


    def getCapacity(self):
        ''' Returning the passenger capacity of the train '''
        return self.capacity
