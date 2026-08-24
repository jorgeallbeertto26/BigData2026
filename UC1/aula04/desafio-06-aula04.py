LARGURA_LAYOUT = 40

def linha(caractere="-"):
    print(caractere * LARGURA_LAYOUT)

def verificar_sinal():
    linha("=")
    print("VERIFICADOR DE SINAL NUMÉRICO".center(LARGURA_LAYOUT))
    linha("=")

    try:
        valor = float(input("Digite um número: "))

        linha()
        if valor >= 0:
            print(f"O número {valor} é POSITIVO.")
        else:
            print(f"O número {valor} é NEGATIVO.")
        linha("=")

    except ValueError:
        linha()
        print("Erro: Entrada inválida. Digite um valor numérico.")
        linha()

if __name__ == "__main__":
    verificar_sinal()