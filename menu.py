import endereco
from pedido import Pedido
import produto
import cupom

def opt_cliente(cliente_logado): 
    while True:
        opcao = input(f"\nOpções do Cliente ({cliente_logado._nome}):\n1 - Adicionar Endereço\n2 - Remover Endereço\n3 - Ver Endereço\n4 - Adicionar Produto\n5 - Remover Produto\n6 - Ver Produto\n7 - Finalizar Compra\n8 - Historico de pedidos\n9 - Avaliar Pedido\n10 - Sair\n")
        
        if opcao == '1':
            endereco.Endereco.adicionar_endereco(cliente_logado)
        elif opcao == '2':
            endereco.Endereco.remover_endereco(cliente_logado) 
        elif opcao == '3':
            endereco.Endereco.ver_endereco(cliente_logado)
        elif opcao == '4':
            cliente_logado.escolher_produto()
        elif opcao == '5':
            cliente_logado.remover_produto()
        elif opcao == '6':
            cliente_logado.ver_carrinho()
        elif opcao == '7':
            novo_pedido = Pedido(cliente_logado)
            novo_pedido.finalizar_compra()
        elif opcao == '8':
            cliente_logado.historico_pedidos()
        elif opcao == '9':
            cliente_logado.avaliar_pedido()         
        elif opcao == '10':
            print("Saindo do menu do cliente.")
            return False
        else:
            print("Opção inválida. Tente novamente.")
    
    
def opt_entregador(entregador_logado):
    while True:
        opcao = input(f"\nOpções do Entregador ({entregador_logado._nome}):\n1 - Concluir pedidos\n2 - Ver Histórico de Pedidos\n3 - Ver Notas\n4 - sair\n")

        if opcao == '1':
            entregador_logado.concluir_pedido()
            
        elif opcao == '2': 
            entregador_logado.historico_entregas()
            
        elif opcao == '3': 
            entregador_logado.ver_nota()    
        
        elif opcao == '4': 
            print("Saindo do menu do entregador.")
            return False
        else:
            print("Opção inválida. Tente novamente.")


def opt_administrador_primario(adm_logado):
    while True:
        opcao = input(f"\nOpções do Administrador {adm_logado._nome}:\n1 - Adicionar Produto\n2 - Remover Produto\n3 - Listar Produtos\n4 - Repor estoque\n5 - Aplicar cupom\n6 - Aprovar contas de administradores\n7 - Promover nivel de acesso dos administradores\n8 - Rebaixar nivel de acesso dos administradores\n9 - Sair\n") 
        
        
        if opcao == '1':
             produto.adicionar_produto()
        elif opcao == '2':
            produto.remover_produto()
        elif opcao == '3':
            produto.listar_produtos()
        elif opcao == '4':
            produto.repor_estoque_produto()
        elif opcao == '5':
            cupom.cadastrar_cupom()
        elif opcao == '6':
            adm_logado.aprovar_contas()
        elif opcao == '7':
            adm_logado.promover_contas_administrador()
        elif opcao == '8':
            adm_logado.rebaixar_contas_administrador()
        elif opcao == '9':
            print("Saindo do menu do administrador primario.")
            return False
        else:
             print("Opção inválida. Tente novamente.")


def opt_administrador_secundario(adm_logado):
    while True:
        opcao = input(f"\nOpções do Administrador {adm_logado._nome}:\n1 - Adicionar Produto\n2 - Remover Produto\n3 - Listar Produtos\n4 - Repor estoque\n5 - Sair\n")
        
        if opcao == '1':
            produto.adicionar_produto()
        elif opcao == '2':
            produto.remover_produto()
        elif opcao == '3':
            produto.listar_produtos()
        elif opcao == '4':
            produto.repor_estoque_produto()
        elif opcao == '5':
            print("Saindo do menu do administrador secundario.")
            return False
        else:
            print("Opção inválida. Tente novamente.")
       