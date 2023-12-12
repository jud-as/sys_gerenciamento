
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import sys
import os
from database.user_controler import UserController
diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_projeto = os.path.dirname(diretorio_script)
sys.path.append(diretorio_projeto)

from database.connection import estabelecer_conexao

class Bridge:
    def __init__(self, excel_path, string_de_conexao):
        self.excel_path = excel_path
        self.string_de_conexao = string_de_conexao
    
    def exportar_sql_para_excel(self, tabela, sheet):
        engine = create_engine(self.string_de_conexao)
        if(tabela == 'gasto'):
            consulta_sql = f'SELECT * FROM {tabela} WHERE Pendente = 1'
            consulta_historico = f'SELECT * FROM {tabela} WHERE Pendente = 0'
        else:
            consulta_sql = f'SELECT * FROM {tabela}'
        try:
            if(sheet == 'Gastos'):
                df_sql_hist = pd.read_sql(consulta_historico, con=engine)
                pdsql_df_hist = pd.DataFrame(df_sql_hist)
                df_sql = pd.read_sql(consulta_sql, con=engine)
                pdsql_df = pd.DataFrame(df_sql)
                return pdsql_df_hist, pdsql_df
            else:
                df_sql = pd.read_sql(consulta_sql, con=engine)
                pdsql_df = pd.DataFrame(df_sql)
                return pdsql_df
            
        except Exception as e:
            print(f"NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA: {e}")
            
        engine.dispose() 

    def exportar_excel_para_sql(self, tabela, sheet):
        engine = create_engine(self.string_de_conexao)
        df_excel = pd.read_excel(self.excel_path, sheet_name=f'{sheet}', header=0) #Ler dados de um Excel para um dataframe do Pandas
        if(sheet == 'Gastos'):
            print(df_excel)
            try:
                con = UserController()
                con.recriar_tabela_gastos()
                df_excel.to_sql(tabela, con=engine, if_exists='append', index=False)
                pd_df = pd.DataFrame(df_excel)
            except Exception as e:
                print(f"NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA: {e}")
        else:
            try:
                df_excel.to_sql(tabela, con=engine, if_exists='append', index=False)
                pd_df = pd.DataFrame(df_excel)
                return pd_df
            except Exception as e:
                print(f"NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA: {e}")
           
        engine.dispose()            



