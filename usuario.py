from uuid import uuid4
from datetime import datetime
import endereco
import menu
import produto
import pedido

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
        self.__carrinho = []


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
        
    @property
    def _carrinho(self):
        return self.__carrinho

    @_carrinho.setter
    def _carrinho(self, value):
        self.__carrinho = value    

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
    
    def adicionar_endereco(self):
        if not self._endereco:
            
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
            self._endereco = endereco.Endereco(logradouro, numero, bairro, cidade, estado)
            print("Endereço adicionado com sucesso!")
        else:
            print('Você já tem um endereço cadastrado')

    def remover_endereco(self):
        if self._endereco:
            confirmar = input('Você tem certeza que deseja remover o endereço (digite 1 para sim e 2 para não): ')
            while True:
                if confirmar == '1':
                    self._endereco = None
                    break
                elif confirmar == '2':
                    print('Remoção de endereço cancelada')
                    break
                else:
                    print('A opção que você digitou está incorreta')
                    confirmar = input('Você tem certeza que deseja remover o endereço (digite 1 para sim e 2 para não): ')
        else:
            print('Você não possui nenhum endereço')         
               
    def ver_endereco(self):
        if self._endereco:
            print("Seu endereço:", self._endereco)
        else:
            print("Você ainda não cadastrou um endereço.")
            
    def escolher_produto(self):
        num = 0
        for item in produto.produtos:
            num +=1
            print(f'{num} - {item._nome} Preço: {item._preco}\n')
            
        escolha = int(input('digite o numero do produto que vc gostaria de adicionar: '))
        
        if escolha == 0:
            print('opcao invalida')
        elif escolha > len(produto.produtos):
            print('opcao invalida')
        else:
            escolha_index = escolha - 1
            self._carrinho.append(produto.produtos[escolha_index])
            print(f'\n{produto.produtos[escolha_index]} foi adicionado ao seu carrinho de compras')
        
        
        
    def remover_produto(self):
        
        
        
        if self._carrinho:
            carrinho_novo = []
            itens_removidos = [] 

            for item in self._carrinho:
                print(item._nome)
                remover_item = input('Você gostaria de remover esse item?(digite 1 para sim e 2 para não): ')
                if remover_item == '1':
                    itens_removidos.append(item._nome)
                    
                elif remover_item == '2':
                    print(f'Tudo bem, esse item será mantido no seu carrinho')
                    carrinho_novo.append(item)
                else:
                    print('A opção que você selecionou está incorreta')
                    carrinho_novo.append(item) 

            self._carrinho = carrinho_novo  
        else:
            print('Você ainda não adicionou um produto ao carrinho')
            
    def ver_carrinho(self):
        if self._carrinho:
            print(f'Aqui está seu carrinho de compras: {self._carrinho}')
        else:
            print("Você ainda não adicionou nenhum produto ao carrinho.")
  
    
class Entregador(Usuario):
    def __init__(self, nome,email,senha,cpf,tel,veiculo):
        super().__init__(nome,email,senha)
        self.__entregador_id = uuid4
        self.__data_cadastro = datetime.now()
        self.__cpf = cpf
        self.__telefone = tel
        self.__veiculo = veiculo
        self.__pedidos_pendentes = []
        self.__pedidos_entregues = []

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

    @property
    def _pedidos_pendentes(self):
        return self.__pedidos_pendentes

    @_pedidos_pendentes.setter
    def _pedidos_pendentes(self, value):
        self.__pedidos_pendentes = value

    @property
    def _pedidos_entregues(self):
        return self.__pedidos_entregues

    @_pedidos_entregues.setter
    def _pedidos_entregues(self, value):
        self.__pedidos_entregues = value


    
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
    
    def concluir_pedido(self):
        if self._pedidos_pendentes: 
            for pedido_a_confirmar in self._pedidos_pendentes:
                print(f'{pedido_a_confirmar._pedido_id}, {pedido_a_confirmar._cliente._nome}')
                while True:
                    confirmar = input('o pedido desse usuario, foi concluido?(digite 1 para sim e 2 para não): ')
                    if confirmar == '1':
                        pedido_a_confirmar._status = 'concluido'
                        self._pedidos_entregues.append(pedido_a_confirmar)
                        self._pedidos_pendentes.remove(pedido_a_confirmar)
                        break
                        
                    elif confirmar == '2':
                        print(f'Tudo bem, quando for concluido, não esqueça de atualizar o Status')
                        break
                    else:
                        print('opção que voê selecionou está incorreta')
    
        else:
            print('Você não tem nenhum pedido para concluir')
    
    def historico_entregas(self):
        if self._pedidos_entregues:
                print("\nSeu Histórico de Pedidos:")
                for pedido_entregue in self._pedidos_entregues:
                    print(pedido_entregue)
        else:
            print("Você ainda não entregou nenhum pedido.")
            return False
    
def inicializar_entregadores_padrao():
    carlos = Entregador('Carlos Henrique','carlos_moto@gmail.com','carlos_moto123','18467529341','18997485236','moto')
    larissa = Entregador('Larissa Carvalho','larissa_carro@gmail.com','larissa_carro123','48527945613','18981479350','carro')
    jair = Entregador('Jair Silva','jair_caminhao@gmail.com','jair_caminhao123','46751003289','18957984001','caminhão')
    entregadores.append(carlos)
    entregadores.append(larissa)
    entregadores.append(jair)    


def cadastrar_usuario():
    while True:
        tipo = input('Seu cadastro será para Cliente ou Entregador?(digite 1 para Cliente e 2 para Entregador): ')
        if tipo in ['1','2']:
            break
        else:
            print('Opção de usuario incorreto')
            
    nome = input('Digite seu nome de usuário: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    cpf = input('Digite seu CPF: ')
    tel = input('Digite seu telefone: ')

    
    if tipo == '1':
        novo_cliente = Cliente(nome, email, senha, cpf, tel)
        usuarios.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
    elif tipo == '2':
        while True:
            veiculo = input('Seu veiculo é um carro, moto ou caminhão: ').lower()
            if veiculo not in ['carro','moto','caminhão']:
                print('veiculo incorreto, tente novamente')
            else:
                break
        novo_entregador = Entregador(nome, email, senha, cpf, tel, veiculo)
        entregadores.append(novo_entregador)
        print(f"Entregador {nome} cadastrado com sucesso!")
    


def realizar_login():
    

    email_usuario_login = input("Digite seu email de usuário: ")
    senha_login = input("Digite sua senha: ")

    for entregador in entregadores:
        if entregador._email == email_usuario_login and entregador._senha == senha_login:
            print(f"Login bem-sucedido como Entregador, {entregador._nome}!")
            if menu.opt_entregador(entregador): 
                return True 
            else:
                return False

    for cliente in usuarios:
        if cliente._email == email_usuario_login and cliente._senha == senha_login:
            print(f"Login efetuado!, {cliente._nome}!")
            if menu.opt_cliente(cliente): 
                return True 
            else:
                return False 

    print("Falha no login. Usuário ou senha incorretos.")
    return None