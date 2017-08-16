try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator/denominator
    print(fraction)


except ValueError:
    print("numerator and denominator must be valid numbers!")

print("Finished")
