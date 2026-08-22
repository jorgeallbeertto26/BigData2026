# nota_1 = 5
# nota_2 = 6
# nota_3 = 2
# nota_4 = 3
# media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# print(media)
# if media > 7:
#     print ("Aprovado")
# elif media >= 5 and media <= 7:
#     print ("Recuperação")
# else:
#     print("Reprovado")

name = input("Informe o nome do aluno: ")
nota1 = float (input ("Informe a 1ª nota: "))
nota2 = float (input ("Informe a 2ª nota: "))
nota3 = float (input ("Informe a 3ª nota: "))
nota4 = float (input ("Informe a 4ª nota: "))
media = (nota1 + nota2 + nota3 + nota4) /4
print (media)

if media > 7:
    print ("Aprovado")
elif media >= 5 and media <= 7:
    print ("Recuperação")
else:
    print("Reprovado")