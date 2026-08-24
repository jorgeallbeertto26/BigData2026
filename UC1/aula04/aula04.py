# semana = 3
# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")

mes = 6
# match mes:
#  case 1:
#     print("Janeiro")
#  case 2:
#     print("Fevereiro")
#  case 3:
#     print("Março")
#  case 6:
#     print("Junho")
#  case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#     print("Mês inválido")

try:
    numero_mes = int(input("Digite um número de 1 a 12: "))
    match numero_mes:
        case 1:
            print ("O número 1 corresponde a Janeiro.")
        case 2:
            print ("O número 2 corresponde a Fevereiro.")
        case 3:
             print ("O número 3 corresponde a Março.")
        case 4:
             print ("O número 4 corresponde a Abril.")    
        case 5:
            print ("O número 5 corresponde a Maio.")
        case 6:
             print ("O número 6 corresponde a Junho.")
        case 7:
             print ("O número 7 corresponde a Julho.")
        case 8:
             print ("O número 8 corresponde a Agosto.")    
        case 9:
            print ("O número 9 corresponde a Setembro.")
        case 10:
             print ("O número 10 corresponde a Outubro.")
        case 11:
             print ("O número 11 corresponde a Novembro.")
        case 12:
             print ("O número 12 corresponde a Dezembro.")
except ValueError:
       print("Entrada invalida. Por favor, digite um número inteiro.")

