n = int(input("Enter a natural number (n ≥ 0): "))
q = 1

while q**2 <= n:
    q += 1
q= (q - 1) ** 2
print(f"The largest square number less than or equal is {q}.")
