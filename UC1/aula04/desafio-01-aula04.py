import math

# Configurações do cálculo e layout
POTENCIA_POR_M2 = 3.0       # Watts por metro quadrado
AREA_POR_PONTO_LUZ = 3.0    # m² por bocal
TAMANHO_DIVISOR = 45

def exibir_divisor(simbolo="-"):
    print(simbolo * TAMANHO_DIVISOR)

def dimensionar_iluminacao():
    exibir_divisor("=")
    print("SISTEMA DE DIMENSIONAMENTO LUMINOTÉCNICO".center(TAMANHO_DIVISOR))
    exibir_divisor("=")

    try:
        pot_lampada = float(input("Potência unitária da lâmpada (W): "))
        largura = float(input("Largura do ambiente (m): "))
        comprimento = float(input("Comprimento do ambiente (m): "))

        # Validação de integridade dos dados
        if pot_lampada <= 0 or largura <= 0 or comprimento <= 0:
            exibir_divisor()
            print("Erro: Todas as medidas devem ser estritamente positivas.")
            exibir_divisor()
            return

        # Cálculos de engenharia
        area_total = largura * comprimento
        demanda_termica_watts = area_total * POTENCIA_POR_M2
        
        # Quantidade de lâmpadas calculada com arredondamento para cima
        total_lampadas = math.ceil(demanda_termica_watts / pot_lampada)
        
        # Quantidade física de bocais instalados (mínimo 1 se o cômodo for menor que 3m²)
        bocais_instalados = max(1, math.floor(area_total / AREA_POR_PONTO_LUZ))

        # Relatório de saída
        exibir_divisor()
        print(f"Dimensão do Ambiente    : {area_total:.2f} m²")
        print(f"Demanda Total de Carga  : {demanda_termica_watts:.2f} W")
        print(f"Pontos de Luz no Teto   : {bocais_instalados} bocal(is)")
        print(f"Lâmpadas Solicitadas    : {total_lampadas} un ({pot_lampada:.0f}W cada)")
        exibir_divisor()

        # Parecer técnico da instalação
        if total_lampadas > bocais_instalados:
            print("Alerta: A estrutura física não suporta essa potência.")
            print(f"Faltam {total_lampadas - bocais_instalados} ponto(s) de fixação para suprir a luminosidade.")
        elif total_lampadas == bocais_instalados:
            print("Status: Instalação ideal. 100% dos bocais serão ocupados.")
        else:
            pontos_livres = bocais_instalados - total_lampadas
            print(f"Status: O ambiente ficará iluminado e restarão {pontos_livres} bocal(is) livres.")

        exibir_divisor("=")

    except ValueError:
        exibir_divisor()
        print("Erro de formato: Utilize apenas números para preencher os campos.")
        exibir_divisor()

if __name__ == "__main__":
    dimensionar_iluminacao()