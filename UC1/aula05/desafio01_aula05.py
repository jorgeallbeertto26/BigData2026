
ntentativas = 3
user = "admin"
passw = "123456"


def are_credentials_valid(username_input, password_input):
    return username_input == user and password_input == passw

for attempt_index in range(ntentativas):
    remaining_attempts = ntentativas - (attempt_index + 1)
    username_input = input("Usuário: ")
    password_input = input("Senha: ")

    if are_credentials_valid(username_input, password_input):
        print("Acesso concedido!")
        break
    elif attempt_index < (ntentativas - 1):
        print(f"Credenciais inválidas. Você tem mais",{remaining_attempts},"tentativas.")
    else:
        print("Login bloqueado. Entre em contato com o suporte.")
       