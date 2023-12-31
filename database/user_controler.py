
from database.connection import estabelecer_conexao, desligar_conexao
from models.gastos import Gastos
from models.salas import Salas

class UserController:
    def createSala(self, nomeSala):
        #Instancia um objeto Sala com o parametro fornecido pelo usuário:
        nova_sala = Salas(nomeSala) 
        #Chama o método para inserir a sala instanciada no Banco de Dados
        nova_sala.inserir_sala()
            
    def createGasto(self, novo_gasto):
        novo_gasto.inserir_gasto()
        
    def atualizar_valor_sala(self):
        sala = Salas(None)
        sala.valor_total_sala()

    def recriar_tabela_gastos(self):
        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            cursor.execute("TRUNCATE gasto")
            connection.commit()
        cursor = desligar_conexao()
        
         

