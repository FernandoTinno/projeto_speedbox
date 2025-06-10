from uuid import uuid4
from datetime import datetime
import menu
import produto
import pedido






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


class Administrador(Usuario):
    def __init__(self, nome, email, senha,acesso):
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
        
        
    
        
        

    


class Cliente(Usuario):
    def __init__(self, nome,email,senha,cpf,tel):
        super().__init__(nome,email,senha)
        self.__cliente_id = uuid4
        self.__data_cadastro = datetime.now()
        self.__cpf = cpf
        self.__telefone = tel
        self.__endereco = None
        self.__carrinho = []
        self.__pedidos_feitos = []
        self.__pedidos_avaliados = []

    
 
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
        
    @property
    def _pedidos_feitos(self):
        return self.__pedidos_feitos

    @_pedidos_feitos.setter
    def _pedidos_feitos(self, value):
        self.__pedidos_feitos = value     
                
    @property
    def _pedidos_avaliados(self):
        return self.__pedidos_avaliados

    @_pedidos_avaliados.setter
    def _pedidos_avaliados(self, value):
        self.__pedidos_avaliados = value


    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
           
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
            if produto.produtos[escolha_index]._quantidade_estoque == 0:
                print('\nProduto fora de estoque!')
                return False
            else:
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
                    print(f'Ok, o item {item._nome} foi removido com sucesso\n')
                    itens_removidos.append(item._nome)
                    
                elif remover_item == '2':
                    print(f'Tudo bem, esse item será mantido no seu carrinho\n')
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
            
    def historico_pedidos(self):
        if self._pedidos_feitos or self._pedidos_avaliados:
                print("\nSeu Histórico de Pedidos:")
                for pedidos in self._pedidos_feitos:
                    print(pedidos)
                for pedidos_avaliados in self._pedidos_avaliados:
                    print(pedidos_avaliados)
        else:
            print("Você ainda não realizou nenhum pedido.")
            return False
        
    def avaliar_pedido(self):
        
        pedidos_para_avaliar = []
        for pedido in self._pedidos_feitos:
            if pedido._status == 'concluido':
                pedidos_para_avaliar.append(pedido)
            else:
                pass
        for pedido_filtrado in pedidos_para_avaliar:
            if pedido_filtrado._avaliacao != 'pendente':
                pedidos_para_avaliar.remove(pedido_filtrado)
            else:
                pass
        
        if pedidos_para_avaliar:
            for pedido_a_avaliar in pedidos_para_avaliar:
                
                
                while True:
                    avaliar = input(f'em relação ao pedido {pedido_a_avaliar._pedido_id}\n Digite sua nota de 1 a 5 em relação ao pedido, desde a espera até o produto em si: ')
                    if avaliar in ['1','2']:
                        print(f'Sinto muito pela má experiencia que você teve {self._nome}. Agradeçemos ao seu feedback e iremos melhorar, desde já agradeço!')
                        break
                    elif avaliar in ['3','4']:
                        print(f'Ficamos contende que sua experiencia tenha sido agradavel {self._nome}. Agradeçemos ao seu feedback e iremos melhorar, para que possamos ser nota máxima!')
                        break
                    elif avaliar in ['5']:
                        print(f'Estamos cem porcento contente com sua avaliação {self._nome}. Atraves dela, conseguimos perceber que estamos fazendo um otimo serviço, muito obrigado!')
                        break
                    else:
                        print(f'A nota que você atribuiu ao pedido está incorreta')
                        
                
                while True:
                        avaliar_entregador = input(f'em relação ao entregador {pedido_a_avaliar._entregador_escolhido._nome}\n Digite sua nota de 1 a 5 em relação ao entregador, desde a valocidade de entrega, as condições em que o produto foi entregue e abordagem do entregador: ')
                        
                        if avaliar_entregador in ['1','2']:
                            print(f'Sinto muito pela má experiencia que você teve {self._nome}. Agradeçemos ao seu feedback e iremos reportar ao nosso entregador, desde já agradeço!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        elif avaliar_entregador in ['3','4']:
                            print(f'Ficamos contende que sua experiencia tenha sido agradavel {self._nome}. Agradeçemos ao seu feedback e iremos repassar para nosso entregador, para que ele se torne nota máxima!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        elif avaliar_entregador in ['5']:
                            print(f'Estamos cem porcento contente com sua avaliação {self._nome}. Atraves dela, conseguimos perceber que nosso entregador esta fazendo um otimo serviço, muito obrigado!')
                            pedido_a_avaliar._avaliacao = avaliar
                            pedido_a_avaliar._avaliacao_entregador = avaliar_entregador
                            self._pedidos_avaliados.append(pedido_a_avaliar)
                            self._pedidos_feitos.remove(pedido_a_avaliar)
                            break
                        else:
                            print(f'A nota que você atribuiu ao pedido está incorreta')                        
        else:
            print('Você não possui nenhum Pedido como concluido para poder Avaliar')           
                        
                
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
    
    def ver_nota(self):
        if self._pedidos_entregues:
            notas_avaliadas = []
            for item in self._pedidos_entregues:
                if item._avaliacao_entregador in ['1','2','3','4','5']:
                    nota_int = int(item._avaliacao_entregador)
                    notas_avaliadas.append(nota_int)
                else:
                    pass
            if notas_avaliadas:
                soma_notas = sum(notas_avaliadas)
                qtd_notas = len(notas_avaliadas)
                print(f'Quantidade de notas que Você possui: {qtd_notas}.\nAqui está sua média: {soma_notas / qtd_notas}')
            else:
                print('Você não possui nenhma avaliação ainda')
        else:
            print('Você ainda não tem nenhum pedido')
    
usuarios = []
entregadores = []
administradores = []
    
def inicializar_entregadores_padrao():
    carlos = Entregador('Carlos Henrique','carlos_moto@gmail.com','carlos_moto123','18467529341','18997485236','moto')
    larissa = Entregador('Larissa Carvalho','larissa_carro@gmail.com','larissa_carro123','48527945613','18981479350','carro')
    jair = Entregador('Jair Silva','jair_caminhao@gmail.com','jair_caminhao123','46751003289','18957984001','caminhão')
    entregadores.append(carlos)
    entregadores.append(larissa)
    entregadores.append(jair) 
    administradores.append(ceo_speedbox)   


def obter_input_validado(exibir_mensagem, condicao, exibir_erro):
    while True:
        valor = input(exibir_mensagem).strip()
        if condicao(valor):
            return valor
        else:
            print(exibir_erro)

def verificar_email_existente(email):
    verificar_email = []
    for usuario in usuarios:
            if email == usuario._email:
                verificar_email.append(usuario._email)
            else:
                pass
    for entregador in entregadores:
            if email == entregador._email:
                verificar_email.append(entregador._email)
            else:
                pass
    for administrador in administradores:
            if email == administrador._email:
                verificar_email.append(administrador._email)
            else:
                pass
    if email in verificar_email:
        return False
    else:
        return True


def cadastrar_usuario():
    
    tipo = obter_input_validado('Seu cadastro será para Cliente, Entregador ou Administrador?(digite 1 para Cliente, 2 para Entregador e 3 para Administrador): ', lambda x: x in ['1','2','3'], 'Opção de usuario incorreto')                 
    nome = obter_input_validado('Digite seu nome de usuário: ', lambda x:len(x)>=3, 'Nome de usuario não pode ter menos de três caracteres\n')
    while True:
        email = obter_input_validado('Digite seu email: ', lambda x: '@' in x and x.index('@') > 0 and x.endswith(('@gmail.com','@hotmail.com','@outlook.com')),'seu email está invalido, pois não consta o endereço de email correto ou o nome do usuario do email está incorreto\n')
        if verificar_email_existente(email) == True:
            break
        else:
            print('Email já cadastrado, tente outro endereço de email')        
    senha = obter_input_validado('Digite sua senha(no minimo oito caracteres): ', lambda x:len(x)>=8, 'A senha deve conter pelo menos oito caracteres\n')

    
    if tipo == '1':
        cpf = obter_input_validado('Digite seu cpf: ', lambda x:len(x) == 11, 'O cpf deve conter onze digitos\n')
        tel = obter_input_validado('Digite seu telefone(incluir DDD e apenas os números): ', lambda x:len(x) == 11, 'O telefone deve conter apenas números e somente onze digitos\n')
        novo_cliente = Cliente(nome, email, senha, cpf, tel)
        usuarios.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
    elif tipo == '2':
        cpf = obter_input_validado('Digite seu cpf: ', lambda x:len(x) == 11, 'O cpf deve conter onze digitos\n')
        tel = obter_input_validado('Digite seu telefone(incluir DDD e apenas os números): ', lambda x:len(x) == 11, 'O telefone deve conter apenas números e somente onze digitos\n')
        veiculo = obter_input_validado('Seu veiculo é um carro, moto ou caminhão:', lambda x: x in ['carro','moto','caminhão'], 'veiculo incorreto, tente novamente' )
        novo_entregador = Entregador(nome, email, senha, cpf, tel, veiculo)
        entregadores.append(novo_entregador)
        print(f"Entregador {nome} cadastrado com sucesso!")
    
    elif tipo == '3':
        novo_adm = Administrador(nome,email,senha,'pendente')
        administradores.append(novo_adm)
        print(f"Administrador {nome} aguardando validação de cadastro!")
        

def realizar_login():
    email_usuario_login = input("Digite seu email de usuário: ")
    senha_login = input("Digite sua senha: ")

    for admin in administradores:
        if email_usuario_login == admin._email and senha_login == admin._senha :
            if admin._acesso == 'pendente':
                print('É nescessario a validação do login para proseguir o login de administrador')
                return False
            elif admin._acesso == 'primario':
                print("Login bem-sucedido como Administrador primario!")
                if menu.opt_administrador_primario(admin):
                    return True 
                else:
                    return False
            elif admin._acesso == 'secundario':
                print("Login bem-sucedido como Administrador secundario!")
                if menu.opt_administrador_secundario(admin):
                    return True
                else:
                    return False
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
    return False
ceo_speedbox = Administrador('Fernando','fer.ceo@gmail.com','fer_ceo123','primario')
