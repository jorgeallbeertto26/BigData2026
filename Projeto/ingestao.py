import pandas as pd
from sqlalchemy import create_engine

# 1. Configurar a conexão com a AWS (Senha do último container: AdminBigData2026)
ip_aws = '18.117.108.116' 
engine = create_engine(f'mysql+pymysql://root:AdminBigData2026@{ip_aws}:3306/bigdata_db')

# 2. Mapear os arquivos CSV para os nomes das tabelas no MySQL
arquivos_para_tabelas = {
    'Plant_1_Generation_Data.csv': 'plant_1_generation',
    'Plant_1_Weather_Sensor_Data.csv': 'plant_1_weather',
    'Plant_2_Generation_Data.csv': 'plant_2_generation',
    'Plant_2_Weather_Sensor_Data.csv': 'plant_2_weather'
}

# 3. Processar e enviar os arquivos
for arquivo, tabela in arquivos_para_tabelas.items():
    print(f"Carregando {arquivo}...")
    df = pd.read_csv(arquivo)
    
    # Opcional: Converter colunas de data/hora para o formato datetime do MySQL
    if 'DATE_TIME' in df.columns:
        df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
        
    print(f"Enviando dados para a tabela '{tabela}' na AWS...")
    
    # if_exists='replace' cria a tabela automaticamente se ela não existir
    df.to_sql(name=tabela, con=engine, if_exists='replace', index=False)
    print(f"Sucesso! Tabela '{tabela}' finalizada.\n")

print("Ingestão de dados concluída para todos os arquivos!")