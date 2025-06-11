# main.py

from usuarios import gerenciador_usuarios
from usuarios import entregador 
from usuarios import adm 
import produto


if __name__ == "__main__":
    entregador.inicializar_entregadores_padrao()
    produto.inicializar_produtos_padrao()
    adm.inicializar_adm_padrao()
    
    while True:
        opcao = input("\nEscolha uma opção:\n1 - Cadastrar Usuário\n2 - Realizar Login\n3 - Sair\n")

        if opcao == '1':
            gerenciador_usuarios.cadastrar_usuario()
        elif opcao == '2':
            gerenciador_usuarios.realizar_login()   
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")