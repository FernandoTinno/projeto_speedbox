from uuid import uuid4
from datetime import datetime
from abc import ABC
import endereco
import menu

usuarios = []
entregadores = []



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


class Administrador:
    def __init__(self):
        self.__nome_usuario = 'admin'
        self.__senha_usuario = 'admin123'

    @property
    def _nome_usuario(self):
        return self.__nome_usuario

    @_nome_usuario.setter
    def _nome_usuario(self, value):
        self.__nome_usuario = value

    @property
    def _senha_usuario(self):
        return self.__senha_usuario

    @_senha_usuario.setter
    def _senha_usuario(self, value):
        self.__senha_usuario = value


class Cliente(Usuario):
    def __init__(self, nome,email,senha,cpf,tel):
        super().__init__(nome,email,senha)
        self.__cliente_id = uuid4
        self.__data_cadastro = datetime.now()
        self.__cpf = cpf
        self.__telefone = tel
        self.__endereco = None


    @property
    def _cliente_id(self):
        return self.__cliente_id

    @_cliente_id.setter
    def _cliente_id(self, value):
        self.__cliente_id = value

    @property
    def _data_cadastro(self):
        return self.__data_cadastro

    @_data_cadastro.setter
    def _data_cadastro(self, value):
        self.__data_cadastro = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco(self):
        return self.__endereco

    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value


    def __repr__(self):
        return super().__repr__()
    
    
    def adicionar_endereco(self):
        print("Vamos cadastrar o seu endereço:")
        logradouro = input('Digite o logradouro: ')
        numero = input('Digite o número: ')
        bairro = input('Digite o bairro: ')
        cidade = input('Digite a cidade: ')
        cep = input('Digite o CEP: ')
        self._endereco = endereco.Endereco(logradouro, numero, bairro, cidade, cep)
        print("Endereço adicionado com sucesso!")

    def ver_endereco(self):
        if self._endereco:
            print("Seu endereço:", self._endereco)
        else:
            print("Você ainda não cadastrou um endereço.")
    

class Entregador(Usuario):
    def __init__(self, nome,email,senha,cpf,tel,veiculo):
        super().__init__(nome,email,senha)
        self.__entregador_id = uuid4
        self.__data_cadastro = datetime.now()
        self.__cpf = cpf
        self.__telefone = tel
        self.__veiculo = veiculo

    @property
    def _entregador_id(self):
        return self.__entregador_id

    @_entregador_id.setter
    def _entregador_id(self, value):
        self.__entregador_id = value

    @property
    def _data_cadastro(self):
        return self.__data_cadastro

    @_data_cadastro.setter
    def _data_cadastro(self, value):
        self.__data_cadastro = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _veiculo(self):
        return self.__veiculo

    @_veiculo.setter
    def _veiculo(self, value):
        self.__veiculo = value


    
    
    def __repr__(self):
        return super().__repr__()




def cadastrar_usuario():
    tipo = input('Seu cadastro será para Entregador ou Cliente? ').lower()
    nome = input('Digite seu nome de usuário: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    cpf = input('Digite seu CPF: ')
    tel = input('Digite seu telefone: ')

    if tipo == 'entregador':
        veiculo = input('Seu veiculo é um carro, moto ou caminhão: ')
        novo_entregador = Entregador(nome, email, senha, cpf, tel, veiculo)
        entregadores.append(novo_entregador)
        print(f"Entregador {nome} cadastrado com sucesso!")
    elif tipo == 'cliente':
        novo_cliente = Cliente(nome, email, senha, cpf, tel)
        usuarios.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
    else:
        print('Tipo de usuário inválido.')


def realizar_login():
    email_usuario_login = input("Digite seu email de usuário: ")
    senha_login = input("Digite sua senha: ")

    for entregador in entregadores:
        if entregador._email == email_usuario_login and entregador._senha == senha_login:
            print(f"Login bem-sucedido como Entregador, {entregador._nome}!")
            menu.opt_entregador() # Chama o menu do entregador (a implementar)
            return True # Podemos retornar True aqui também se o menu do entregador tiver um loop interno

    for cliente in usuarios:
        if cliente._email == email_usuario_login and cliente._senha == senha_login:
            print(f"Login bem-sucedido como Cliente, {cliente._nome}!")
            if menu.opt_cliente(cliente): # Verifica se opt_cliente retornou True (o que significa que o cliente saiu)
                return True # Retorna True para o main.py sair do loop interno do login
            else:
                return False # Ou outra lógica se o menu do cliente não retornar True ao sair

    print("Falha no login. Usuário ou senha incorretos.")
    return None





