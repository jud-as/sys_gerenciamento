from database.connection import estabelecer_conexao, desligar_conexao
from datetime import datetime
class Gastos:
    def __init__(self, id_sala, data_vencimento, valor, categoria, descricao):
        self.id_sala = id_sala    
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
    
    def inserir_gasto(self):

        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            query = "INSERT INTO gasto (ID_Sala, DataVencimento, Valor, Categoria, Descricao) VALUES (%s, %s, %s, %s, %s)"
            values = (self.id_sala, self.data_vencimento, self.valor, self.categoria, self.descricao)
            cursor.execute(query, values)
            connection.commit()
            
    
    def solicitar_infos_gasto(self):
        info_gasto = {}  # Cria um dicionário para armazenar as informações
        info_gasto['id_sala'] = input("ID SALA ATRIBUÍDA: ")
        data_str = input("DATA DE VENCIMENTO (formato YYYY-MM-DD): ")
        try:
            info_gasto['data_vencimento'] = datetime.strptime(data_str, "%Y-%m-%d")
        except ValueError:
            print("FORMATO DE DATA INVÁLIDO. USE O FORMADO YYYY-MM-DD.")
            return None
        
        info_gasto['valor'] = float(input("VALOR: "))
        info_gasto['categoria'] = input("CATEGORIA: ")
        info_gasto['descricao'] = input("DESCRIÇÃO: ")

        return info_gasto