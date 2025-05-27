import pedido

class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, estado):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def _logradouro(self):
        return self.__logradouro

    @_logradouro.setter
    def _logradouro(self, value):
        self.__logradouro = value

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _bairro(self):
        return self.__bairro

    @_bairro.setter
    def _bairro(self, value):
        self.__bairro = value

    @property
    def _cidade(self):
        return self.__cidade

    @_cidade.setter
    def _cidade(self, value):
        self.__cidade = value

    @property
    def _estado(self):
        return self.__estado

    @_estado.setter
    def _estado(self, value):
        self.__estado = value


    def __repr__(self):
        return f"{self._logradouro}, {self._numero}, {self._bairro}, {self.__cidade}, {self._estado}"
    
    def adicionar_endereco(usuario):
        if not usuario._endereco:
            
            print("Vamos cadastrar o seu endereço:")
            logradouro = input('Digite o logradouro: ')
            numero = input('Digite o número: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite a cidade: ')
            
            while True:
                estado = input('Digite a sigla do seu estado (Ex: SP): ').upper()
                if estado in pedido.TEMPOS_DE_ENTREGA: 
                    break
                else:
                    print("Sigla de estado inválida. Por favor, digite uma sigla válida (Ex: SP, RJ, MG).")
            endereco_usuario = Endereco(logradouro, numero, bairro, cidade, estado)
            usuario._endereco = endereco_usuario
            print("Endereço adicionado com sucesso!")
        else:
            print('Você já tem um endereço cadastrado')
            
    
    def remover_endereco(usuario):
        if usuario._endereco:
            
            while True:
                confirmar = input('Você tem certeza que deseja remover o endereço (digite 1 para sim e 2 para não): ')
                if confirmar == '1':
                    usuario._endereco = None
                    break
                elif confirmar == '2':
                    print('Remoção de endereço cancelada')
                    break
                else:
                    print('A opção que você digitou está incorreta')            
        else:
            print('Você não possui nenhum endereço') 
    
    
    def ver_endereco(usuario):
        if usuario._endereco:
            print("Seu endereço:", usuario._endereco)
        else:
            print("Você ainda não cadastrou um endereço.")