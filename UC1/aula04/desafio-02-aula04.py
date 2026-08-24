import math

# Constantes do projeto
RENDIMENTO_CAIXA_M2 = 1.5
LARGURA_LINHA = 46

def imprimir_linha(caractere="-"):
    print(caractere * LARGURA_LINHA)

def calcular_revestimento_cozinha():
    imprimir_linha("=")
    print("ORÇAMENTO DE REVESTIMENTO: PAREDES DA COZINHA".center(LARGURA_LINHA))
    imprimir_linha("=")

    try:
        comprimento = float(input("Digite o comprimento da cozinha (m): "))
        largura = float(input("Digite a largura da cozinha (m): "))
        altura = float(input("Digite a altura/pé-direito (m): "))

        # Validação de entradas
        if comprimento <= 0 or largura <= 0 or altura <= 0:
            imprimir_linha()
            print("Erro: As dimensões devem ser maiores que zero.")
            imprimir_linha()
            return

        # Cálculo da área total das 4 paredes: 2*(comprimento * altura) + 2*(largura * altura)
        perimetro = 2 * (comprimento + largura)
        area_paredes = perimetro * altura

        # Quantidade de caixas necessárias (arredondando sempre para cima)
        total_caixas = math.ceil(area_paredes / RENDIMENTO_CAIXA_M2)
        cobertura_total_caixas = total_caixas * RENDIMENTO_CAIXA_M2
        sobra_material = cobertura_total_caixas - area_paredes

        # Exibição do resumo
        imprimir_linha()
        print(f"Perímetro do Cômodo     : {perimetro:.2f} m")
        print(f"Área Total das Paredes  : {area_paredes:.2f} m²")
        print(f"Rendimento por Caixa    : {RENDIMENTO_CAIXA_M2:.2f} m²")
        print(f"Caixas Necessárias      : {total_caixas} caixa(s)")
        print(f"Área Comprada           : {cobertura_total_caixas:.2f} m² (Sobra: {sobra_material:.2f} m²)")
        imprimir_linha("=")

    except ValueError:
        imprimir_linha()
        print("Erro: Digite apenas valores numéricos válidos.")
        imprimir_linha()

if __name__ == "__main__":
    calcular_revestimento_cozinha()