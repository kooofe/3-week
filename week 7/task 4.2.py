def isInside(x, y, rad, p1, p2):
    if ((p1 - x) * (p1 - x) +
            (p2 - y) * (p2 - y) <= rad * rad):
        return True
    else:
        return False
p1 = 11
p2 = 12
x = 0
y = 1
rad = 2
if isInside(x, y, rad, p1, p2):
    print("Inside")
else:
    print("Outside")
