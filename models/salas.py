from database.connection import estabelecer_conexao, desligar_conexao

class Salas:
    def __init__(self, nomeSala,):
        self.nomeSala = nomeSala
        
    def inserir_sala(self):
        
        with estabelecer_conexao() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sala (NomeSala) VALUES (%s)", (self.nomeSala,))
            connection.commit()
            cursor = desligar_conexao()
    