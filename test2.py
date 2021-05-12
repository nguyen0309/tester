a = bin(1163)[2:] # số mũ
n = len(a)
b = int(a[0])
x = 43 # x mũ a
c = 4399 # số cần mod
for i in range(n):
    if(a[i] == '1'):
        b = b*b
        j = b
        b = b%c
        k = b
        b = b*x
        l = b
        b = b%c
        p = b
        print(a[i]+ "  " +str(j) + "      " + str(k) + "       " + str(l) + "       " + str(p))
    elif(a[i] == '0'):
        b = b*b
        t = b
        b = b%c
        y = b
        b = b%c
        o = b
        print(a[i]+ "  " +str(t) + "      " + str(y) + "       " + "--" + "       " + str(o))