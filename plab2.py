import math
def seriefor(cant_terminos):
    t_for = []
    aproximacion = 0
    for i in range(cant_terminos):
        aproximacion = aproximacion + 1/((2*i+1))*(-1)**(i)
        t_for.append(aproximacion)
    return aproximacion, t_for

def seriewhile1(precision,referencia):
    aproximacion = 0
    i = 0
    t_w1 = []
    error = 1
    while error >= precision:
        aproximacion = aproximacion + 1/((2*i+1))*(-1)**(i)
        t_w1.append(aproximacion)  
        i+=1
        error = abs(aproximacion-referencia)
    return aproximacion, t_w1

def seriewhile2(precision):
    aproximacion = 0
    valor_serie = math.pi/4
    i = 0
    t_w2 = []
    error = 1
    while error >= precision:
        aproximacion = aproximacion + 1/((2*i+1))*(-1)**(i)
        t_w2.append(aproximacion)  
        i+=1
        error = abs(aproximacion-valor_serie)
    return aproximacion, t_w2


N = 4000
valorseriefor,t_for = seriefor(N)
print("El valor calculado por la serie for es:",valorseriefor)

precisionw1 = 1e-4
referenciaw1 = math.pi/4
valorseriew1,t_w1 = seriewhile1(precisionw1,referenciaw1)
print("El valor por la serie while1 es: ", valorseriew1)

precision_w2 = 1e-5
valorseriew2,t_w2 = seriewhile2(precision_w2)
print("El valor calculado por la serie while2 es:", valorseriew2)