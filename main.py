from uuid import uuid4
from datetime import datetime
from abc import ABC
import usuario
import menu
import endereco
    




if __name__ == "__main__":
    while True:
        opcao = input("\nEscolha uma opção:\n1 - Cadastrar Usuário\n2 - Realizar Login\n3 - Sair\n")

        if opcao == '1':
            usuario.cadastrar_usuario()
            print("Usuários cadastrados (clientes):", usuario.usuarios)
            print("Entregadores cadastrados:", usuario.entregadores)
        elif opcao == '2':
            cliente_entregador_logado = usuario.realizar_login()
            if cliente_entregador_logado:
                if isinstance(cliente_entregador_logado, usuario.Cliente):
                    print(f"\nBem-vindo, {cliente_entregador_logado._nome}")
                    menu.opt_cliente(cliente_entregador_logado)
                elif isinstance(cliente_entregador_logado, usuario.Entregador):
                    print(f"\nBem-vindo, {cliente_entregador_logado._nome}")
                    menu.opt_entregador(cliente_entregador_logado)
            
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")