
import math

m = float (input ("Mass (in Kg): " ) )
g = float (input ("Gravity (9.8 m/s^2 for Earth, 24 m/s^2 for Jupiter): "))
t = float (input ("Time (in seconds): " ) )
p = float (input ("Desity of fluid (in kg/m^3, 1.3 for air, 1000 for water): " ) )
A = float (input ("Cross sectional are (in m^2): " ) )
C = float (input ("Drag constant (0.5 for sphere, 1.1 for cylinder falling on its side.)" ) )

c = (1 / 2) * p * A * C

v = ( math.sqrt ( ( m * g ) / c ) ) * ( 1 - math.exp ( ( ( - math.sqrt (m * g * c) ) / m ) * t ) )

print ( "-"*20)
print ( f"The inner value of c is: {c:.3f}" )
print ( "-"*20)
print ( "-"*20)
print ( f"The velocity after {t} seconds is: {v:.3f} M/s" )
print ( "-"*20)
