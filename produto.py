produtos = []

class Produto:
    def __init__(self,nome,marca,quantidade_estoque:int,preco:float,peso:float):
        self.__nome = nome
        self.__marca = marca
        self.__quantidade_estoque = quantidade_estoque
        self.__preco = preco
        self.__peso = peso
        
    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _quantidade_estoque(self):
        return self.__quantidade_estoque

    @_quantidade_estoque.setter
    def _quantidade_estoque(self, value):
        self.__quantidade_estoque = value

    @property
    def _preco(self):
        return self.__preco

    @_preco.setter
    def _preco(self, value):
        self.__preco = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

    def __repr__(self):
        return f"{self._nome} - {self._marca} | Estoque: {self._quantidade_estoque} | Preço: R${self._preco} | Peso: {self._peso}kg"
    
def adicionar_produto():
    print("\nAdicionar novo produto:")
    nome = input("Nome do produto: ")
    marca = input("Marca: ")
    
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a quantidade.")
    
    while True:
        try:
            preco = float(input("Preço: R$"))
            break
        except ValueError:
            print("Por favor, digite um número válido para o preço.")
    
    while True:
        try:
            peso = float(input("Peso (kg): "))
            break
        except ValueError:
            print("Por favor, digite um número válido para o peso.")
    
    novo_produto = Produto(nome, marca, quantidade, preco, peso)
    produtos.append(novo_produto)
    print(f"\nProduto '{nome}' adicionado com sucesso!")

def remover_produto():
    if not produtos:
        print("Não há produtos cadastrados para remover.")
        return
    
    print("\nProdutos disponíveis:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i} - {produto}")
    
    while True:
        try:
            escolha = int(input("\nDigite o número do produto que deseja remover (ou 0 para cancelar): "))
            if 0 <= escolha <= len(produtos):
                break
            print("Número inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")
    
    if escolha == 0:
        print("Operação cancelada.")
        return
    
    produto_removido = produtos.pop(escolha - 1)
    print(f"\nProduto '{produto_removido._nome}' removido com sucesso!")

def listar_produtos():
    if not produtos:
        print("\nNão há produtos cadastrados.")
        return
    
    print("\nLista de Produtos:")
    for produto in produtos:
        print(produto)

def inicializar_produtos_padrao():
    notebook_1 = Produto('notebook aspire','acer',4,2799.99,1.5)
    micro_ondas = Produto('microondas hot wave','eletrolux',2,350.00,10)
    cama = Produto('cochão king','gazin',3,1749.99,30)
    produtos.append(notebook_1)
    produtos.append(micro_ondas)
    produtos.append(cama)     
        

    




        