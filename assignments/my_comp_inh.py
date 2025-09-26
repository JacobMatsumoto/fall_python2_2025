"""
Create a base class called Device that includes common attributes and methods for all devices in the smart home system (e.g., device name, status, and a method to turn the device on and off).

Create a subclass called Light that inherits from Device. Add specific attributes and methods for a general light (e.g., brightness level).

Create additional subclasses for specific types of lights, such as LEDLight and SmartBulb, that inherit from Light. Include unique attributes and methods for these specific types of lights.

Create a class called Thermostat that also inherits from Device. Include attributes and methods specific to a thermostat (e.g., current temperature, target temperature).

Create a main class called SmartHome that uses composition to include instances of Light, LEDLight, SmartBulb, and Thermostat. This class should have methods to control and manage the different devices.

Implement a user interface (UI) that allows users to interact with the smart home system. The UI should provide options to turn devices on and off, adjust brightness, and set temperatures. This should be a menu that brings up a list of devices. When you select a device, it should have a menu for off, on, brightness, etc., as well as the option to return to the main menu when done.

Test your program before handing it in. 
"""


class Device:
    def __init__(self, name, status):
        self.name = name
        self._status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def on_off(self):
        if self.status == "On":
            self.status = "Off"
        else:
            self.status = "On"


class Light(Device):
    def __init__(self, name, status, brightness):
        super().__init__(name, status)
        self.brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        try:
            if not isinstance(value, int):  # makes sure the entry is an int
                raise TypeError

            if not (1 <= value <= 100):  # makes sure it is between 1 and 100
                raise ValueError

            self._brightness = value

        except (TypeError, ValueError):
            print("Brightness must be a numeric number between 1 and 100")
            return

        except Exception as e:
            print(f"An error has occured: {e}")
            return


class LEDLight(Light):
    def __init__(self, name, status, brightness, strobe):
        super().__init__(name, status, brightness,)
        self.strobe = strobe

    @property
    def strobe(self):
        return self._strobe

    @strobe.setter
    def strobe(self, value):  # This ensures strobe cannot be something other than on or off
        if value != "On" and value != "Off":
            print("Invalid stobe state, defaulting to Off")
            value = "Off"
        self._strobe = value

    def toggle_strobe(self):
        if self.strobe == "On":
            self.strobe = "Off"

        else:
            self.strobe = "On"

        print(f"The {self.name}'s strobe is now {self.strobe} ")


class Smartbulb(Light):
    def __init__(self, name, status, brightness, color):
        super().__init__(name, status, brightness)
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        try:  # Bellow it makes sure value is within the valid colors to choose from for when I make it an option later
            # it shouldn't be needed because i'll force them to choose 1-7 but just in case.
            if not value.lower().strip() in ("white", "yellow", "green", "red", "blue", "purple", "cyan"):
                raise ValueError
            self._color = value
        except (ValueError):
            print(
                "The Color needs to be one of the following White, Yellow, Green, Red, Blue, Purple, Cyan")
        except Exception as e:
            print(f"An error has occured {e}")


class Thermometer(Device):
    def __init__(self, name, status, temp):
        super().__init__(name, status)
        self.temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        try:  # copy from brightness with minor changes
            if not isinstance(value, int):  # makes sure the entry is an int
                raise TypeError

            if not (1 <= value <= 90):  # makes sure it is between 1 and 90
                raise ValueError

            self._temp = value

        except (TypeError, ValueError):
            print("Temperature must be a numeric number between 1 and 90")
            return

        except Exception as e:
            print(f"An error has occured: {e}")


