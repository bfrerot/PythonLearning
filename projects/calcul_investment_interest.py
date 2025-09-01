##illustrer les resultats d'un investissement
#display a welcome message
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

 #Welcome to the Future Value Calculator

# How much do you want to invest? 1000
# At each rate? 5
# For how many years? 6
#year 1: $1,050.00

# year 2: $1,102.50

# year 3: $1,157.62

# year 4: $1,215.51

# year 5: $1,276.28

# year 6: $1,340.10

# Bye!