#FUNCOES E MODULOS

def sorteaime ():
    '''
    Algoritmo escolhe e retorna um numero
    inteiro aleatorio no intervalo de 1 até 30.
    '''
    import random
    
    numero_random = random.randint(1,30)

    return numero_random
resultado = sorteaime()
print(resultado)