class SmartHome:
    def __init__(self):
        super().__init__()
        # Instantiating each one to then use methods over them
        self.living_room_light = Light("Living room light", "Off", 80)
        self.led_in_bathroom = LEDLight("Bathroom LED", "Off", 50, "Off")
        self.smart_light_bedroom = Smartbulb("Bedroom", "Off", 30, "purple")
        self.thermostat = Thermometer("Home Thermostat", "Off", 68)

    def turn_all_off(self):
        """Turns all devices off"""
        self.living_room_light.status = "Off"
        self.led_in_bathroom.status = "Off"
        self.smart_light_bedroom.status = "Off"
        self.thermostat.status = "Off"

    def turn_all_on(self):
        """Turns all devices on"""
        self.living_room_light.status = "On"
        self.led_in_bathroom.status = "On"
        self.smart_light_bedroom.status = "On"
        self.thermostat.status = "On"

    def on_or_off(self):
        """Prompt the user to turn specific items on or off depending on their choice 1-4 (5 to exit)"""
        # print( #commented out temporarily
        #     f"{self.living_room_light.name} Status:{self.living_room_light.status}\n"

        #     f"{self.led_in_bathroom.name} Status:{self.led_in_bathroom.status}\n"

        #     f"{self.smart_light_bedroom.name} Status:{self.smart_light_bedroom.status}\n"

        #     f"{self.thermostat.name} Status:{self.thermostat.status}\n"
        # )
        try:
            choice = 0
            while choice != 5:
                print(
                    f"{self.living_room_light.name} Status:{self.living_room_light.status}\n"

                    f"{self.led_in_bathroom.name} Status:{self.led_in_bathroom.status}\n"

                    f"{self.smart_light_bedroom.name} Status:{self.smart_light_bedroom.status}\n"

                    f"{self.thermostat.name} Status:{self.thermostat.status}\n"
                )

                choice = int(input(
                    "Which would you like to turn on or off? Pick 1-4 or 5 to exit\n"

                    f"1. {self.living_room_light.name}\n"

                    f"2. {self.led_in_bathroom.name}\n"

                    f"3. {self.smart_light_bedroom.name}\n"

                    f"4. {self.thermostat.name}\n"

                    f"5. Exit\n"

                ))

                if choice == 1:
                    self.living_room_light.on_off()
                    print(
                        f"{self.living_room_light.name} Status:{self.living_room_light.status}\n")

                elif choice == 2:
                    self.led_in_bathroom.on_off()
                    print(
                        f"{self.led_in_bathroom.name} Status:{self.led_in_bathroom.status}\n")

                elif choice == 3:
                    self.smart_light_bedroom.on_off()
                    print(
                        f"{self.smart_light_bedroom.name} Status:{self.smart_light_bedroom.status}\n")

                elif choice == 4:
                    self.thermostat.on_off()
                    print(
                        f"{self.thermostat.name} Status:{self.thermostat.status}\n")

                elif choice == 5:
                    print("Exiting")
                    break
                else:
                    print("Invalid input, please enter a 1,2,3,4 or 5")

        except (ValueError):
            print("Please enter a number in numerics between 1 and 5")

        except Exception as e:
            print(f"An error has occured: {e}")

    def change_brightness(self):
        """Prompt the user to change brightness depending on their choice 1-3 (4 to exit)"""

        try:
            choice = 0
            new_bright = 0
            while choice != 4:
                print(
                    f"{self.living_room_light.name} Brightness:{self.living_room_light.brightness}%\n"

                    f"{self.led_in_bathroom.name} Brightness:{self.led_in_bathroom.brightness}%\n"

                    f"{self.smart_light_bedroom.name} Brightness:{self.smart_light_bedroom.brightness}%\n"
                )

                print(
                    f"1. {self.living_room_light.name}\n"

                    f"2. {self.led_in_bathroom.name}\n"

                    f"3. {self.smart_light_bedroom.name}\n"

                    f"4. Exit"
                )

                choice = int(input(
                    "Which would you like to change the brightness of? Pick 1-3 or 4 to exit "))

                if choice == 1:  # This is a little redundent but I'm tired and it's 2am. it stays functional and redundent
                    try:
                        new_bright = int(input(
                            f"What brightness would you like to change {self.living_room_light.name}'s brightness to? Pick 1-100 "))
                        if 1 <= new_bright <= 100:
                            self.living_room_light.brightness = new_bright
                            print(f"Brightness set to {new_bright}%")
                        else:
                            print(
                                "\n\n-----Invalid brightness. Please enter a number between 1 and 100-----\n\n"
                            )

                    except (ValueError):
                        print("Please enter a number between 1-100")

                    except Exception as e:
                        print(f"An error has occured: {e}")

                if choice == 2:
                    try:
                        new_bright = int(input(
                            f"What brightness would you like to change {self.led_in_bathroom.name}'s brightness to? Pick 1-100 "))
                        if 1 <= new_bright <= 100:
                            self.led_in_bathroom.brightness = new_bright
                            print(f"Brightness set to {new_bright}%")

                        else:
                            print(
                                "\n\n-----Invalid brightness. Please enter a number between 1 and 100-----\n\n"
                            )

                    except (ValueError):
                        print("Please enter a number between 1-100")

                    except Exception as e:
                        print(f"An error has occured: {e}")

                if choice == 3:
                    try:
                        new_bright = int(input(
                            f"What brightness would you like to change {self.smart_light_bedroom.name}'s brightness to? Pick 1-100"))
                        if 1 <= new_bright <= 100:
                            self.smart_light_bedroom.brightness = new_bright
                            print(f"Brightness set to {new_bright}%")
                        else:
                            print(
                                "\n\n-----Invalid brightness. Please enter a number between 1 and 100-----\n\n"
                            )

                    except (ValueError):
                        print("Please enter a number between 1-100")

                    except Exception as e:
                        print(f"An error has occured: {e}")

                if choice == 4:
                    print("Exiting")
                    break

        except (ValueError):
            print("Please enter a number in numerics between 1 and 4")

        except Exception as e:
            print(f"An error has occured: {e}")

    def temp_control(self):
        choice = 0
        while choice != 2:
            try:
                print(
                    f"\nWould you like to change the temperature of the {self.thermostat.name}?\n"
                    f"It is currently set to {self.thermostat.temp}°F"
                )
                choice = int(input(f"Please enter 1 for yes and 2 for no "))
                if choice == 1:
                    new_temp = 0
                    try:
                        while new_temp < 50 or new_temp > 90:
                            new_temp = int(
                                input("Please set the temp between 50-90°F "))
                            if new_temp > 50 and new_temp < 90:
                                self.thermostat.temp = new_temp
                                print(f"Temp set to {new_temp}°F")
                            else:
                                print(
                                    f"\n\n-----Error! {new_temp} is not a number between 50 and 90-----\n\n")

                    except (ValueError):
                        print("Please enter a number between 50-90")

                    except Exception as e:
                        print(f"An error has occured: {e}")

                if choice == 2:
                    break
            except (ValueError):
                print("Please enter 1 or 2")

            except Exception as e:
                print(f"An error has occured: {e}")

    def toggle_color(self):
        """Prompt user to change the color on their LED 1-7 colors to pick"""
        try:
            choice = 0
            while choice != 8:

                print(
                    f"Current color: {self.smart_light_bedroom.color}\n"
                    "Pick a color to change 1-7 or 8 to exit\n"
                    "1. white\n"
                    "2. yellow\n"
                    "3. green\n"
                    "4. red\n"
                    "5. blue\n"
                    "6. purple\n"
                    "7. cyan\n"
                    "8. Exit"
                )

                choice = int(
                    input("Please select from the menu and enter a number between 1-8 "))

                if choice == 1:
                    self.smart_light_bedroom.color = "white"

                elif choice == 2:
                    self.smart_light_bedroom.color = "yellow"

                elif choice == 3:
                    self.smart_light_bedroom.color = "green"

                elif choice == 4:
                    self.smart_light_bedroom.color = "red"

                elif choice == 5:
                    self.smart_light_bedroom.color = "blue"

                elif choice == 6:
                    self.smart_light_bedroom.color = "purple"

                elif choice == 7:
                    self.smart_light_bedroom.color = "cyan"

                elif choice == 8:
                    print("Exiting")

                else:
                    print("Invalid input! Please enter 1-8")

        except (ValueError):
            print("Please enter 1-8")

        except Exception as e:
            print(f"An error has occured: {e}")

    def change_strobe(self):
        """Allows user to toggle the strobe on or off by offering a choice of 1 for toggle and 2 to quit"""
        try:
            choice = 0
            while choice != 2:
                choice = int(input
                             (f"Would you like to toggle the strobe? 1. Yes. 2. No. Currently:{self.led_in_bathroom.strobe} "
                              ))
                if choice == 1:
                    self.led_in_bathroom.toggle_strobe()
                    print(f"Toggled to {self.led_in_bathroom.strobe}!")

                elif choice == 2:
                    print("Goodbye!")

                else:
                    print(
                        f"\n\n-----Error! is not 1 or 2-----\n\n")

        except (ValueError):
            print("Please enter 1-8")

        except Exception as e:
            print(f"An error has occured: {e}")

    def status_report(self):
        """Prints all devices current states"""
        print(
            f"\n{self.living_room_light.name} Status:{self.living_room_light.status} "
            f"Brightness:{self.living_room_light.brightness}%\n"

            f"{self.led_in_bathroom.name} Status:{self.led_in_bathroom.status} "
            f"Brightness:{self.led_in_bathroom.brightness}% Strobe:{self.led_in_bathroom.strobe}\n"

            f"{self.smart_light_bedroom.name} Status:{self.smart_light_bedroom.status} "
            f"Brightness:{self.smart_light_bedroom.brightness}% Color:{self.smart_light_bedroom.color}\n"

            f"{self.thermostat.name} Status:{self.thermostat.status} "
            f"Temp:{self.thermostat.temp}°F \n"
        )


