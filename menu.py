import main

def opt_cliente(cliente_logado): # Recebe o objeto cliente logado como argumento
    while True:
        opcao = input(f"\nOpções do Cliente ({cliente_logado._nome}):\n1 - Adicionar Endereço\n2 - Ver Endereço\n3 - Outra Funcionalidade (a implementar)\n4 - Sair\n")

        if opcao == '1':
            cliente_logado.adicionar_endereco()
        elif opcao == '2':
            cliente_logado.ver_endereco()
        elif opcao == '3':
            print("Outra funcionalidade será implementada aqui.")
        elif opcao == '4':
            print("Saindo do menu do cliente.")
            return True
        else:
            print("Opção inválida. Tente novamente.")
    
    
    
    


def opt_entregador():
    print('deu certo')


def opt_administrador():
    print('deu certo')        