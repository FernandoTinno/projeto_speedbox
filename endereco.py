class Endereco:
    def __init__(self):
        self.__enderecos_cliente1 = []
        self.__enderecos_cliente2 = []
        self.__enderecos_cliente3 = []

    @property
    def _enderecos_cliente1(self):
        return self.__enderecos_cliente1

    @_enderecos_cliente1.setter
    def _enderecos_cliente1(self, value):
        self.__enderecos_cliente1 = value

    @property
    def _enderecos_cliente2(self):
        return self.__enderecos_cliente2

    @_enderecos_cliente2.setter
    def _enderecos_cliente2(self, value):
        self.__enderecos_cliente2 = value

    @property
    def _enderecos_cliente3(self):
        return self.__enderecos_cliente3

    @_enderecos_cliente3.setter
    def _enderecos_cliente3(self, value):
        self.__enderecos_cliente3 = value
        

    def adicinar_endereco_cliente(self):
        dict_endereco_cliente1 ={}
        dict_endereco_cliente2 ={}
        dict_endereco_cliente3 ={}
        
        if len(self.__enderecos_cliente1) == 0:
            logradouro = input('Digite o locradouro da empresa:')
            numero = input('Digite o numero do endereço da empresa:')
            bairro = input('Digite o bairo da empresa:')
            cidade = input('Digite a cidade da empresa:')
            cep = input('Digite o CEP da empresa:')
            dict_endereco_cliente1 = {'logradouro': logradouro,'numero': numero,'bairro': bairro,'cidade': cidade,'CEP': cep}
            self.__enderecos_cliente1.append(dict_endereco_cliente1)
            return ('endereço adicionado com sucesso')   
        
        
        elif len(self.__enderecos_cliente2) == 0:
            logradouro = input('Digite o locradouro da empresa:')
            numero = input('Digite o numero do endereço da empresa:')
            bairro = input('Digite o bairo da empresa:')
            cidade = input('Digite a cidade da empresa:')
            cep = input('Digite o CEP da empresa:')
            dict_enderecos_cliente2 = {'logradouro': logradouro,'numero': numero,'bairro': bairro,'cidade': cidade,'CEP': cep}
            self.__enderecos_cliente2.append(dict_enderecos_cliente2)
            
            
        elif len(self.__enderecos_cliente3) == 0:
            logradouro = input('Digite o locradouro da empresa:')
            numero = input('Digite o numero do endereço da empresa:')
            bairro = input('Digite o bairo da empresa:')
            cidade = input('Digite a cidade da empresa:')
            cep = input('Digite o CEP da empresa:')
            dict_enderecos_cliente3 = {'logradouro': logradouro,'numero': numero,'bairro': bairro,'cidade': cidade,'CEP': cep}
            self.__enderecos_cliente3.append(dict_enderecos_cliente3)
        else:
            print('Voçê chegou ao numero maximo de endereços cadastrados')
            


    def mostrar(self):
        print(self.__enderecos_cliente1)
        print(self.__enderecos_cliente2)

