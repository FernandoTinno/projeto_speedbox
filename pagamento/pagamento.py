class Pagamento:
    def __init__(self, valor: float):
        self.valor = valor

    def realizar_pagamento(self):
        print("Qual o método de pagamento?")
        print("1 - Cartão")
        print("2 - Pix")
        print("3 - Boleto")
        escolha = input("Digite o número correspondente: ")

        if escolha == '1':
            numero = input("Número do cartão: ")
            validade = input("Validade (MM/AA): ")
            cvv = input("CVV: ")
            pagamento = Cartao(self.valor, numero, validade, cvv)
            print("Pagamento com Cartão registrado.")
        elif escolha == '2':
            chave = input("Chave Pix: ")
            pagamento = Pix(self.valor, chave)
            print("Pagamento com Pix registrado.")
        elif escolha == '3':
            cod_barras = input("Código de barras: ")
            vencimento = input("Data de vencimento (DD/MM/AAAA): ")
            pagamento = Boleto(self.valor, cod_barras, vencimento)
            print("Pagamento com Boleto registrado.")
        else:
            print("Opção inválida.")
            pagamento = None

        return pagamento


class Cartao(Pagamento):
    def __init__(self, valor: float, numero_cartao: str, validade: str, cvv: str):
        super().__init__(valor)
        self.numero_cartao = numero_cartao
        self.validade = validade
        self.cvv = cvv


class Pix(Pagamento):
    def __init__(self, valor: float, chave_pix: str):
        super().__init__(valor)
        self.chave_pix = chave_pix


class Boleto(Pagamento):
    def __init__(self, valor: float, cod_barras: str, data_vencimento: str):
        super().__init__(valor)
        self.cod_barras = cod_barras
        self.data_vencimento = data_vencimento