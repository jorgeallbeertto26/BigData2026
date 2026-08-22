#### ESTRUTURAS DE REPETIÇÃO 
# FOR
# for i in range(2,101,2):
#    print(i)

#WHILE

# somador = int(input("Registro:"))
# controle = 0

# while controle  <= 30:
#     controle=controle+somador
#     somador = int(input("Registro:"))

# print ("Oficina lotada!!")
# print ("A oficina está com", controle, "clientes neste momento!!!")

######for i
# for i in range(5):
#     try:
#         # i representa o número atual da repetição (0, 1, 2...)
#         print (f"Numero {i+1} de 5:")
#         num = float(input("Digite um numero:"))

#         dobro = num * 2
#         triplo = num * 3
#         quadrupulo = num * 4

#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quadrupulo={quadrupulo}\n")

#     except ValueError:
#         print ("Entrada inválida. Tente novamente")


# acertou = 0
# while acertou < 5:
#         print (f"Numero {acertou + 1} de 5:")     
#         num = float(input("Digite um numero:"))
#         print ("Nymero de tentativas",acertou)

#         dobro = num * 2
#         triplo = num * 3
#         quadrupulo = num * 4

#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quadrupulo={quadrupulo}\n")
#         acertou += 1


# DO WHILE
contador = 0
limite = 5

while True:
    if contador >= limite:
        break # Ponto de decisao: Se o limite for atingido

    try:
        contador += 1
        print (f"Número {contador} de {limite}:")
        num = float(input("Digite um numero: "))
        
        dobro = num * 2
        triplo = num * 3
        quadrupulo = num * 4

        print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quadrupulo={quadrupulo}\n")
        print ("Tentativas", contador)
    except ValueError:
        print ("Uma mensagem de erro!!!")   

