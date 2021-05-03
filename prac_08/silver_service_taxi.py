"""Silver Service Taxi"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi class"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f} ".format(super().__str__(), self.flagfall)

    def get_silver_fare(self):
        """Calculate the total fare"""
        return super().get_fare() + self.flagfall

# Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50
# s1 = SilverServiceTaxi("asd",200,4)
# print(s1.get_silver_fare())
