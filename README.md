# ECSE543-NumericalMethods
 This repository contains the code corresponding to assignments 1 and 2 for the graduate numerical methods course, ECSE543.
#### @Author: Vasily G. Piccone
#### Languages: Python, MATLAB
#### Libraries used: numpy, matplotlib, datetime, copy

## Assignment 1
The objective for this assignment was to implement numerical solution schemes for Laplace's equation in 2D. The PDE arises from solving for the electrostatic potential (voltage) within a square co-axial cable, in which the inner conductor is held at 15 volts, and the outer conductor is held at 0 volts. Due to the symmetry of the problem, the square coaxial cable can divided into 4 sub-domains. Solving over one sub-domain provides the solution for the entire problem. 

### Question 1
Code which generates the S-matrices which arise from the finite element method was written in this question. The finite element is a square composed of two right angle triangles, defined by four (x, y) coordinate points. The coordinates serve as the arguments for this function, and the function returns the S-matrices.

### Question 2
The SIMPLE2D_M.m solves the finite element mesh with the input of a file that containing the vertices of the triangles over the problem domain.

### Question 3
The final question solves the same coaxial cable problem using the conjugate gradient method.

## Assignment 2
The objective of this assignment was to interpolate data, and solve various non-linear problems using iterative methods.

### Question 1
This question uses Lagrange interpolation and cubic hermite polynomials to interpolate data from a B-H curve.

### Question 2 
Using the data from question 1, the flux through an iron core was found using linear interpolation and the Newton-Raphson method. The area of the core was given, and the B-field value was calculated and thenn multiplied by areaa to obtain the flux. 

### Question 3 
The equations governing a circuit containing two diodes, a resistor and a voltage source were constructed, the unknowns being the voltages across the diodes. The Newton-Raphson method was then employed. 
