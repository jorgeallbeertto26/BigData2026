import pandas as pd

# 1. Carregando o arquivo Excel e lendo cada aba especificamente
arquivo = 'base_invest.xlsx'
df_transacoes = pd.read_excel(arquivo, sheet_name='Transacoes')
df_ativo = pd.read_excel(arquivo, sheet_name='Ativo')
df_participante = pd.read_excel(arquivo, sheet_name='Participante')
df_historico = pd.read_excel(arquivo, sheet_name='HistoricoPrecos')

# Criando uma coluna de Valor Total da Transação (Quantidade * Preço)
df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']

print("-" * 50)
# --- PERGUNTA 1: Quais são as máximas e mínimas de operação de compra e venda? ---
print("1. MÁXIMAS E MÍNIMAS DAS TRANSAÇÕES DE COMPRA E VENDA (Valor Total):")
max_min = df_transacoes.groupby('operacao')['valor_total'].agg(Máxima='max', Mínima='min')
print(max_min)
print("-" * 50)

# --- PERGUNTA 2: Qual CNPJ tem o ativo de maior valor? ---
print("2. CNPJ DO ATIVO DE MAIOR VALOR:")
# Encontra a linha com o maior preço no histórico
indice_maior_preco = df_historico['preco'].idxmax()
id_ativo_max = df_historico.loc[indice_maior_preco, 'id_ativo']
maior_preco = df_historico.loc[indice_maior_preco, 'preco']

# Procura o id_ativo na tabela de Ativos para pegar o CNPJ
cnpj_resultado = df_ativo.loc[df_ativo['id_ativo'] == id_ativo_max, 'cnpj'].values[0]

print(f"O CNPJ '{cnpj_resultado}' tem o ativo de maior valor (R$ {maior_preco:.2f}).")
print("-" * 50)

# --- PERGUNTA 3: Qual valor total em transações de cada participante? ---
print("3. VALOR TOTAL EM TRANSAÇÕES POR PARTICIPANTE:")
# Junta a tabela de transações com a tabela de participantes usando a coluna em comum 'id_participante'
df_completo = pd.merge(df_transacoes, df_participante, on='id_participante')

# Agrupa pelo nome do participante e soma o valor total
total_por_participante = df_completo.groupby('nome_participante')['valor_total'].sum()
print(total_por_participante)
print("-" * 50)