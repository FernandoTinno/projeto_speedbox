
import pedido

def opt_cliente(cliente_logado): 
    while True:
        opcao = input(f"\nOpções do Cliente ({cliente_logado._nome}):\n1 - Adicionar Endereço\n2 - Remover Endereço\n3 - Ver Endereço\n4 - Adicionar Produto\n5 - Remover Produto\n6 - Ver Produto\n7 - Finalizar Compra\n8 - Sair\n")

        if opcao == '1':
            cliente_logado.adicionar_endereco()
        elif opcao == '2':
            cliente_logado.remover_endereco() 
        elif opcao == '3':
            cliente_logado.ver_endereco()
        elif opcao == '4':
            cliente_logado.escolher_produto()
        elif opcao == '5':
            cliente_logado.remover_produto()
        elif opcao == '6':
            cliente_logado.ver_carrinho()
        elif opcao == '7':
            novo_pedido = pedido.Pedido(cliente_logado)
            novo_pedido.finalizar_compra()
                
        elif opcao == '8':
            print("Saindo do menu do cliente.")
            return False
        else:
            print("Opção inválida. Tente novamente.")
    
    
    
    


def opt_entregador(entregador_logado):
    while True:
        opcao = input(f"\nOpções do Entregador ({entregador_logado._nome}):\n1 - Ver Histórico de Pedidos\n2 - Sair\n")

        if opcao == '1':
            entregador_logado.historico_entregas()
        elif opcao == '2':
            print("Saindo do menu do entregador.")
            return False
        else:
            print("Opção inválida. Tente novamente.")


def opt_administrador(adm_logado):
    pass #mais para frente, pretendo colocar opcoes para o administrador, como por exemplo, adicionar ou remover produtos e afins
       