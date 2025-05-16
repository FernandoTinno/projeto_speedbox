class Produto:
    def __init__(self,nome,marca,quantidade_estoque:int,preco:float):
        self.__nome = nome
        self.__marca = marca
        self.__quantidade_estoque = quantidade_estoque
        self.__preco = preco

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


    
    
    
        

    


notebook_1 = Produto('aspire ultimate','acer',25,2799.99)
micro_ondas = Produto('hot wave','eletrolux',16,350.00)
cama = Produto('cochão king','gazin',3,1749.99)

        