# Constantes do sistema
PRECO_COMBUSTIVEL = 6.15
LARGURA_LAYOUT = 48

def traco(simbolo="-"):
    print(simbolo * LARGURA_LAYOUT)

def fechar_caixa_diario():
    traco("=")
    print("CONTROLE DE RENDIMENTO DIÁRIO - TÁXI".center(LARGURA_LAYOUT))
    traco("=")

    try:
        km_inicio = float(input("Odômetro inicial (km): "))
        km_fim = float(input("Odômetro final (km): "))
        litros_gastos = float(input("Litros de combustível consumidos (L): "))
        faturamento_bruto = float(input("Total arrecadado dos passageiros (R$): "))

        # Validações lógicas
        if km_fim < km_inicio:
            traco()
            print("Erro: A quilometragem final não pode ser menor que a inicial.")
            traco()
            return

        if litros_gastos <= 0 or faturamento_bruto < 0:
            traco()
            print("Erro: Litros gastos devem ser maiores que zero e receita válida.")
            traco()
            return

        # Cálculos de desempenho e financeiro
        distancia_total = km_fim - km_inicio
        consumo_medio = distancia_total / litros_gastos
        custo_combustivel = litros_gastos * PRECO_COMBUSTIVEL
        lucro_liquido = faturamento_bruto - custo_combustivel

        # Exibição do fechamento
        traco()
        print(f"Distância Percorrida  : {distancia_total:.1f} km")
        print(f"Consumo Médio         : {consumo_medio:.2f} km/L")
        print(f"Despesa Combustível   : R$ {custo_combustivel:.2f} (a R$ {PRECO_COMBUSTIVEL:.2f}/L)")
        print(f"Faturamento Bruto     : R$ {faturamento_bruto:.2f}")
        traco()
        
        # Análise do resultado financeiro
        if lucro_liquido > 0:
            print(f"LUCRO LÍQUIDO DO DIA  : R$ {lucro_liquido:.2f}")
        elif lucro_liquido == 0:
            print("LUCRO LÍQUIDO DO DIA  : R$ 0.00 (Empatou os custos)")
        else:
            print(f"PREJUÍZO DO DIA       : -R$ {abs(lucro_liquido):.2f}")
            
        traco("=")

    except ValueError:
        traco()
        print("Erro: Digite apenas números válidos para os valores.")
        traco()

if __name__ == "__main__":
    fechar_caixa_diario()