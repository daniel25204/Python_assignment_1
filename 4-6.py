def computepay(h,r):
    if h > 40:
        p = (40*r) + (1.5 * r * (h - 40))
    else:
        p = h * r
    return p
    
hr = float(input("Enter Hours:"))
rphr = float(input("Enter rate per hour:"))

p = computepay(hr,rphr)
print(p)