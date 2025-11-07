import pandas as pd

# O nome do arquivo Excel que você acabou de criar
arquivo_excel = 'dados.xlsx'

try:
    # Tenta ler o arquivo
    df = pd.read_excel(arquivo_excel)

    # Imprime os dados na tela
    print("Dados lidos do Excel com sucesso:")
    display(df)

except FileNotFoundError:
    print(f"ERRO: O arquivo '{arquivo_excel}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
