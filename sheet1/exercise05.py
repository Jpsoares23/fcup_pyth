def how_to_pay(value: int) -> None:
    money_list = [20, 10, 5, 1]
    money_index = 0
    last_money_list_index = len(money_list) - 1

    bill_times_used_list = []

    while True:
        bill_times_used_placeholder = 0

        while value >= money_list[money_index]:
            value -= money_list[money_index]
            bill_times_used_placeholder += 1

        bill_times_used_list.append(bill_times_used_placeholder)

        if money_index < last_money_list_index:
            money_index += 1

        else:
            break

    print(f'notas EUR {money_list[0]}: {bill_times_used_list[0]}')
    print(f'notas EUR {money_list[1]}: {bill_times_used_list[1]}')
    print(f'notas EUR {money_list[2]}: {bill_times_used_list[2]}')
    print(f'notas EUR {money_list[3]}: {bill_times_used_list[3]}')


if __name__ == "__main__":
    while True:
        try:
            money = int(input('How much money (€)? '))
            if money < 0:
                print("Amount of money cannot be negative. Please enter a positive amount.")
            else:
                how_to_pay(money)
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
