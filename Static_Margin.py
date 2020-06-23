print('##### Calculador de Margem Estatica #####')
c = 0.16        # corda media aerodinamica da asa
xca = 0.040     # posição do centro aerodinamico
n = 0.95        # eficiencia
clasa = 0.060   # derivada da Cl x Alfa da asa
arasa = 5.00    # ar da asa
clpro = 0.040   # derivada da Cl x Alfa do profundor
s = 0.4000      # area da asa
sht = 0.1000    # area do profundor
lht = 0.40      # distancia do CG ate o CA do profundor
xcg = 0.07      # posição do CG

clasa = clasa*(1/0.01745) 
clpro = clpro*(1/0.01745)
vh = (lht*sht)/(c*s)
de = (2*clasa)/(3.1415*arasa)
hpn = (xca/c) + (vh*n*clpro)/(clasa)*(1-de)
hpg = xcg/c

me = hpn-hpg

print('Valor da Margem Estatica %f' % me)

