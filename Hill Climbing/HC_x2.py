import random

def Ajusta(s0):
    result = s0 * 0.90
    return result

def Qualidade(s0):
    return s0

#fo
def fo(s0):
    z = s0**2
    return z

#inicialização das variaveis de decisão
s0 = random.uniform(-10,10)
s = s0
print("Solução inicial \nS0: ", s0, "f(x): ", fo(s0))
i = 0
while i < 50: #Quantidade de gerações
    r = Ajusta(s) #fator de ajuste
    if(fo(r) < fo(s)): #se o ótimo local melhorar
        s = r
    i = i + 1
print("Solução ótima\nS': ", s, ", f(x): ", fo(s))
