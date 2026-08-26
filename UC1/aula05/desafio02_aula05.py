
ANO = 2026

for i in range (12):
    data_nasc = int (input ("Informe o ano de seu nascimento: \n"))
    idade = ANO - data_nasc

    if idade < 18:
        print ("Este cadastro é apenas para maiores de 18 anos!!!\n")
    else:
        nome = input ("Digite seu nome: \n")
        email = input ("Digite seu e-mail: \n")
        telefone = input ("Digite seu telefone: \n")
        print ("CADASTRO CONCLUIDO COM SUCESSO!!!\n")
