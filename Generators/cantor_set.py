#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:06:27 2019

@author: grogroda
"""

from matplotlib import pyplot as plt
import numpy as np
from scipy import stats as scistat
import random

## Cantor Set: Esse programa criara uma versao finita do conjunto de Cantor, ##
## alem de medir numericamente sua dimensao fractal. ##########################

#print('Seja 10>N>0 o numero de iteracoes, vao ser construidas N linhas do conjunto de Cantor')

N=6 #int(input('Numero de iteracoes (Resolucao ruim a partir de 6):'))

intervalos=[[[i+1 for i in range(3**10)]]]
plot=[[i+1 for i in range(3**10)]]
points=[]

def slicer(intervalo): #cria uma lista com as duas pontas da terça parte separadas como sublistas - vai nas interacoes seguintes
    slicing=[]
    slicing.append(intervalo[0:(len(intervalo)//3)])
    slicing.append(intervalo[2*(len(intervalo)//3):(len(intervalo))])
    
    return slicing

def sliced(intervalo): #cria uma lista com as duas pontas da terça parte em uma unica lista - vai no plot
    intervalofinal=[]
    for i in range(len(intervalo[0:(len(intervalo)//3)])):
        intervalofinal.append(intervalo[i])
        
    for i in range(len(intervalo[2*(len(intervalo)//3):(len(intervalo))])):
        intervalofinal.append(intervalo[i+2*(len(intervalo)//3)])
    
    return intervalofinal
    
for i in range(N):
    
    n=[]
    m=[]
    
    for j in range(len(intervalos[i])):
        
        a=slicer(intervalos[i][j])
        m=m+a
        
        b=sliced(intervalos[i][j])
        n=n+b
        
    intervalos.append(m)
    plot.append(n)

for i in range(N):
    plt.scatter(plot[i], [10-i for j in range(len(plot[i]))], marker='.', s=0.01,c='black')
    
    for j in range(len(plot[i])):
        points.append((plot[i][j], 10-i))

def correlationdimension(pointlist):
    
    N=[] 
    Ce=[]
    raios=[] 

    for i in range(1,21):
        R=0.2*i
        raios.append(R)       

    for p in range(200): #tirarei a media para varios pontos iniciais
        C0=pointlist[random.randint(0,len(pointlist))] #toma um ponto inicial aleatório para fazer a pointwise dimension
        Np=[]
    
        for i in range(1,21): #serao testadas 20  circunferências
            c=0 #contador
            R=0.2*i #raio do teste
            for j in range(len(pointlist)): 
            
                if (pointlist[j][0]-C0[0])**2+(pointlist[j][1]-C0[1])**2<R**2: #testando cada ponto Cj para ver se ta dentro do circulo
                    c=c+1 #se estiver, vai no contador
            
            Np.append(c) #Np é a lista de números de pontos para o p-esimo C0
        N.append(Np) #N é uma lista das listas Np

    for j in range(len(raios)): 
        k=0
        for i in range(len(N)): #para cada ponto inicial tiramos a media do#
            k=k+N[i][j]            #numero de pontos na i-esima circunferencia#
                               
        media=k/(len(N))
        Ce.append(media)  #Ce=C(epsilon), é a média de cada ponto 

    print(scistat.linregress(np.log(raios)[0:7], np.log(Ce)[0:7])) #imprime os parametros do mmq


#print(points)

correlationdimension(points[len(points)-1-(2**5)*(3**5):])
plt.show()