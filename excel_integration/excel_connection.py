
import pandas as pd
from sqlalchemy import create_engine
import sys
import os
diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_projeto = os.path.dirname(diretorio_script)
sys.path.append(diretorio_projeto)

from database.connection import estabelecer_conexao

class Bridge:
    def __init__(self, excel_path, string_de_conexao):
        self.excel_path = excel_path
        self.string_de_conexao = string_de_conexao
    
    def exportar_sql_para_excel(self, tabela):
        engine = create_engine(self.string_de_conexao)
        consulta_sql = f'SELECT * FROM {tabela}'
        df_sql = pd.read_sql(consulta_sql, con=engine)
        df_sql.to_excel(self.excel_path, sheet_name='Gastos', index=False)
        engine.dispose()

    def exportar_excel_para_sql(self, tabela):
        opc = 0
        engine = create_engine(self.string_de_conexao)
        df_excel = pd.read_excel(self.excel_path, sheet_name='Adicionar_Gastos') #Ler dados de um Excel para um dataframe do Pandas
        while True:
            print(df_excel)
            opc = int(input("\nDESEJA INSERIR ESSES DADOS?\n1 - Sim\n2 - Não"))
            if opc == 1:
                try:
                    df_excel.to_sql(tabela, con=engine, if_exists='append', index=False)
                    break
                except:
                    print("NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA.")
                    break
            else:
                break      
        engine.dispose()                     





