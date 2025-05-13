from uuid import uuid4
from datetime import datetime
from abc import ABC
import usuario
import menu
    




if __name__ == "__main__":
    while True:
        opcao = input("\nEscolha uma opção:\n1 - Cadastrar Usuário\n2 - Realizar Login\n3 - Sair\n")

        if opcao == '1':
            usuario.cadastrar_usuario()
            print("Usuários cadastrados (clientes):", usuario.usuarios)
            print("Entregadores cadastrados:", usuario.entregadores)
        elif opcao == '2':
            usuario.realizar_login()
            
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")