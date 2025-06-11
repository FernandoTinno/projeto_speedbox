from uuid import uuid4
from datetime import datetime
from .usuario import Usuario 
import produto




usuarios = []

class Cliente(Usuario):
    def __init__(self, nome,email,senha,cpf,tel):
        super().__init__(nome,email,senha)
        self.__cliente_id = uuid4
        self.__data_cadastro = datetime.now()
        self.__cpf = cpf
        self.__telefone = tel
        self.__endereco = None
        self.__carrinho = []
        self.__pedidos_feitos = []
        self.__pedidos_avaliados = []

    @property
    def _cliente_id(self):
        return self.__cliente_id

    @_cliente_id.setter
    def _cliente_id(self, value):
        self.__cliente_id = value

    @property
    def _data_cadastro(self):
        return self.__data_cadastro

    @_data_cadastro.setter
    def _data_cadastro(self, value):
        self.__data_cadastro = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco(self):
        return self.__endereco

    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value
        
    @property
    def _carrinho(self):
        return self.__carrinho

    @_carrinho.setter
    def _carrinho(self, value):
        self.__carrinho = value   
        
    @property
    def _pedidos_feitos(self):
        return self.__pedidos_feitos

    @_pedidos_feitos.setter
    def _pedidos_feitos(self, value):
        self.__pedidos_feitos = value     
                
    @property
    def _pedidos_avaliados(self):
        return self.__pedidos_avaliados

    @_pedidos_avaliados.setter
    def _pedidos_avaliados(self, value):
        self.__pedidos_avaliados = value

    def __repr__(self):
        return super().__repr__()
           
    def escolher_produto(self):
        num = 0
        for item in produto.produtos:
            num +=1
            print(f'{num} - {item._nome} Preço: {item._preco}\n')
            
        escolha = int(input('digite o numero do produto que vc gostaria de adicionar: '))
        
        if escolha == 0:
            print('opcao invalida')
        elif escolha > len(produto.produtos):
            print('opcao invalida')
        else:
            escolha_index = escolha - 1
            if produto.produtos[escolha_index]._quantidade_estoque == 0:
                print('\nProduto fora de estoque!')
                return False
            else:
                self._carrinho.append(produto.produtos[escolha_index])
                print(f'\n{produto.produtos[escolha_index]} foi adicionado ao seu carrinho de compras')
             
    def remover_produto(self):
        if self._carrinho:
            carrinho_novo = []
            itens_removidos = [] 

            for item in self._carrinho:
                print(item._nome)
                remover_item = input('Você gostaria de remover esse item?(digite 1 para sim e 2 para não): ')
                if remover_item == '1':
                    print(f'Ok, o item {item._nome} foi removido com sucesso\n')
                    itens_removidos.append(item._nome)
                    
                elif remover_item == '2':
                    print(f'Tudo bem, esse item será mantido no seu carrinho\n')
                    carrinho_novo.append(item)
                else:
                    print('A opção que você selecionou está incorreta')
                    carrinho_novo.append(item) 

            self._carrinho = carrinho_novo  
        else:
            print('Você ainda não adicionou um produto ao carrinho')
            
    def ver_carrinho(self):
        if self._carrinho:
            print(f'Aqui está seu carrinho de compras: {self._carrinho}')
        else:
            print("Você ainda não adicionou nenhum produto ao carrinho.")
            
    def historico_pedidos(self):
        if self._pedidos_feitos or self._pedidos_avaliados:
                print("\nSeu Histórico de Pedidos:")
                for pedidos in self._pedidos_feitos:
                    print(pedidos)
                for pedidos_avaliados in self._pedidos_avaliados:
                    print(pedidos_avaliados)
        else:
            print("Você ainda não realizou nenhum pedido.")
            return False
        
    def avaliar_pedido(self):
        pedidos_para_avaliar = []
        for pedido in self._pedidos_feitos:
            if pedido._status == 'concluido':
                pedidos_para_avaliar.append(pedido)
            else:
                pass
        for pedido_filtrado in pedidos_para_avaliar:
            if pedido_filtrado._avaliacao != 'pendente':
                pedidos_para_avaliar.remove(pedido_filtrado)
            else:
                pass
        
        if pedidos_para_avaliar:
            for pedido_a_avaliar in pedidos_para_avaliar:
                while True:
                    avaliar = input(f'em relação ao pedido {pedido_a_avaliar._pedido_id}\n Digite sua nota de 1 a 5 em relação ao pedido, desde a espera até o produto em si: ')
                    if avaliar in ['1','2']:
                        print(f'Sinto muito pela má experiencia que você teve {self._nome}. Agradeçemos ao seu feedback e iremos melhorar, desde já agradeço!')
                        break
                    elif avaliar in ['3','4']:
                        print(f'Ficamos contende que sua experiencia tenha sido agradavel {self._nome}. Agradeçemos ao seu feedback e iremos melhorar, para que possamos ser nota máxima!')
                        break
                    elif avaliar in ['5']:
                        print(f'Estamos cem porcento contente com sua avaliação {self._nome}. Atraves dela, conseguimos perceber que estamos fazendo um otimo serviço, muito obrigado!')
                        break
                    else:
                        print(f'A nota que você atribuiu ao pedido está incorreta')
                        
                while True:
                        avaliar_entregador = input(f'em relação ao entregador {pedido_a_avaliar._entregador_escolhido._nome}\n Digite sua nota de 1 a 5 em relação ao entregador, desde a valocidade de entrega, as condições em que o produto foi entregue e abordagem do entregador: ')
                        
                        if avaliar_entregador in ['1','2']:
                            print(f'Sinto muito pela má experiencia que você teve {self._nome}. Agradeçemos ao seu feedback e iremos reportar ao nosso entregador, desde já agradeço!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        elif avaliar_entregador in ['3','4']:
                            print(f'Ficamos contende que sua experiencia tenha sido agradavel {self._nome}. Agradeçemos ao seu feedback e iremos repassar para nosso entregador, para que ele se torne nota máxima!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        elif avaliar_entregador in ['5']:
                            print(f'Estamos cem porcento contente com sua avaliação {self._nome}. Atraves dela, conseguimos perceber que nosso entregador esta fazendo um otimo serviço, muito obrigado!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        else:
                            print(f'A nota que você atribuiu ao pedido está incorreta')                        
        else:
            print('Você não possui nenhum Pedido como concluido para poder Avaliar')