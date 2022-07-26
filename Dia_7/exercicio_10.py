"""Exercício 10 [22/28]

Enunciado:
    Usando Pandas, procure por um dado específico (da sua escolha)
    e printe somente o mesmo utilizando o CSV.
    
    Dado procurado: Filme referente ao ano de 1985.

Autor:
    Pedro Favoreto Gaya - 02/08/2022
    
Referências:
    Exibir resultado sem coluna de índice:
    https://stackoverflow.com/questions/24644656/how-to-print-pandas-dataframe-without-index
    
    Correção do caminho relativo do arquivo:
    https://stackoverflow.com/questions/918154/relative-paths-in-python
"""

###
# Importar funções auxiliares do diretório acima
# Referência: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os.path
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Auxiliar.helper_formatacao import print_header
###

import pandas as pd

# Função main
def main():
    # Leitura do arquivo CSV
    try:
        # Montagem do caminho absoluto para o arquivo.
        # Permite executar o script a partir de outras pastas, sem que haja erro.
        diretorio = os.path.dirname(__file__)
        arquivo_csv = os.path.join(diretorio, "dados/oscar.csv")
        
        oscar_df = pd.read_csv(arquivo_csv, encoding="UTF-8", sep=",")
    except FileNotFoundError as err:
        print("Erro: Arquivo não encontrado --", err)
        return
    
    # Objetivo: Nome do filme referente ao ano de 1985
    ano = 1985
    filme = oscar_df.loc[
        oscar_df["Year"] == ano,
        "Movie"
    ]
    
    # Saída
    print_header("SAÍDA")
    
    print(f"Filme referente ao ano de {ano}: {filme.to_string(index=False)}")


if __name__ == '__main__':
    main()
    

"""
========================================================================
TEST CASES
========================================================================

TC-01:
------------------------------------------------------------------------
[Entrada]
(vazia)
------------------------------------------------------------------------
[Saída esperada]
Filme referente ao ano de 1985: Amadeus

========================================================================
""" 
