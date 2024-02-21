def Temp_calc(V,I):
    R = V/I
    R2 = R/1.1
    a = 4.5*(10**(-3))
    Temp = 295.15 + ((R2-1)/a)
    return Temp

def error_prop(temp,delta,I):
    res = temp*(delta/I)
    return res

I = 0.43
V = 5
D = 0.0005
Temp = Temp_calc(V,I)

print(Temp)

err = error_prop(Temp, D, I)


print(err)