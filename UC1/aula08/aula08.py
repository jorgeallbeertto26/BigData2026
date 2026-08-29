import time
#. DEFINIÇÃO DA FUNCAO

def dar_boas_vindas():
    print ("-"*40)
    print (" Bem vindo ao nosso aplicativo!  😁")
    print ("-"*40)

    #2. CHAMADA DA FUNÇÃO
    #O código abaixo sera executado se você "chamar" a funcao pelo nome.

    print("Início do programa.")
    print("Por favor, aguarde... ")
    time.sleep(2) #Simula uma pausa
    dar_boas_vindas()  #<-- Isso executa o código dentro da função
    print ("Meio do programa")
    dar_boas_vindas() #<-- Podemos chamar de novo