def value(v: list) -> float:
    total_gasoline_spent = 0
    gasoline_price = 1.72

    for gasoline in v:
        total_gasoline_spent += gasoline

    trip_cost = total_gasoline_spent * gasoline_price
    return trip_cost


if __name__ == "__main__":
    gasoline_spent = []

    while True:
        try:
            gasoline_spent.append(int(input("Gasoline spent: ")))
        except ValueError:
            print("Please enter a valid number for gasoline spent.")
            continue

        while True:
            want_ex = input("Do you want to enter more data? (y/n): ").upper()
            if want_ex == "Y":
                break
            elif want_ex == "N":
                print(value(gasoline_spent))
                exit()
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
