import menu
from .cliente import Cliente, usuarios
from .entregador import Entregador, entregadores
from .adm import Administrador, administradores

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
        email = obter_input_validado('Digite seu email: ', lambda x: '@' in x and x.index('@') > 0 and x.endswith(('@gmail.com','@hotmail.com','@outlook.com')),'seu email está invalido\n')
        if verificar_email_existente(email):
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
        veiculo = obter_input_validado('Seu veiculo é um carro, moto ou caminhão:', lambda x: x in ['carro','moto','caminhão'], 'veiculo incorreto, tente novamente\n' )
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
        if email_usuario_login == admin._email and senha_login == admin._senha:
            if admin._acesso == 'pendente':
                print('É nescessario a validação do login para proseguir.')
                return
            elif admin._acesso == 'primario':
                print("Login bem-sucedido como Administrador primario!")
                menu.opt_administrador_primario(admin)
                return
            elif admin._acesso == 'secundario':
                print("Login bem-sucedido como Administrador secundario!")
                menu.opt_administrador_secundario(admin)
                return

    for entregador in entregadores:
        if entregador._email == email_usuario_login and entregador._senha == senha_login:
            print(f"Login bem-sucedido como Entregador, {entregador._nome}!")
            menu.opt_entregador(entregador)
            return

    for cliente in usuarios:
        if cliente._email == email_usuario_login and cliente._senha == senha_login:
            print(f"Login efetuado!, {cliente._nome}!")
            menu.opt_cliente(cliente)
            return

    print("Falha no login. Usuário ou senha incorretos.")