import mysql.connector
 
def estabelecer_conexao():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sysgerenciamento'
    )
    return conexao
    
    
with estabelecer_conexao() as conexao:
    cursor = conexao.cursor()
    
    
def desligar_conexao():
    cursor.close()
    conexao.close()