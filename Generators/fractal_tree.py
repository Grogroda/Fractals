#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:55:15 2020

@author: grogroda
"""

import turtle 

rafa=turtle.Turtle() #quero chamar minha tartaruga de rafa, pq sim
        
N=8

rafa.seth(90)
rafa.forward(80)
finalpoints=[rafa.pos()]
finalheadings=[rafa.heading()]

for j in range(N):
    
    newpoints=[]
    newheadings=[]
    
    for i in range(len(finalpoints)):
        
        rafa.pu()
        rafa.setpos(finalpoints[i])
        rafa.seth(finalheadings[i])
        rafa.pd()
        
        rafa.left(20)
        rafa.fd(80*((0.67)**(j+1)))
        
        newpoints.append(rafa.pos())
        newheadings.append(rafa.heading())
        
        rafa.setpos(finalpoints[i])
        rafa.right(40)
        rafa.fd(80*((0.67)**(j+1)))
        
        newpoints.append(rafa.pos())
        newheadings.append(rafa.heading())
        
    finalpoints=newpoints
    finalheadings=newheadings
    
rafa.hideturtle()
    
turtle.Screen().exitonclick()
    
    
        
        