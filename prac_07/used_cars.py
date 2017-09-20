from prac_07.car import Car

def main():
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(str(limo))


main()