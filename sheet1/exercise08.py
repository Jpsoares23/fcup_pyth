def final_capital_tabl(i_capital: int | float, i_rate: float) -> None:
    for months in range(0, 24):
        final_capital = i_capital * ((1 + i_rate / 12) ** months)
        print(f"{months} | {final_capital:.2f}")


initial_capital = float(input("Initial Capital: "))
interest_rate = float(input("Interest Rate: "))

final_capital_tabl(initial_capital, interest_rate)
