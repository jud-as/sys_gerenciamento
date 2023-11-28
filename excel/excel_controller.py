import pandas as pd
from sqlalchemy import create_engine
from database.connection import estabelecer_conexao, desligar_conexao

df_excel = pd.read_excel("gerenciamento_teste.xlsx")


