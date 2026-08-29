

nusuarios = int (input ("Quantidade usuários: "))
cont_usuarios=0

for i in range (nusuarios):
    
    peso = float (input ("Informe o peso: "))
    altura = float (input ("Informe a altura: "))
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        print(imc, " Abaixo do peso🙄\n")
    elif imc >= 18.5 and imc <= 24.9:
        print (imc, " Peso normal😂\n")
    elif imc > 24.9 and imc <= 29.9:
         print (imc, " Sobrepeso😒\n")
    elif imc > 30:
        print(f"{imc} \033[3;31mObesidade😤\033[0m\n")
    
    
    
  




# ntentativas = 3
# user = "admin"
# passw = "123456"


# def are_credentials_valid(username_input, password_input):
#     return username_input == user and password_input == passw

# for attempt_index in range(ntentativas):
#     remaining_attempts = ntentativas - (attempt_index + 1)
#     username_input = input("Usuário: ")
#     password_input = input("Senha: ")

#     if are_credentials_valid(username_input, password_input):
#         print("Acesso concedido!")
#         break
#     elif attempt_index < (ntentativas - 1):
#         print(f"Credenciais inválidas. Você tem mais",{remaining_attempts},"tentativas.")
#     else:
#         print("Login bloqueado. Entre em contato com o suporte.")