class Car:

    def __init__(self):
        self.key_in = bool
        self.gear = str
        self.drive_state = str

    def ignition(self, key_in):
        self.key_in = key_in

    def gear_shift(self):
        if self.key_in:
            while True:
                gear_mode = input('Enter the gear mode (P, N, D, R): ')

                if gear_mode == "P":
                    self.gear = gear_mode
                    print("Shifted to %s gear" % self.gear)
                    break

                elif gear_mode == "N":
                    self.gear = gear_mode
                    print("Shifted to %s gear" % self.gear)
                    break

                elif gear_mode == "D":
                    self.gear = gear_mode
                    print("Shifted to %s gear" % self.gear)
                    break

                elif gear_mode == "R":
                    self.gear = gear_mode
                    print("Shifted to %s gear" % self.gear)
                    break

                else:
                    self.gear = "0 (Invalid)"
                    print('Invalid Gear')

        else:
            print('Key is not inserted')

    def drive(self):
        if self.key_in:
            while True:
                system = input('Please enter "Forward", "Reverse", "Steer Left", "Steer Right", "Brakes", "Parking '
                               'Brakes", "Shift Gears" or "Car '
                               'Off": ')

                if system == "Forward":
                    if self.gear == "D":
                        self.drive_state = system
                        print('Moving forward')
                    else:
                        print("You cannot move forwards in this gear")

                elif system == "Reverse":
                    if self.gear == "R":
                        self.drive_state = system
                        print("Moving backwards")
                    else:
                        print("You cannot move backwards in this gear")

                elif system == "Steer Left":
                    self.drive_state = "L"
                    print("Steering Left")

                elif system == "Steer Right":
                    self.drive_state = "R"
                    print("Steering Right")

                elif system == "Brakes":
                    if self.gear == "R" or self.gear == "D" or self.gear == "N":
                        self.drive_state = system
                        print('Stopping')
                    else:
                        print('You cannot brake in this gear')

                elif system == "Car Off":
                    self.drive_state = system
                    self.key_in = False
                    print('Turning off car')
                    break

                elif system == "Parking Brakes":
                    if self.gear == "P":
                        self.drive_state = "P-Brakes"
                        print('Parking Brakes Activated')
                    else:
                        print('You cannot activate the parking brakes in this gear')

                elif system == "Shift Gears":
                    gear_drive_changer = input('Enter the gear mode (P, N, D, R): ')
                    self.gear = gear_drive_changer
                    self.drive_state = "Brakes"

                    if self.gear == "P":
                        print("Shifted to %s gear" % self.gear)

                    elif self.gear == "N":
                        print("Shifted to %s gear" % self.gear)

                    elif self.gear == "D":
                        print("Shifted to %s gear" % self.gear)

                    elif self.gear == "R":
                        print("Shifted to %s gear" % self.gear)

                    else:
                        self.gear = "0 (Invalid)"
                        print('Invalid Gear')

                else:
                    print('Invalid Option')

        else:
            pass


if __name__ == '__main__':
    Car.ignition(Car, True)
    Car.gear_shift(Car)
    Car.drive(Car)

