from classes import SwitchCase
from database.user_controler import UserController
from models.gastos import Gastos


def case1():
    nome_sala = input("Digite a identificação da sala: ")
    user_controller = UserController()
    user_controller.createSala(nome_sala)
    
def case2():
    user_controller = UserController()
    info_gasto = Gastos(id_sala=input("SALA REFERENTE AO GASTO: "),
                        data_vencimento=input("DATA DE VENCIMENTO: "),
                        valor=input("VALOR: "),
                        categoria=input("CATEGORIA: "),
                        descricao=input("DESCRIÇÃO: "))
    user_controller.createGasto(info_gasto)
    user_controller.atualizar_valor_sala()
    
def case3():
    print("listar registros")

switcher = SwitchCase()
switcher.add_case(1, case1)
switcher.add_case(2, case2)
switcher.add_case(3, case3)

opcoes_validas = [1, 2, 3]

print("1 - Adicionar sala.\n2 - Adicionar Gasto.\n3 - Listar Registros.")

while True:
    try:
        user_choice = int(input("\nEscolha uma opção: "))
        if user_choice in opcoes_validas:
            switcher.execute(user_choice)
            break
        else:
            print("ERRO: Insira uma opção válida.")
    except ValueError:
        print("ERRO: Insira um tipo válido.")