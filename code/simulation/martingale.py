# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:06:47 2017

@author: Anton
"""
from random import random
import math
import matplotlib.pyplot as plt
import numpy

def simulate_by_probability(n, probabilities, start_value):
    values = []
    current_value = start_value
    for i in range(n):
        threshold = random()
        if threshold < probabilities[i]:
            values.append(current_value+1)
        if threshold >= probabilities[i]:
            values.append(current_value-1)
        current_value = values[i]
        
    return values

def martingale(values, probabilities,omega,gamma):
    x = []
    sum = 0
    end_value = 0
    for i in range(len(probabilities)):
        sum = sum + ((gamma+1)*probabilities[i]-1)**2
    
    sum = math.sqrt(sum)
    for i in range(len(values)):
        x.append(omega*((gamma+1)-1)/(sum))
    
    for i in range(1,len(x)):
        if values[i]<values[i-1]:
            end_value -= x[i-1]
        else:
            end_value += x[i-1]*gamma
        print(end_value)
    return end_value,x

def get_probabilities(n):
    probabilities = []
    for i in range(n):
        probabilities.append(random())
    return probabilities

n = 100
probs = get_probabilities(n)
values = simulate_by_probability(n,probs,0)
end_value,x= martingale(values,probs,100,2)
print(end_value)
print(values)
print(x)
print(probs)