class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, cep):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def get_logradouro(self):
        return self.logradouro

    def set_logradouro(self, value):
        self.logradouro = value

    def get_numero(self):
        return self.numero

    def set_numero(self, value):
        self.numero = value

    def get_bairro(self):
        return self.bairro

    def set_bairro(self, value):
        self.bairro = value

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, value):
        self.cidade = value

    def get_cep(self):
        return self.cep

    def set_cep(self, value):
        self.cep = value


    def __repr__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.cep}"