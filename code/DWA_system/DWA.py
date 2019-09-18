from passenger import passenger
from platform import platform
from train import train
from small import small
from medium import medium
from large import large
from max import max



def CreatePlatform():
    ''' Creating the platform '''
    n = "Testplatform"
    p = 200
    s = 5
    t = None
    p = platform(n, p, s, t)

    return p


def main():

    # Creating the objects for the system
    p1 = CreatePlatform()


    print("The platform " + p1.__str__() + " was created and has currently "
          + str(p1.getPassenger()) + " Passengers waiting.")



if __name__ == "__main__":
    main()