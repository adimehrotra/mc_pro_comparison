#first need linear approximation 

#then write function that inputs gear ratios 
#and spits out the new torque speed curve 
#so we have a MAX TORQUE limit and a MX SPEED limit (look @ ben's curve)

#max torque, max speed, constant power line 
#and a CONSTRAINT ON THE MAX POWER !!!! 

from numpy import arange
import matplotlib.pyplot as plt

#setup constraints
POWER_LIMIT = 2.7*60 #Nm*rads/s = W
SATURATION_TORQUE = 2.7 #Nm
FREE_SPEED = 195.0 #rads/s

#setup search discretization
discretization_t = 0.05
discretization_v = 1.0

#T/S Key Points
point1 = (30.0, 33.0)
point2 = (210.0, 0.0)
m = (point2[1]-point1[1]) / (point2[0]-point1[0])
b = point1[1] - m * point1[0]
print(b)

levels = arange(0.0, POWER_LIMIT+50.0, 10.0)

#generate the arrays
taus = []
vs = []
ps = []
for tau in arange(0.0, SATURATION_TORQUE, discretization_t):
    for vel in arange(0.0, FREE_SPEED, discretization_v):
        if tau <= m * vel + b:
            taus.append(tau)
            vs.append(vel)
            ps.append(tau*vel)

plt.tricontourf(vs, taus, ps, levels=levels)
plt.show()


#NOTE THIS DOES NOT WORK, IT DOESNT COVER THE WHOLE RANGE OF T/S CURVE POSSIBILITIES 


#NOTE:
#SO THIS IS NOT ACCURATE BECAUSE THE LINE IS NOT REALLY THE CONSTANT POWER LINE 
#WHAT's ACTUATLLY HAPPENING IS IN THAT REGION THE INDUCTANCE AND RESISTANCE IS LIMITING THE VALUE
#THAT THE BACK_EMF CAN ACHIEVE, AND IF VEL = K_m * V_BEMF THEN THAT LIMITS THE VELOCITY OF THE MOTOR
#NOTE: voltage drop over the inductor and the resistor also play a part

#TS MODIFIERS IN DESMOS: https://www.desmos.com/calculator/slndwo5eh1

#NOTE: Better to do a linear approximation