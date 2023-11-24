
from connection import estabelecer_conexao, desligar_conexao
from models.gastos import Gastos
from models.salas import Salas

class UserController:
    def createSala(self, nomeSala):
        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sala (NomeSala) VALUES (%s)", (nomeSala))
            connection.commit()

