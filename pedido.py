from uuid import uuid4
from datetime import datetime
import usuario
import random
import empresa


TEMPOS_DE_ENTREGA = {
    'AC': 10, 'AL': 7, 'AP': 12, 'AM': 15, 'BA': 6, 'CE': 7, 'DF': 5,
    'ES': 4, 'GO': 4, 'MA': 9, 'MT': 5, 'MS': 5, 'MG': 3, 'PA': 10,
    'PB': 8, 'PR': 3, 'PE': 7, 'PI': 9, 'RJ': 2, 'RN': 8, 'RS': 4,
    'RO': 12, 'RR': 14, 'SC': 3, 'SP': 1, 'SE': 6, 'TO': 6
}

class Pedido:
    def __init__(self, cliente):
        self.__pedido_id = uuid4()
        self.__data_pedido = datetime.now()
        self.__cliente = cliente
        self.__itens_pedido = []
        self.__valor_total = 0.0
        self.__status = "pendente"
        self.__metodo_de_entrega = None
        self.__entregador_escolhido = None
        self.__metodo_de_pagamento = None
        self.__tempo_entrega = None

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

    @property
    def _entregador_escolhido(self):
        return self.__entregador_escolhido

    @_entregador_escolhido.setter
    def _entregador_escolhido(self, value):
        self.__entregador_escolhido = value

    @property
    def _metodo_de_pagamento(self):
        return self.__metodo_de_pagamento

    @_metodo_de_pagamento.setter
    def _metodo_de_pagamento(self, value):
        self.__metodo_de_pagamento = value

    @property
    def _tempo_entrega(self):
        return self.__tempo_entrega

    @_tempo_entrega.setter
    def _tempo_entrega(self, value):
        self.__tempo_entrega = value

        
        

        
        
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
            metodo_de_entrega = "moto"
            frete = 15.0
        elif maior_peso >=10 and maior_peso <=20:
            metodo_de_entrega = "carro"
            frete = 30.0
        else:
            metodo_de_entrega = "caminhão"
            frete = 50.0
            
        self._metodo_de_entrega = metodo_de_entrega
        print(f'\ndevido o item mais pesado do seu carrinho de compras ser {maior_peso}KG.\nO veiculo sera: {self._metodo_de_entrega}')
        
        
        entregadores_disponíveis = []
        for entregador in usuario.entregadores:
            if entregador._veiculo == self._metodo_de_entrega:
                entregadores_disponíveis.append(entregador)
        
        
        if entregadores_disponíveis:
            sortear_entregador = random.choice(entregadores_disponíveis)
            self._entregador_escolhido = sortear_entregador
            sortear_entregador._pedidos_pendentes.append(self)
            print(f'o entregador que foi escolhido para realizar a entrega foi: {self._entregador_escolhido._nome}')
        
        
        for item in itens_para_remover:
            self._cliente._carrinho.remove(item)

        self.__valor_total = valor_total_pedido + frete
        #self.__status = "concluído"
        
        print(f'frete: {frete}R$')
        
        estado_cliente = self._cliente._endereco.estado
        estado_empresa = empresa.speedbox._estado.upper()
        
        if estado_cliente == estado_empresa:
            self._tempo_entrega = TEMPOS_DE_ENTREGA['SP']
            print(f"O tempo de entrega estimado para o seu estado é de {self._tempo_entrega} dia(s).")
        elif estado_cliente in TEMPOS_DE_ENTREGA:
            self._tempo_entrega = TEMPOS_DE_ENTREGA[estado_cliente]
            print(f"O tempo de entrega estimado para o seu estado é de {self._tempo_entrega} dia(s).")
        else:
            self._tempo_entrega = 7
            print(f"Não foi possível estimar o tempo de entrega para o seu estado. O tempo estimado é de {self._tempo_entrega} dia(s).")
        
        print(f"\nValor total do pedido: R$ {self._valor_total}")
        while True:
            mtd_pagamento = input('Qual metodo de pagamento você deseja:\n1 - Pix\n2 - Boleto\n3 - Crédito\n4 - Débito:\n')
            if mtd_pagamento == '1':
                self._metodo_de_pagamento = 'Pix'
                break
            elif mtd_pagamento == '2':
                self._metodo_de_pagamento = 'Boleto'
                break
            elif mtd_pagamento == '3':
                self._metodo_de_pagamento = 'Crédito'
                break
            elif mtd_pagamento == '4':
                self._metodo_de_pagamento = 'Débito'
                break
            else:   
                print('A opção para forma de pagamento invalida!') 
        item._quantidade_estoque -= quantidade
        self._cliente._pedidos_feitos.append(self)
        print("Compra finalizada com sucesso!")
        return True

    def __repr__(self):
        return f"Pedido ID: {self._pedido_id},Data da pedido: {self._data_pedido} Cliente: {self._cliente._nome}, Endereço de Entrega: {self._cliente._endereco}, Tempo de Espera: {self._tempo_entrega}, Valor Total: R$ {self._valor_total}, Metodo de Pagamento: {self._metodo_de_pagamento}, Status: {self._status}"
            