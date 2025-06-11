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


    def aprovar_contas(self):
        administradores_pendentes = []
        for adm_pendente in administradores:
            if adm_pendente._acesso == 'pendente':
                administradores_pendentes.append(adm_pendente)
            else:
                pass
        if administradores_pendentes:
            
            for adm_a_confirmar in administradores_pendentes:
                print(f'Nome: {adm_a_confirmar._nome} Email: {adm_a_confirmar._email}\n')
                while True:
                    confirmar = input('Você deseja confirmar o acesso a essa conta?(digite 1 para sim e 2 para não): ')
                    if confirmar == '1':
                        adm_a_confirmar._acesso = 'secundario'
                        print(f'Acesso permitido para o usuario {adm_a_confirmar._nome}\n')
                        break
                    elif confirmar == '2':
                        print(f'Acesso negado para o usuario {adm_a_confirmar._nome}\n')
                        break
                    else:
                        print('opção que voê selecionou está incorreta')
            
        else:
            print('Não há nenhuma conta para aprovar')

    
    def promover_contas_administrador(self):
        adms_secundarios = []
        for adms in administradores:
            if adms._acesso == 'secundario':
                adms_secundarios.append(adms)
            else:
                pass    
        
        if adms_secundarios:   
            for subir_conta_adm in adms_secundarios:
                
                print(f'Nome: {subir_conta_adm._nome} Email: {subir_conta_adm._email}\n')
                while True:
                    confirmar = input('Você deseja promover o acesso a essa conta?(digite 1 para sim e 2 para não): ')
                    if confirmar == '1':
                        subir_conta_adm._acesso = 'primario'
                        print(f'O administrador {subir_conta_adm._nome} agora tem acesso primario\n')
                        break
                    elif confirmar == '2':
                        print(f'O usuario {subir_conta_adm._nome} não foi promovido\n')
                        break
                    else:
                        print('opção que voê selecionou está incorreta')
        else:
            print('Não há nenhuma conta para promover')
    
    
    def rebaixar_contas_administrador(self):
        contas_adm = []
         
        for adms in administradores:
            if adms._acesso != 'pendente' and adms._acesso != 'primordial' and adms._email != self._email:
                contas_adm.append(adms)
            else:
                pass
        
        if contas_adm:
            for conta_adm in contas_adm:
                print(f'Nome: {conta_adm._nome} Email: {conta_adm._email} Acesso: {conta_adm._acesso}\n')
                while True:
                    confirmar = input('Você deseja rebaixar o acesso a essa conta?(digite 1 para sim e 2 para não): ')
                    if confirmar == '1':
                        if conta_adm._acesso == 'primario':
                            conta_adm._acesso = 'secundario'
                            print(f'O acesso da conta do administrador {conta_adm._nome} foi reduzido a secundario') 
                            break  
                        elif conta_adm._acesso == 'secundario':
                            
                            while True:
                                deletar = input(f'o acesso da conta desse administrador é secundario, ao rebaixar o acesso dessa conta, você estará excluindo essa conta definitivamente, você realmente deseja continuar?(digite 1 para sim e 2 para não):')
                                if deletar == '1':
                                    print(f'a conta do administrador {conta_adm._nome} foi removida do sistema')
                                    administradores.remove(conta_adm)
                                    break
                                    
                                elif deletar == '2':
                                    print('Ok, essa conta com acesso secundario continuara no sistema')
                                    break   
                                else:
                                    print('Opção invalida, digite 1 ou 2')
                                    
                            break          
                    elif confirmar == '2':
                        print(f'O usuario {conta_adm._nome} não foi rebaixado')
                        break
                    else:
                        print('opção que voê selecionou está incorreta')       
        else:    
            print('Não há nehuma conta para rebaixar') 
            
        
def inicializar_adm_padrao():
    ceo_speedbox = Administrador('Fernando','fer.ceo@gmail.com','fer_ceo123','primordial')
    administradores.append(ceo_speedbox)