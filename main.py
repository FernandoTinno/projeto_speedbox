import usuario
import produto



if __name__ == "__main__":
    usuario.inicializar_entregadores_padrao()
    produto.inicializar_produtos_padrao()
    while True:
        opcao = input("\nEscolha uma opção:\n1 - Cadastrar Usuário\n2 - Realizar Login\n3 - Sair\n")

        if opcao == '1':
            usuario.cadastrar_usuario()
        elif opcao == '2':
            usuario.realizar_login()   
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")  