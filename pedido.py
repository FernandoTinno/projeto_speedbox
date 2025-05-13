from uuid import uuid4
from datetime import datetime
from abc import ABC
import produto

class Pedido:
    def __init__(self, valor_total: produto.Produto,status):
        self.__pedido_id = uuid4
        self.__data_pedido = datetime.now()
        self.__valor_total = valor_total
        self.__status = status