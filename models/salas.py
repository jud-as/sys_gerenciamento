from database.connection import estabelecer_conexao, desligar_conexao

class Salas:
    def __init__(self, nomeSala=None,):
        self.nomeSala = nomeSala
        
    def inserir_sala(self):
        
        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sala (NomeSala) VALUES (%s)", (self.nomeSala,))
            connection.commit()
        cursor = desligar_conexao()
            
            
    def valor_total_sala(self):
        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE sala SET ValorTotalGastos = (SELECT SUM(Valor) FROM gasto WHERE gasto.ID_Sala = sala.ID_Sala and gasto.Pendente = 1)")
            connection.commit()
        cursor = desligar_conexao()
        
