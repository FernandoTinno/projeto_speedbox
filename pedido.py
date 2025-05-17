from uuid import uuid4
from datetime import datetime
from abc import ABC
import produto

class Pedido:
    def __init__(self, cliente):
        self.__pedido_id = uuid4()
        self.__data_pedido = datetime.now()
        self.__cliente = cliente
        self.__itens_pedido = []
        self.__valor_total = 0.0
        self.__status = "pendente"
        self.__metodo_de_entrega = None

    @property
    def _pedido_id(self):
        return self.__pedido_id

    @_pedido_id.setter
    def _pedido_id(self, value):
        self.__pedido_id = value

    @property
    def _data_pedido(self):
        return self.__data_pedido

    @_data_pedido.setter
    def _data_pedido(self, value):
        self.__data_pedido = value

    @property
    def _cliente(self):
        return self.__cliente

    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value

    @property
    def _itens_pedido(self):
        return self.__itens_pedido

    @_itens_pedido.setter
    def _itens_pedido(self, value):
        self.__itens_pedido = value

    @property
    def _valor_total(self):
        return self.__valor_total

    @_valor_total.setter
    def _valor_total(self, value):
        self.__valor_total = value

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _metodo_de_entrega(self):
        return self.__metodo_de_entrega

    @_metodo_de_entrega.setter
    def _metodo_de_entrega(self, value):
        self.__metodo_de_entrega = value


    

        
        
    def finalizar_compra(self):
        
        if not self._cliente._endereco:
            print('Para dar continuidade ao pedido é nescessario possuir um endereço.')
            return False
        if not self._cliente._carrinho:
            print("Seu carrinho está vazio. Adicione produtos para finalizar a compra.")
            return False

        print("Itens no seu carrinho:")
        valor_total_pedido = 0.0
        itens_para_remover = []

        for item in self._cliente._carrinho:
            quantidade = self._cliente._carrinho.count(item)
            if quantidade > item._quantidade_estoque:
                print(f"Estoque insuficiente para o produto: {item._nome}. Disponível: {item._quantidade_estoque}, Você selecionou: {quantidade}.")
                return False
            elif item not in self._itens_pedido:
                self._itens_pedido.append(item)
                valor_total_pedido += item._preco * quantidade
                print(f"- {item._nome} (x{quantidade}): R$ {item._preco} (Subtotal: R$ {item._preco * quantidade:})")
                
                for _ in range(quantidade):
                    itens_para_remover.append(item)

        maior_peso = 0
        for item in self._cliente._carrinho:
            if item._peso > maior_peso:
                maior_peso = item._peso
        if maior_peso < 10:
            metodo_de_entrega = 'Moto'
        elif maior_peso >= 10 and maior_peso <= 20:
            metodo_de_entrega = 'Carro'
        else:
            metodo_de_entrega = 'Caminhão'
            
        self._metodo_de_entrega = metodo_de_entrega
        print(f'devido o item mais pesado do seu carrinho de compras ser {maior_peso}KG.\nO veiculo sera: {self._metodo_de_entrega}')
        for item in itens_para_remover:
            self._cliente._carrinho.remove(item)

        self.__valor_total = valor_total_pedido
        self.__status = "concluído"
        print(f"\nValor total do pedido: R$ {self._valor_total:.2f}")
        print("Compra finalizada com sucesso!")
        return True

    def __repr__(self):
        return f"Pedido ID: {self._pedido_id}, Cliente: {self._cliente._nome}, Valor Total: R$ {self._valor_total:.2f}, Status: {self._status}"
            