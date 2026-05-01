car_mpg = float(input("What's your cars mpg? "))
cost_of_gas = float(input("How much does gas cost for you? "))

gas_cost_20 = cost_of_gas / car_mpg * 20
gas_cost_75 = cost_of_gas / car_mpg * 75
gas_cost_500 = cost_of_gas / car_mpg * 500

print(f"{gas_cost_20:.2f} {gas_cost_75:.2f} {gas_cost_500:.2f}")