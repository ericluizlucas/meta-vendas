import pandas as pd

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela = pd.read_excel(f"{mes}.xlsx")
    if (tabela["Vendas"] > 55000).any():
        vendedor = tabela.loc[tabela["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela.loc[tabela["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {mes} o vendedor {vendedor} bateu a meta, com {vendas} reais em vendas.")