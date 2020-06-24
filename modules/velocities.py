
b = 2.77 # wing span
p = 1.1504 # rho
vmax = 18.52 # max speed - performance area
CLmax = 1.7821 # Lift Coefficient aircraft 
S = 0.70635 # Wing Area
m = 8.6 # MTOW
W = m * 9.7925 
nmax = 2.5 # maximum load factor
nmax_neg = -0.4*nmax
CLinvertido = -1

vs_pos = ((2*W)/(CLmax*S*p)) ** 0.5
vs_ = (2*W*nmax_neg/(S*CLinvertido*p)) ** 0.5
va = vs_pos * (nmax ** 0.5)
print ('manouver speed =', va)
vc = 0.9*vmax
print('cruze speed =', vc)
vd = 1.25*vmax
print('dive speed =', vd)
takeoffSpeed = 0.6 * vmax
divergenceSpeed = 3 * vmax
