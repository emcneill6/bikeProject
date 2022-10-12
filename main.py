#
# Number of Gears -
    # a whole number
    # require that the number of wheels be entered and say that there is an error if there is not an input

# Current Geae
    # default set to 1

#Number of Wheels
    # can accept 1, 2, 3, or 4 wheels is acceptable
    # any other integer or string etc entered should return an error
    # require that the number of wheels be entered and say that there is an error if there is not an input

#Brake Type
    # either "hand brakes" or "foot brakes"
    # require that the number of wheels be entered and say that there is an error if there is not an input

#Set & Get Number of Gears (2 points)
# Set & Get Current Gear (2 points)
    # this default value is 1, but any point you can change the gear to a valid number (1-15)
# Set & Get Number of Wheels (2 points)
    # the default is
# Set & Get Brake Type (2 points)

# once your bike is created,
#Reset Gears: Set gear back to 1 (1 point)
        #myBike.resetGear
# Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears (1 point)
# myBike.increaseGear
# Decrease Gear: Decrease Current Gear by 1, do not allow going under 1
# if you are at gear 15, then you can't increase the gear anymore
    # you should never go above the number of gears set in the numberOfGears method

from bike import Bike

try:

#instantiate new bike
    myBike = Bike()
    myBike.setNum(10)
    myBike.setCurrent(1)
    myBike.setWheels(2)
    myBike.setBrake("hand")

#show the bike has 10 gears
    print(f"The bike has {myBike.getNum()} gears")

    myBike.increaseGear()

    print(f"The current gear has increased to {myBike.getCurrent()}")
    print(f"Let us increase the current gear to the maximum gear allowed: {myBike.getNum()}")
    myBike.setCurrent(10)
    input("Press [ENTER] to continue ")
    print()
#see what happens when you try to go above max gear
    print(f"The current gear has increased to {myBike.getCurrent()}")
    myBike.increaseGear()
    print(f"The current gear has increased to {myBike.increaseGear()}")

    myBike.increaseGear()
    print(f"The current gear has increased to {myBike.increaseGear()}")
#try to set invalid number of wheels
    input("Press [ENTER] to continue ")
    print()


    myBike.reset()
    print(f"Let us reset the gear to 1")
    print("Let us see what happens if we try to go below the minimum number of gears")
    myBike.setCurrent(1)
    myBike.decreaseGear()
    print(f"the current gear is {myBike.getCurrent()}")
    print(f"if we decrease the gear, then {myBike.getCurrent()}")
    input("Press [ENTER] to continue ")
    print()
# increase gears
    myBike.increaseGear()
    myBike.increaseGear()

#try to set an invalid brake type
    myBike.setBrake("electric")



except Exception as e:
    print(f"Got an error: {e}")