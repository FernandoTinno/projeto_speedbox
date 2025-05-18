class Produto:
    def __init__(self, nome: str, categoria: str, preco: float, descricao: str):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.descricao = descricao


class DetalheEnvio:
    def __init__(self, tamanho_pacote: str, peso: float, embalagem: str):
        self.tamanho_pacote = tamanho_pacote
        self.peso = peso
        self.embalagem = embalagem
