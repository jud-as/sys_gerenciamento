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
    sheet_salas = wb.sheets["Salas"]
    bridge = excel_connection.Bridge('C:/Users/guilh/OneDrive/Área de Trabalho/Serial Experiments/python/sys_gerenciamento/sys_gerenciamento/sys_gerenciamento.xlsm', 'mysql+mysqlconnector://root:''@localhost/sysgerenciamento')
    if(sheet == "Adicionar_Gastos"):
        inserir_gastos(bridge, sheet_gastos, sheet_salas, wb)
        
    elif(sheet == "Gastos"):
        remover_gastos(bridge, sheet_gastos, sheet_salas, wb)
    else:
        print("ERRO: Comando não especificado.")
        time.sleep(2.5)
        
        

def remover_gastos(bridge, sheet_gastos, sheet_salas, wb):
    try:
        wb.save()
        df = bridge.exportar_excel_para_sql('gasto', 'Gastos')
        time.sleep(0.5)
        if df.empty:
            return
        
        df_sql = bridge.exportar_sql_para_excel('gasto', 'Gastos')
        print(df_sql)
        time.sleep(5.0)
    except Exception as e:
        print(f'Erro de {e}.')
        time.sleep(2.5)

        
    
    
    
    
       
        
def inserir_gastos(bridge, sheet_gastos, sheet_salas, wb):
    try:
        wb.save()
        df = bridge.exportar_excel_para_sql('gasto', 'Adicionar_Gastos')
        time.sleep(0.5)
        if df.empty:
            return
        
        df_sql = bridge.exportar_sql_para_excel('gasto', 'Adicionar_Gastos')
        try:
            print(df)
            print(df_sql)
            sheet_gastos.range("A2").value = df_sql.values
            try:
                salas = Salas()
                salas.valor_total_sala()
                df_sql = bridge.exportar_sql_para_excel('sala', 'Salas')
                sheet_salas.range("A2").value = df_sql.values
                wb.save()
            except Exception as e:
                print(f'Erro de {e}.')
                time.sleep(2.5)
        except Exception as e:
            print(f'Erro de {e}.')
            time.sleep(2.5)
    except Exception as e:
        print(f'Erro de {e}.')
        time.sleep(2.5)
        

        

if __name__ == "__main__":
    xw.Book("sys_gerenciamento.xlsm").set_mock_caller()
    main()



