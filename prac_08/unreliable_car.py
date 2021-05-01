from prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, {}".format(self.name, self.reliability)

    def drive(self, distance, reliability):
        """Only drive the car if the breakdown chance is less than the car's reliability"""

        import random
        breakdown_chance = float(random.randint(0, 100))
        if breakdown_chance < self.reliability:
            driven_distance = super().drive(distance)
            print("WARNING:\nWith {}% reliability the chance of "
                  "a breakdown driving {}KMs is {}%".format(self.reliability,
                                                            driven_distance,
                                                            breakdown_chance))
            distance = 0
        driven_distance = super().drive(distance)
        print("The distance driver is: ", distance)
        return driven_distance
