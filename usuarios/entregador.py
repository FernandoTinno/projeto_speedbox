from uuid import uuid4
from datetime import datetime
from .usuario import Usuario 


entregadores = []

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
    
def inicializar_entregadores_padrao():
    carlos = Entregador('Carlos Henrique','carlos_moto@gmail.com','carlos_moto123','18467529341','18997485236','moto')
    larissa = Entregador('Larissa Carvalho','larissa_carro@gmail.com','larissa_carro123','48527945613','18981479350','carro')
    jair = Entregador('Jair Silva','jair_caminhao@gmail.com','jair_caminhao123','46751003289','18957984001','caminhão')
    entregadores.extend([carlos, larissa, jair])