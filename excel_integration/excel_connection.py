
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
    
    def exportar_sql_para_excel(self, tabela, sheet):
        engine = create_engine(self.string_de_conexao)
        consulta_sql = f'SELECT * FROM {tabela}'
        df_sql = pd.read_sql(consulta_sql, con=engine)
        
        while True:
            print(df_sql)
            try:
                with pd.ExcelWriter(
                    path=self.excel_path,
                    mode='a',
                    if_sheet_exists='overlay',
                    date_format="YYYY-MM-DD"
                    ) as writer:
                    df_sql.to_excel(excel_writer=writer, sheet_name=f'{sheet}', header=True, index=False)
                break
            except Exception as e:
                print(f"NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA: {e}")
                break
            
        engine.dispose()

    def exportar_excel_para_sql(self, tabela):
        engine = create_engine(self.string_de_conexao)
        df_excel = pd.read_excel(self.excel_path, sheet_name='Adicionar_Gastos', header=0) #Ler dados de um Excel para um dataframe do Pandas
        
        print(df_excel)
        try:
            df_excel.to_sql(tabela, con=engine, if_exists='append', index=False)
            return df_excel
        except Exception as e:
            print(f"NÃO FOI POSSÍVEL ALOCAR OS DADOS NA TABELA: {e}")
           
        engine.dispose()                     





