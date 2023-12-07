import xlwings as xw
import sys
import os
diretorio_script = os.path.dirname(os.path.abspath(__file__))
diretorio_projeto = os.path.dirname(diretorio_script)
sys.path.append(diretorio_projeto)
from excel_integration import excel_connection
from models.salas import Salas
import time as time
import pandas as pd

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets.active.name
    sheet_gastos = wb.sheets["Gastos"]
    bridge = excel_connection.Bridge('C:/Users/guilh/OneDrive/Área de Trabalho/Serial Experiments/python/sys_gerenciamento/sys_gerenciamento/sys_gerenciamento.xlsm', 'mysql+mysqlconnector://root:''@localhost/sysgerenciamento')
    if(sheet == "Adicionar_Gastos"):
        try:
            df = bridge.exportar_excel_para_sql('gasto')
            time.sleep(1.5)
            df_sql = bridge.exportar_sql_para_excel('gasto')
            try:
                print(df)
                print(df_sql)
                time.sleep(2.5)
                sheet_gastos.range("A2").value = df_sql.values
            except Exception as e:
                print(f'Erro de {e}.')
                time.sleep(5.0)
        except Exception as e:
            print(f'Erro de {e}.')
            time.sleep(5.0)
            
    else:
        print("ERRO: Comando não especificado.")
        time.sleep(1.5)
        
        
if __name__ == "__main__":
    xw.Book("sys_gerenciamento.xlsm").set_mock_caller()
    main()