def main():
    """Menu system prompts for a 1-8 for different options to chose from, 9 to exit."""
    my_smart_home = SmartHome()
    choice = 0

    try:
        while choice != 9:
            print(
                "\n=====Welcome to the Smart Home system!=====\n"
                "1 Turn all devices on\n"
                "2 Turn all devices off\n"
                "3 Toggle a device on/off\n"
                "4 Change device brightness\n"
                "5 Control thermostat temperature\n"
                "6 Toggle smart light strobe\n"
                "7 Change LED color\n"
                "8 Show status report\n"
                "9 Exit\n"
            )
            choice = int(input(
                "Please pick which you would like access "
            ))

            if choice == 1:
                my_smart_home.turn_all_on()
                print("\nAll devices are now on")

            elif choice == 2:
                my_smart_home.turn_all_off()
                print("\nAll devices are now off")

            elif choice == 3:
                my_smart_home.on_or_off()

            elif choice == 4:
                my_smart_home.change_brightness()

            elif choice == 5:
                my_smart_home.temp_control()

            elif choice == 6:
                my_smart_home.change_strobe()

            elif choice == 7:
                my_smart_home.toggle_color()

            elif choice == 8:
                my_smart_home.status_report()

            elif choice == 9:
                print("Goodbye!")

            else:
                print(
                    f"\n\n-----Error! that is not a number between 1 and 7-----\n\n")

    except (ValueError):
        print("Please enter a number between 1-7")

    except Exception as e:
        print(f"An error has occured: {e}")


main()
