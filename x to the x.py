# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:48:37 2022

@author: almon
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw
plt.rcParams.update({'font.size': 32,'axes.linewidth':2,'lines.linewidth':2})

# Solving the equation x^x = a
# Often we rewrite the problem to be x^x - a = 0
max_error = 1e-6
a = 55

def f(x, a):
    return x**x - a

def f_prime(x, a):
    return x**x*(1 + np.log(x))

x = np.linspace(2,4, 1000)
y = f(x, a)
plt.figure(figsize=(12, 8))
plt.plot(x,y)
plt.xlabel(r"$x$")
plt.ylabel(r"$x^x - $" + str(a))

# Relazation method, get the system into a form f(x) = x then iteratively solve
x = 3  # Our first guess, based on the graph
error = 1  # Initalize error to be higher than max_error
while error > max_error:
    x_f = np.log(a)/np.log(x)
    error = abs(x - x_f)
    x = x_f
print(f"Using the relaxation method we find x to be: {x}")

# Binary search method, start with a window around the solution and narrow in
x_l = 0
x_r = 5
error = 1
while error > max_error:
    x_mid = 1/2*(x_l + x_r)
    f_new = f(x_mid, a)
    # If the point on the left is the same sign as the midpoint, move the
    # left point to the middle narrowing the window
    if np.sign(f_new) == np.sign(f(x_l, a)):
        x_l = x_mid
    # Else move the right point to the middle
    else:
        x_r = x_mid
    error = abs(x_r - x_l)
x = 1/2*(x_l + x_r)
print(f"Using the binary search method we find x to be: {x}")


# Newton's method, 
x = 3
error = 1
while error > max_error:
    x_new = x - f(x, a)/f_prime(x, a)
    error = abs(x_new - x)
    x = x_new
print(f"Using Newton's method we find x to be: {x_new}")

# Exact solution
x = np.exp(lambertw(np.log(a)))
print(f"Using exact solution we find x to be: {x_new}")