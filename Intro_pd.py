import pandas as pd

from IPython.display import display


# Primeiramente devemoss importar a biblioteca pandas

tabela = pd.read_excel("Vendas11.xlsx")

display(tabela)
# import os
# print(os.getcwd())

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

# faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)

#faturamento por produto
faturamento_por_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)

#Para  a retirada de colunas vazias :

# import pandas as pd

# # Carregar a tabela do arquivo Excel
# # Substitua 'arquivo.xlsx' pelo caminho do seu arquivo
# tabela = pd.read_excel("Vendas11.xlsx")

# # Remover colunas que estão completamente vazias
# tabela = tabela.dropna(axis=1, how='all')

# # Salvar o resultado em um novo arquivo Excel
# # Substitua 'arquivo_limpo.xlsx' pelo nome desejado para o novo arquivo
# tabela.to_excel('arquivo_limpo.xlsx', index=False)

# print("Colunas em branco removidas com sucesso!")
