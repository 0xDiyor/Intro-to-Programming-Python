import math

r = math.pow(2,(1/12))

init_freq = float(input("Enter initial frequency: "))

freq_1 = init_freq * (math.pow(r,1))
freq_2 = init_freq * (math.pow(r,2))
freq_3 = init_freq * (math.pow(r,3))

print(f"{init_freq:.2f} Hz\n{freq_1:.2f} Hz\n{freq_2:.2f} Hz\n{freq_3:.2f} Hz")

