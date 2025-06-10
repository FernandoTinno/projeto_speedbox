cupons = []

class Cupom:
    def __init__(self,valor_cupom,quantidade):
        self.__valor = valor_cupom
        self.__quantidade = quantidade

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value
        
    def __repr__(self):
        return f"{self._valor},{self._quantidade}"


def cadastrar_cupom():
        while True:
            try:
                print('Opções de cupons:\n')
                print('50R$\n100R$\n200R$\n300R$\n500R$\n')
                valor_cupom = int(input('Gostaria de cadastrar quais desses cupons:'))  
                if valor_cupom in [50,100,200,300,500]:
                    break
                else:
                    print('Valor Invalido!')
            except ValueError:
                    print('O valor digitado não é um numero ou contem letras, digite somente o valor do cupom')
                
        while True:
            try:
                quantidade = int(input(f'Quantos cupons no valor de {valor_cupom} Voce gostaria de adicionar(somente cupons de 100 a 1000): '))
                   
                if quantidade < 100:
                    print('Deve ser atribuido no minimo 100 cupons')
                elif quantidade > 1000 :
                    print('não pode atribuir mais de 1000 cupons por requerimento')   
                else:
                    for cupom_repitido in cupons:
                        if cupom_repitido._valor == valor_cupom:
                            cupom_repitido._quantidade += quantidade
                            print(f'Reposição do estoque do cupom de {valor_cupom}R$')
                            return
                        else: 
                            pass
                    novo_cupom = Cupom(valor_cupom,quantidade)
                    cupons.append(novo_cupom)
                    print(f'O cupom de {valor_cupom}R$ foi cadastrado com sucesso!')
                    break
            except ValueError:
                print('Valor que foi digitado está incorreto')
        
        
        
def filtrar_cupom(valor_total):
        if cupons:
            cupons_escolhidos = []
            
            if valor_total >= 300 and valor_total <= 550:
                for cupom in cupons:
                    if cupom._valor == 50:
                        cupons_escolhidos.append(cupom)
                    else:
                        pass
                    
            elif valor_total >= 551 and valor_total <= 800:
                for cupom in cupons:
                    if cupom._valor == 100:
                        cupons_escolhidos.append(cupom)
                    else:
                        pass
                    
            elif valor_total >= 801 and valor_total <= 1100:
                for cupom in cupons:
                    if cupom._valor == 200:
                        cupons_escolhidos.append(cupom)
                    else:
                        pass
                    
            elif valor_total >= 1101 and valor_total <= 1450:
                for cupom in cupons:
                    if cupom._valor == 300:
                        cupons_escolhidos.append(cupom)
                    else:
                        pass
                    
            elif valor_total >= 1451:
                for cupom in cupons:
                    if cupom._valor == 500:
                        cupons_escolhidos.append(cupom)
                    else:
                        pass
                    
            if cupons_escolhidos:
                valor_cupom = 0
                quantidade_cupom = 0
                for cupom_valores in cupons_escolhidos:
                    valor_cupom += cupom_valores._valor
                    quantidade_cupom += cupom_valores._quantidade
                
                for verificar_quantidade_cupom in cupons_escolhidos:
                    if verificar_quantidade_cupom._quantidade >= 1:
                        while True:
                    
                            escolha = input(f'Voce possui um de {valor_cupom}R$ para usar, Você usar(1 para sim e 2 para não): ')

                            if escolha == '1':
                                for remover_cupom in cupons:
                                    if remover_cupom._valor == valor_cupom:
                                        remover_cupom._quantidade -= 1
                                    else:
                                        pass
                                valor_total -= valor_cupom
                                print(f'Desconto de {valor_cupom}R$ aplicado com sucesso. Agora o valor total da sua compra é de: {valor_total}')
                                return valor_total
                            elif escolha == '2':
                                print(f'Tudo bem, o cupom de {valor_cupom} não será usado para obter desconto\n')
                                break
                            else:
                                print('Opção inválida')
                    else:
                        print('Cupom Esgotado')

                    

                
            else:
                print('Não há nenhum cupom aplicavel!')
                return False
        else:
            print('não foi liberado nenhum cupom de desconto')
            return False