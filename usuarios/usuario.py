class Usuario:
    def __init__(self,nome,email,senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        
    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _senha(self):
        return self.__senha

    @_senha.setter
    def _senha(self, value):
        self.__senha = value
    
    def __repr__(self):
        return f"{self._nome},{self._email}"