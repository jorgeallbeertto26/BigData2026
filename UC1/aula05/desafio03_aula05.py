
USER_S = "admin"
PASSW = "123456"
cont=0
qtdtentativas=0
for i in range (3):
    valida_user = (input ("Usuário: "))
    valida_passw = (input ("Senha: "))

    if valida_user == USER_S and valida_passw == PASSW:
        print ("Usuario logado com sucesso:::\n")
        break

    cont+=1
    qtdtentativas +=1
    print ("Você ja tenhou", qtdtentativas)

    if cont == 3:
        print ("Numero de tentativas excedidas!!!")
        print ("Se ferrou!!!")
    # else:
    #     nome = input ("Digite seu nome: \n")
    #     email = input ("Digite seu e-mail: \n")
    #     telefone = input ("Digite seu telefone: \n")
    #     print ("CADASTRO CONCLUIDO COM SUCESSO!!!\n")
