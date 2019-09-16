class platform:
    ''' The platform class '''

    def __init__(self, n, p, t):
        ''' Initializes the platform '''
        self.name = n
        self.passenger = p
        self.train = t


    def __str__(self):
        ''' The print statement for the platform '''

        return str(self.name)

    def getPassenger(self):
        ''' This returns the number of passengers waiting '''

        return self.passenger