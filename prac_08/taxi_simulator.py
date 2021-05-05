"""Taxi Simulator"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"


def main():
    """
    Choose a taxi from a list, drive for your preferred distance,
    each trip and the total fare will be calculated.
    """
    print("Let's drive!")
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [prius, limo, hummer]
    total_bill = 0.0
    chosen_taxi = None
    user_choice = input(MENU).upper()
    while user_choice != "Q":
        if user_choice == "C":
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_bill))
        elif user_choice == "D":
            chosen_taxi.start_fare()
            distance = float(input("Drive how far? "))
            chosen_taxi.drive(distance)
            trip_fare = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, trip_fare))
            total_bill += trip_fare
            print("Bill to date: ${:.2f}".format(total_bill))

        else:
            print("Invalid choice")

        user_choice = input(MENU).upper()
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    """List available taxis"""
    for i, taxi in enumerate(taxis):
        print(i, "-", taxi)


# Test
# c 0 d 333 c 1 d 60 c 2 d 60 c 1 d 50 q


if __name__ == main():
    main()
