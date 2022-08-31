h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))

if h > 40:
    pay = (40*r) + (1.5 * r * (h - 40))
else:
    pay = h*r

print(pay)