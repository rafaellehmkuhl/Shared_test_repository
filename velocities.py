
b = 2.77 # envergadura da asa
p = 1.1504 # rho
vmax = 18.52 # velocidade máxima - desempenho
CLmax = 1.7821 # CLmax aviao todo 
S = 0.70635 # Area da asa
m = 8.6 # MTOW
W = m * 9.7925 
nmax = 2.5 # fator de carga maximo
nmax_neg = -0.4*nmax
CLinvertido = -1

vs_pos = ((2*W)/(CLmax*S*p)) ** 0.5
vs_ = (2*W*nmax_neg/(S*CLinvertido*p)) ** 0.5
va = vs_pos * (nmax ** 0.5)
print ('Velocidade de manobra =', va)
vc = 0.9*vmax
print('Velocidade de cruzeiro =', vc)
vd = 1.25*vmax
print('Velocidade de mergulho =', vd)
takeoffSpeed = 0.6 * vmax