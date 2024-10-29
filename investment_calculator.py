print("Welcome to the Future Value Calculator")
print()
def invest(amount, rate, years):
    for i in range(1, years+1):
        amount = amount * (1 + (rate/100))
        print(f"year {i}: ${amount:,.2f}")
        print()
amount = float(input("How much do you want to invest? "))
rate = float(input("At each rate? "))
years = int(input("For how many years? "))
invest(amount, rate, years)
print("Bye!")
