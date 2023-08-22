import sys
import math
precision = float(sys.argv[1])
a = math.pi/4
print(a)
terminar = 0
aproximacion = 0
i=0
while terminar == 0:
    aproximacion = aproximacion + 1/((2*i+1))*(-1)**(i)
    i+=1
    error = abs(a-aproximacion)
    if error>precision:
        terminar = 0
    else:
        terminar = 1
print(aproximacion)