import numpy as np

def n(theta):
    res = theta*(np.pi/180)
    res2 = np.sin(res)
    num = np.sqrt(((((2/np.sqrt(3))*res2)+(1/2))**2)+(3/4))
    return num

def delta_n(theta, dtheta, n):
    res = theta*(np.pi/180)
    res2 = np.sin(res)
    res3 = np.cos(res)
    dx = (((2/np.sqrt(3))*res2)+(1/2))*2*((2/np.sqrt(3))*res3*dtheta)
    dn = n * 0.5 * ((dx)/((((2/np.sqrt(3))*res2)+(1/2))**2)+(3/4))
    return dn

def lambda_max(n):
    lam = np.sqrt(13900/(n-1.689))
    return lam

def delta_lam(lam, n, dn):
    dl = lam * 0.5 * ((n-1.689)/dn)
    return dl

theta = 52
dtheta = 0.5
n = n(theta)
print(n)
dn = delta_n(theta,dtheta,n)

lam = lambda_max(n)
dlam = delta_lam(lam, n, dn)

print(lam)
print(dlam)