class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__autopilot = autopilot
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__efficiency = efficiency

    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def color(self):
        return self.__color

    def autopilot(self, obstacle: str) -> str:
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obstacle}"
        return "Autopilot is not available"

    @property
    def seats_count(self):
        """Returns seat count of Tesla"""
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, new_seats_count: int):
        """Takes an argument of how many seats your Tesla should have, and
        returns it, has constrain of not less than 2 seats"""
        self.__seats_count = new_seats_count
        if self.__seats_count < 2:
            self.__seats_count = 2
        else:
            self.__seats_count = new_seats_count

    @property
    def is_locked(self) -> bool:
        """Returns a boolean if car is locked"""
        return self.__is_locked

    def unlock(self) -> None:
        self.__is_locked = False

    def lock(self) -> None:
        self.__is_locked = True

    def open_doors(self) -> str:
        if self.__is_locked:
            return "Car is locked!"
        return "Doors opens sideways"

    @property
    def battery_charge(self):
        return self.__battery_charge

    def check_battery_level(self) -> str:
        return "Battery charge level is {battery_level}%".format(battery_level=self.__battery_charge)

    def charge_battery(self):
        """Charges Tesla to 100%"""
        self.__battery_charge = 100

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency

        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge = self.__battery_charge - battery_discharge_percent
            return self.check_battery_level()
        return self.check_battery_level()


class ModelX(Tesla):
    def __init__(self, color: str, autopilot: bool = False):
        # PASS REQUIRED VARIABLES TO INIT FUNCTION. EFFICIENCY SHOULD BE SET TO 0.125
        super().__init__("Model3", color)
        self.__efficiency = 0.125

    def open_doors(self):
        return "Doors opens towards roof"

    def welcome(self) -> str:
        return "Hello from ModelX!"
