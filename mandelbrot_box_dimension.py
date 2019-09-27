#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:54:13 2019

@author: grogroda
"""

#O conjunto de Mandelbrot eh um fractal definido como o conjunto dos pontos c no
#plano complexo para o qual a sequencia z[n+1]=z[n]^2+c nao diverge

import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import stats as scistat

p=int(input('Numero de pontos:')) #usuario escolhe o numero de pontos no grafico, recomendo pelo menos 5 milhoes
m=int(input('Numero de termos maximo das sequencias:')) #isso determina a "precisao" para testar a sequencia

#parametros fixos
z0=complex(0,0)
Cx=[] #partes reais das constantes
Cy=[] #partes imaginarias das contantes
Cm=[]

#funcao que descobre se uma sequencia converge ou nao
def sequence(constant, z_0):
    zn=z0 #pois z0=0
    c=0 #contador
    while abs(zn)<2 and c<=m: #a sequencia certamente diverge para |zn|>=2 #para mostrar o conjunto em si, usar c<m
        zn=zn*zn+constant
        c=c+1 #implementando o contador ate o limite definido pelo usuario

    if c==m: #se o contador foi ate o final, ou seja, a sequencia nao estourou antes disso
        return 1
    else: #caso a sequencia estoure
        return 0

#testar a sequencia para p constantes escolhidas aleatoriamente
for i in range(p):
    C=complex(random.uniform(-2,0.5), random.uniform(-1.1,1.1))
    k=sequence(C,z0)

    if k==1: #k=1 significa que a funcao retornou um, entao a sequencia nao estourou
        Cm.append(C)
        Cx.append(C.real)
        Cy.append(C.imag)

print("Gerei Mandelbrot! =)")
####################################################################################
#### O código acima gera uma aproximação da borda do conjunto, com isso o resto ####
#### do codigo tentará calcular a dimensao fractal dessa borda, nessa parte#########
#### usarei o conceito de box-counting dimension ###################################
####################################################################################

sizes=[2**(-d) for d in range(2,8)] #lista com o tamanho das grids
invertsizes=[] #para fazer a dimensao eu preciso calcular o inverso de cada tamanho
nsquares=[] #o i-esimo termo da lista eh o numero de quadrados preenchidos no i-esimo tamanho
limits=[] #lista de listas com os pontos que definem as arestas dos quadrados

for i in range(len(sizes)):
    x=1/sizes[i]
    invertsizes.append(x)

for i in range(len(sizes)):
    Xi=[]
    for k in range(int(4//sizes[i])+1):
        xi=-2+k*sizes[i]
        Xi.append(xi)

    limits.append(Xi)

for i in range(len(sizes)):
    c=0

    for j in range(int(4//sizes[i])+1):
        for n in range(int(4//sizes[i])+1):
            for k in range(len(Cm)):

                if limits[i][j]<Cx[k]<limits[i][j+1] and limits[i][n]<Cy[k]<limits[i][n+1]:
                    c=c+1
                    break

                else:

                    continue

    nsquares.append(c)


print(scistat.linregress(np.log(invertsizes), np.log(nsquares)))
#print(nsquares)
print(len(Cm))
#print(limits)

plt.figure() #plota tudo junto

plt.subplot(121)
plt.scatter(Cx, Cy, s=0.2, c='Black', marker='.')
plt.axis([-2,0.5,-2,2])

plt.subplot(122)
plt.scatter(np.log(invertsizes), np.log(nsquares))

plt.show()