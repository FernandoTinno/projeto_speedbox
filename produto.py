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
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    while True:
        try:
            preco = float(input("Preço: R$"))
            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido para o preço.")
    
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue
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
    for i, prod in enumerate(produtos, 1):
        print(f"{i} - {prod._nome} (Marca: {prod._marca}, Estoque: {prod._quantidade_estoque})")
    
    while True:
        try:
            escolha = input("\nDigite o número do produto que deseja remover (ou 0 para cancelar): ")
            if escolha == '0':
                print("Operação cancelada.")
                return
                
            escolha = int(escolha)
            if 1 <= escolha <= len(produtos):
                break
            print(f"Por favor, digite um número entre 1 e {len(produtos)} ou 0 para cancelar.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    produto_removido = produtos.pop(escolha - 1)
    print(f"\nProduto '{produto_removido._nome}' removido com sucesso!")

def listar_produtos():
    if not produtos:
        print("\nNão há produtos cadastrados.")
        return
    
    print("\nLista de Produtos:")
    for i, prod in enumerate(produtos, 1):
        print(f"{i} - {prod._nome} (Marca: {prod._marca}, Estoque: {prod._quantidade_estoque}, Preço: R${prod._preco:.2f}, Peso: {prod._peso}kg)")

def repor_estoque_produto():
    if produtos:
        
        print(f'aqui está sua lista de produtos:\n')
    
        num = 0
        for item in produtos:
            num +=1
            print(f'{num} - {item._nome} quantidade em estoque: {item._quantidade_estoque}\n')
                
        escolha = int(input('digite o numero do produto que vc gostaria de repor o estoque: '))
            
        if escolha == 0:
            print('opcao invalida')
            
        elif escolha > len(produtos):
            print('opcao invalida')
            
        else:
            while True:
                escolha_index = escolha - 1
                try:
                    qtd = int(input(f'Digite a quantidade de produtos que seram adicionados ao {produtos[escolha_index]._nome}(de 1 a 1000): '))
                    if qtd <= 0:
                        print(f'o valor {qtd} não é valido para atibuição de estoque')
                    elif qtd > 1000:
                        print('Essa quantidade de produtos não pode ser adicionado em um unico requerimento de reposição de estoque')
                    else:
                        produtos[escolha_index]._quantidade_estoque += qtd
                        print(f'O estoque do produto {produtos[escolha_index]._nome} agora é de: {produtos[escolha_index]._quantidade_estoque} unidades')
                        return
                except ValueError:
                    print('Valor que foi digitado está incorreto')
                
    else:
        print('Não tem nenhum produto registrado no estoque da empresa')
        return False
                    
                


def inicializar_produtos_padrao():
    notebook_1 = Produto('notebook aspire', 'acer', 4, 2799.99, 1.5)
    micro_ondas = Produto('microondas hot wave', 'eletrolux', 2, 350.00, 10)
    cama = Produto('cochão king', 'gazin', 3, 1749.99, 30)
    produtos.extend([notebook_1, micro_ondas, cama])     
        

    




        