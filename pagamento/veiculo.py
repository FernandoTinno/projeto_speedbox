class Veiculo:
    def __init__(self, modelo: str, marca: str, cor: str, placa: str):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.placa = placa

    def cadastrar_veiculo(self):
        pass

    def remover_veiculo(self):
        pass


class Moto(Veiculo):
    def __init__(self, modelo: str, marca: str, cor: str, placa: str,
                 cilindrada: str, tipo_partida: str, categoria: str):
        super().__init__(modelo, marca, cor, placa)
        self.cilindrada = cilindrada
        self.tipo_partida = tipo_partida
        self.categoria = categoria


class Carro(Veiculo):
    def __init__(self, modelo: str, marca: str, cor: str, placa: str,
                 numero_portas: str, carroceria: str, tipo_transmissao: str):
        super().__init__(modelo, marca, cor, placa)
        self.numero_portas = numero_portas
        self.carroceria = carroceria
        self.tipo_transmissao = tipo_transmissao


class Caminhao(Veiculo):
    def __init__(self, modelo: str, marca: str, cor: str, placa: str,
                 capacidade_carga: float, num_eixos: int, bau: bool):
        super().__init__(modelo, marca, cor, placa)
        self.capacidade_carga = capacidade_carga
        self.num_eixos = num_eixos
        self.bau = bau