m = 4536
fake = m
a = 11
y0 = 0
y1 = 1
c = 0
print('m' + " " + "a" + " " + "r" + " " + "q" + " " + "y0" + " " + "y1" + "  " + "y")
while True:
    r = m%a
    q = int(m/a)
    y = y0 - (y1 * q)
    if (y < 0):
        c = y + fake
    if (r == 0):
        print(c)
        break
    print(str(m) + " | " + str(a) + " | " + str(r) + " | " + str(q) + " | " + str(y0) + " | " + str(y1) + " | " + str(y))
    m = a
    a = r
    y0 = y1
    y1 = y