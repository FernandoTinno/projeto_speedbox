import main
import pedido

def opt_cliente(cliente_logado): 
    while True:
        opcao = input(f"\nOpções do Cliente ({cliente_logado._nome}):\n1 - Adicionar Endereço\n2 - Ver Endereço\n3 - Adicionar produtos ao carrinho\n4 - Sair\n")

        if opcao == '1':
            cliente_logado.adicionar_endereco()#adicionar end
        elif opcao == '2':
            cliente_logado.ver_endereco() #remover end
        elif opcao == '3':
            cliente_logado.escolher_produto()#ver end
        elif opcao == '4':
            cliente_logado.ver_carrinho()#adicionar prod
        elif opcao == '5':
            cliente_logado.escolher_produto()#remover prod
        elif opcao == '6':
            cliente_logado.escolher_produto()#ver prod
        elif opcao == '7':
            novo_pedido = pedido.Pedido(cliente_logado)
            novo_pedido.finalizar_compra()
                
        elif opcao == '8':
            print("Saindo do menu do cliente.")
            return True
        else:
            print("Opção inválida. Tente novamente.")
    
    
    
    


def opt_entregador():
    print('deu certo')


def opt_administrador():
    print('deu certo')        