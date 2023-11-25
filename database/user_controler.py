
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
        
        
         

