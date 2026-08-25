# impar_1 = 3
# impar_2 = 5
# impar_3 = 13
# impar_45 = 27

# # impares = []
# # print(type(impares))
# # impares = [3,5,13,27]
# # print(impares[3])

# lista_01 =[
#     12,
#     "Pedro",
#     12.53343,
#     "[{_{^^{}}}",
#     False,
#     0,
#     [2,4,6,8]
#     ]

# print(lista_01[1],lista_01[2],lista_01[4],lista_01[6][2])
 
# lista_02 = ["Márcio"]
# if "Márcia" in lista_02:
#     print(lista_02)
# else:
#     print("Márcia não esta presente na lista.")

#Looping
# participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]

# for participante in participantes:
#     print (participante)

# partic_2 = "Hugo"
# participantes.append(partic_2)
# participantes.insert(2,partic_2)
# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse()
# participantes.clear
# # print(participantes)
# participantes = ["Isaque","Luana","Fernando","Bianca","Ana Paula"]

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202
# }
# # print(numeros_pares,type(numeros_pares))
# numeros_impares ={111,111,112,291,205}
# print(numeros_pares.intersection(numeros_impares))
# numeros_pares.remove(205)
# print(numeros_pares)

#DICIONARIO

produtos = {"maça":5.99,"laranja":4.79}

print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))
produtos2 = produtos.copy()
#produtos2.pop("maça")
produtos2["maça"]=7.99
produtos.update()
print(produtos2)
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)


