LARGURA_LAYOUT = 50

def separador(simbolo="-"):
    print(simbolo * LARGURA_LAYOUT)

def calcular_desempenho_academico():
    separador("=")
    print("SISTEMA DE GESTÃO DE NOTAS SEMESTRAIS".center(LARGURA_LAYOUT))
    separador("=")

    try:
        av1 = float(input("Digite a nota da Avaliação 1 (0 a 10): "))
        av2 = float(input("Digite a nota da Avaliação 2 (0 a 10): "))
        optativa = float(input("Digite a nota da Optativa (0 a 10 ou -1 se não fez): "))

        # Validação básica de valores
        if not (0 <= av1 <= 10) or not (0 <= av2 <= 10):
            separador()
            print("Erro: As notas normais (AV1 e AV2) devem estar entre 0 e 10.")
            separador()
            return

        if optativa != -1 and not (0 <= optativa <= 10):
            separador()
            print("Erro: A nota optativa deve estar entre 0 e 10, ou -1 caso não realizada.")
            separador()
            return

        # Aplicação da regra da avaliação optativa
        nota_final_1 = av1
        nota_final_2 = av2
        substituicao_feita = False

        if optativa != -1:
            # Substitui apenas se a optativa for maior que a menor nota
            if av1 < av2 and optativa > av1:
                nota_final_1 = optativa
                substituicao_feita = True
            elif av2 <= av1 and optativa > av2:
                nota_final_2 = optativa
                substituicao_feita = True

        # Cálculo da média semestral
        media = (nota_final_1 + nota_final_2) / 2

        # Definição da situação acadêmica
        if media >= 6.0:
            situacao = "APROVADO"
        elif media < 3.0:
            situacao = "REPROVADO"
        else:
            situacao = "RECUPERAÇÃO"

        # Exibição dos resultados
        separador()
        print(f"Notas Originais     : AV1 = {av1:.1f} | AV2 = {av2:.1f} | Opt = {optativa:.1f}")
        if substituicao_feita:
            print(f"Notas Computadas    : N1 = {nota_final_1:.1f} | N2 = {nota_final_2:.1f} (Houve substituição)")
        else:
            print(f"Notas Computadas    : N1 = {nota_final_1:.1f} | N2 = {nota_final_2:.1f}")
            
        print(f"Média Semestral     : {media:.2f}")
        print(f"Situação do Aluno   : {situacao}")
        separador("=")

    except ValueError:
        separador()
        print("Erro: Digite apenas números válidos para as notas.")
        separador()

if __name__ == "__main__":
    calcular_desempenho_academico()