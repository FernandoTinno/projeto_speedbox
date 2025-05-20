class Empresa:
    
    def __init__(self,nome,cnpj,telefone,logradouro,numero,bairo,cidade,estado):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairo = bairo
        self.__cidade = cidade
        self.__estado = estado

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _cnpj(self):
        return self.__cnpj

    @_cnpj.setter
    def _cnpj(self, value):
        self.__cnpj = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

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
    def _bairo(self):
        return self.__bairo

    @_bairo.setter
    def _bairo(self, value):
        self.__bairo = value

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


speedbox = Empresa('Speedbox','12.345.678/9012-34','(18)997679126','Avenida brasil','33','zona sul','Ilha solteira','SP')
