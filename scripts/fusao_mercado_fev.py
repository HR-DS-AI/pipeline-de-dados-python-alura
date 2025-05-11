from processamento_dados import Dados

# Caminhos para os arquivos de dados brutos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Instancia os dados da Empresa A (formato JSON)
dados_empresaA = Dados(path_json, 'json')

# Exibe informações básicas
print(dados_empresaA.nome_colunas)  # Colunas presentes no JSON
print(dados_empresaA.qtd_linhas)    # Número de registros

# Instancia os dados da Empresa B (formato CSV)
dados_empresaB = Dados(path_csv, 'csv')

# Exibe informações básicas
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

# Mapeamento para padronizar os nomes das colunas entre os dois arquivos
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# Renomeia colunas do CSV com base no mapeamento
dados_empresaB.rename_columns(key_mapping)

# Junta os dois conjuntos de dados
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

# Exibe resultado final
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# Salva os dados combinados em um CSV final
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Dados combinados salvos em: {path_dados_combinados}')
