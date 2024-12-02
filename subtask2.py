n = 0
s = 0
a = -1
m=11111111111111111111111111111

print("Enter numbers in the sequence (end with -1):")

while True:
    x = int(input("Enter number: "))
    if x == -1:
        break #break is used to exit the loop immeditaly so to ensure that -1 does not enter the loop
    n += 1
    s += x
    if x < m:
        m = x

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print(f"Count: {n}")
print(f"Sum: {s}")
print(f"Minimum: {m}")
print(f"Mean: {a}")
# it looks like I learned how to use git today
