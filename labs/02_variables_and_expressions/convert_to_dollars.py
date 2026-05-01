nickels = float(input("How many nickels do you have? "))
dimes = float(input("How many dimes do you have? "))
quarters = float(input("How many quarters do you have? "))

dollars = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

print(f"Amount: ${dollars:.2f}")