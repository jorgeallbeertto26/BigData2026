
# def calculadora_v1 (num1,num2,operador="3"):

# # num1=float(input("Digite seu primeiro numero: "))
# # num2=float(input("Digite seu segundo numero: "))
# # operador=input("Informe a operação desejada entre: 1. adição")

#     match operador:
#         case "1":
#             print (f"Resultado da soma:{num1+num2}.")
#         case "2":
#             print(f"Resultado da subtração: {num1-num2}.")
#         case "3":
#             print(f"Resultado da multiplicação: {num1*num2}.")
#         case "4":
#                 if num2!=0:
#                     print(f"Resultado da divisão: {num1/num2}.")
#                 else:
#                     print("Dividiu por zero. ERROOOOU.")
#         case _ :
#                     print("Informe um operador valido.")

# calculinho = calculadora_v1(3323,111)

# print (calculinho)




def calculadora_v1 (num1,num2,operador="3"):

# num1=float(input("Digite seu primeiro numero: "))
# num2=float(input("Digite seu segundo numero: "))
# operador=input("Informe a operação desejada entre: 1. adição")

    match operador:
        case "1":
           resultado = num1+num2
        case "2":
            resultado = num1-num2
        case "3":
            resultado = num1*num2
        case "4":
                if num2!=0:
                    resultado = num1/num2
                else:
                    print("Dividiu por zero. ERROOOOU.")
        case _ :
                    print("Informe um operador valido.")

    return resultado

calculinho = calculadora_v1(3323,111)

print (calculinho)


