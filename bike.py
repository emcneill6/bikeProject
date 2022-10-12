# this is bike class

class Bike:


    __num: int = 0
    __current: int = 1
    __wheels: int = 1
    __brake: str = ""

    def __init__(self,
                 num=1,
                 current=1,
                 wheels=1,
                 brake=""):

        # Set all our properties
        if brake is None:
            brake = "hand"
        self.setNum(num)
        self.setCurrent(1)
        self.setWheels(wheels)
        self.setBrake(brake)

# set and number of gears
    def setNum(self, num: int) -> None:
        try:
            if int(num):
                pass
        except Exception as e:
            raise TypeError(f"{num} is not an integer")

        if num > 0 and num < 16:
            self.__num = int(num)
        else:
            raise ValueError(f"{num} is not a valid number of gears")

    def getNum(self) -> int:
        return self.__num


# set and get current gear
    def setCurrent(self, current):
        try:
            if int(current):
                pass
        except Exception as e:
            raise TypeError(f"{current} is not a valid integer")

            if current <= 0 or current > self.__num:
                raise ValueError('Current gear cannot exceed the number of gears')
            else:
                self.__current = int(current)

    def getCurrent(self) -> int:
        return self.__current

# set and get number of wheels
    def setWheels(self, wheels: int) -> None:
        try:
            if int(wheels):
                pass
        except Exception as e:
            raise TypeError(f"{wheels} is not a valid integer")

            if wheels < 1 and wheels <= 4:
                self.__num = num
            else:
                raise ValueError('The bike can only have 1, 2, 3, or 4 wheels.')
          #  else:

#get and set brake type
    def setBrake(self, brake: str) -> None:
        try:
            if brake != "hand" and brake != "foot":
                print(f"Invalid brake type. Brake type must be a hand or foot brake")
            else:
                self.__brake = brake
                    #str(brake):
                    #pass
        except Exception as e:
            raise TypeError(f"{brake} is not a valid input.")


             #raise ValueError(f"Brake type must be a hand or foot brake")

    def getBrake(self):
        return self.__brake

    def increaseGear(self):
        if self.getCurrent() == self.__num:
            print("Gear is already maximized")
        else:
            return (self.__current + 1)

       # except Exception as e:
       #     raise e

    def decreaseGear(self):
        if self.getCurrent() == 1:
            return(print("Gear cannot go below 1"))
        else:
            return(self.setCurrent(self.getCurrent() - 1))


    def reset(self):
        self.setCurrent == 1