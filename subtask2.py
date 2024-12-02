n = 0
s = 0
a = -1
m=11111111111111111111111111111

print("Enter numbers in the sequence (terminate with -1):")

while True:
    x = int(input("Enter number: "))
    if x == -1:
        break
    n += 1
    s += x
    if x < m:
        m = x

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print(f"Count (n): {n}")
print(f"Sum (s): {s}")
print(f"Minimum (m): {m}")
print(f"Mean (a): {a}")
