from passenger import passenger
from platform import platform
from train import train
from wagon import wagon



def CreatePlatform():
    ''' Creating the platform '''
    platform = platform(n, p, t)

    return platform


def main():

    # Creating the objects for the system
    CreatePlatform()

    print("The platform " + platform.__str__() + "was created and has currently "
          + str(platform.getPassenger()) + " Passengers waiting.")
