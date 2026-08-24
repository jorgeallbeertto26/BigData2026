LARGURA_LAYOUT = 45

def linha(caractere="-"):
    print(caractere * LARGURA_LAYOUT)

def identificar_origem_produto():
    linha("=")
    print("CONSULTA DE ORIGEM DE PRODUTO".center(LARGURA_LAYOUT))
    linha("=")

    try:
        codigo = int(input("Informe o código de origem do produto: "))

        # Classificação por região
        if codigo == 1:
            procedencia = "Sul"
        elif codigo == 2:
            procedencia = "Norte"
        elif codigo == 3:
            procedencia = "Leste"
        elif codigo == 4:
            procedencia = "Oeste"
        elif codigo in (5, 6):
            procedencia = "Nordeste"
        elif codigo in (7, 8, 9):
            procedencia = "Sudeste"
        elif 10 <= codigo <= 20:
            procedencia = "Centro-Oeste"
        elif 25 <= codigo <= 30:
            procedencia = "Noroeste"
        else:
            procedencia = "Importado"

        # Exibição do resultado
        linha()
        print(f"Código Informado : {codigo}")
        print(f"Procedência      : {procedencia}")
        linha("=")

    except ValueError:
        linha()
        print("Erro: Digite apenas valores numéricos inteiros para o código.")
        linha()

if __name__ == "__main__":
    identificar_origem_produto()