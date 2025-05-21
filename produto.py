
produtos = []

class Produto:
    def __init__(self,nome,marca,quantidade_estoque:int,preco:float,peso:float):
        self.__nome = nome
        self.__marca = marca
        self.__quantidade_estoque = quantidade_estoque
        self.__preco = preco
        self.__peso = peso
        

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _quantidade_estoque(self):
        return self.__quantidade_estoque

    @_quantidade_estoque.setter
    def _quantidade_estoque(self, value):
        self.__quantidade_estoque = value

    @property
    def _preco(self):
        return self.__preco

    @_preco.setter
    def _preco(self, value):
        self.__preco = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value


    
    def __repr__(self):
        return f"{self._nome}"
    
    
    
def inicializar_produtos_padrao():
    notebook_1 = Produto('notebook aspire','acer',25,2799.99,1.5)
    micro_ondas = Produto('microondas hot wave','eletrolux',16,350.00,10)
    cama = Produto('cochão king','gazin',3,1749.99,30)
    produtos.append(notebook_1)
    produtos.append(micro_ondas)
    produtos.append(cama)       
        

    




        