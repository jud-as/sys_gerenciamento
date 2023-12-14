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
    sheet_hist = wb.sheets["Historico"]
    bridge = excel_connection.Bridge('C:/Users/guilh/OneDrive/Área de Trabalho/Serial Experiments/python/sys_gerenciamento/sys_gerenciamento/sys_gerenciamento.xlsm', 'mysql+mysqlconnector://root:''@localhost/sysgerenciamento')
    if(sheet == "Adicionar_Gastos"):
        inserir_gastos(bridge, sheet_gastos, sheet_salas, wb)
        
    elif(sheet == "Gastos"):
        remover_gastos(bridge, sheet_gastos, sheet_salas, sheet_hist, wb)
    else:
        print("ERRO: Comando não especificado.")
        time.sleep(2.5)
        
        

def remover_gastos(bridge, sheet_gastos, sheet_salas, sheet_hist, wb):
    try:
        #COLOCANDO DADOS NA BASE DE DADOS:
        wb.save()
        df = bridge.exportar_excel_para_sql('gasto', 'Gastos')
        if df.empty:
            return
        #FAZENDO A PONTE VIA DATAFRAMES PANDAS:
        df_sql_hist, df_sql = bridge.exportar_sql_para_excel('gasto', 'Gastos')
        print("HIST: ", df_sql_hist)
        print("GASTOS: ", df_sql)
        #ATUALIZANDO DADOS NO EXCEL UTILIZANDO XLWINGS:
        try:
            sheet_hist.range("A2").value = df_sql_hist.values
            sheet_gastos.range("A2:G200").clear_contents()
            time.sleep(0.5)
            sheet_gastos.range("A2").value = df_sql.values
            try:
                salas = Salas()
                salas.valor_total_sala()
                df_sql = bridge.exportar_sql_para_excel('sala', 'Salas')
                #Imprime o valor atualizado na planilha das Salas
                sheet_salas.range("A2").value = df_sql.values
                wb.save()
            except Exception as e:
                print(f'Erro de {e}.')
                time.sleep(2.5)
        except Exception as e:
            print(f'Erro de {e}.')
            time.sleep(5.5)
            
        wb.save()
        
    except Exception as e:
        print(f'Erro de {e}.')
        time.sleep(5.5)

        
def inserir_gastos(bridge, sheet_gastos, sheet_salas, wb):
    try:
        wb.save()
        #Lê a planilha e joga no Banco de Dados
        df = bridge.exportar_excel_para_sql('gasto', 'Adicionar_Gastos')
        time.sleep(0.5)
        if df.empty:
            return
        
        #Joga os dados do sql para planilha Gastos
        df_sql = bridge.exportar_sql_para_excel('gasto', 'Adicionar_Gastos')
        try:
            print(df)
            print(df_sql)
            sheet_gastos.range("A2").value = df_sql.values
            #Atualiza o valor total das salas baseado nos gastos adicionados
            try:
                salas = Salas()
                salas.valor_total_sala()
                df_sql = bridge.exportar_sql_para_excel('sala', 'Salas')
                #Imprime o valor atualizado na planilha das Salas
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



