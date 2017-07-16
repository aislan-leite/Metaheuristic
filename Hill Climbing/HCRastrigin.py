import math
import random

#Benchmarck Rastrigin
def fo(x,y):
    z = 20 + (x * x - 10 * (math.cos(2 * math.pi * x))) + (y * y - 10 * (math.cos(2 * math.pi * y)))
    return z

#inicialização das variaveis de decisão
s0 = random.uniform(-5.12,5.12)
s1 = random.uniform(-5.12,5.12)
sx = s0 #variavel atual de s0
sy = s1 #variavel atual de s1
atual_sol = fo(sx,sy)
print("Solução inicial \nS0: ", sx, ", s1: ", sy, ", f(x): ", fo(sx,sy))

i = 0
while i < 100000:
        ajuste = sx * 0.1 #pertubação de 10%
        if(atual_sol > fo(sx+ajuste,sy)):
            sx = sx + ajuste
            atual_sol = fo(sx,sy)
        elif(atual_sol > fo(sx-ajuste,sy)):
            sx = sx - ajuste
            atual_sol = fo(sx,sy)

        ajuste = sy * 0.1 #pertubação de 10%
        if(atual_sol > fo(sx,sy+ajuste)):
            sy = sy + ajuste
            atual_sol = fo(sx,sy)
        elif(atual_sol > fo(sx, sy-ajuste)):
            sy = sy - ajuste
            atual_sol = fo(sx, sy)
        i = i + 1
print("X: ", sx, ", Y: ", sy, ", f(x): ", fo(sx,sy))
