import math
print('Welcome to the velocity calculator. Please enter the following: ')
m=float(input('Mass (in kg): '))
g=float(input('Gravity (in m/s^2, for Earth 9.8, for Jupiter 24): '))
t=int(input('Time (in seconds): '))
p=float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A=float(input('Cross sectional are (in m^2): '))
C=float(input('Drag constant(0.5 for sphere, 1.1 for cylinder):'))
c=(1/2)*p*A*C
v=math.sqrt(m*g/c)*(1-math.exp(-math.sqrt(m*g*c)/m)*t)
v_terminal=math.sqrt(m*g/c)
print(f'\nThe inner value of c is: {c:.3f}')
print(f'The velocity after 10.0 seconds is: {v:.3f} m/s')
print(f'The terminal velocity would be: {v_terminal:.3f}')