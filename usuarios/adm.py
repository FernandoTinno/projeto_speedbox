from uuid import uuid4
from .usuario import Usuario


administradores = []

class Administrador(Usuario):
    def __init__(self, nome, email, senha, acesso):
        super().__init__(nome, email, senha)
        self.__adm_id = uuid4
        self.__acesso = acesso

    @property
    def _adm_id(self):
        return self.__adm_id

    @_adm_id.setter
    def _adm_id(self, value):
        self.__adm_id = value

    @property
    def _acesso(self):
        return self.__acesso

    @_acesso.setter
    def _acesso(self, value):
        self.__acesso = value


def inicializar_adm_padrao():
    ceo_speedbox = Administrador('Fernando','fer.ceo@gmail.com','fer_ceo123','primario')
    administradores.append(ceo_speedbox)