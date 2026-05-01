phone_number = int(input())
area_code = phone_number // 10000000
prefix = (phone_number // 10**4) % 1000
line_num = phone_number % 10000
conc = (f"({area_code}) {prefix}-{line_num}")

print (conc)
