"""
EXEMPLO DE USO DO DESIGN PATTERN CHAIN OF RESPONSABILITY
"""

from abc import ABC, abstractstaticmethod

class Item:
    #método construtor 
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor
      
    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    #inicializa a lista de itens
    def __init__(self):
        self.itens = []

    #adiciona os itens numa lista
    def adicionar_item(self, item: Item):
        self.itens.append(item)
        #para visualizar a lista no console: carrinho.itens

    #soma de todos os itens da lista
    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))
        #para visualizar a soma no console : carrinho.valor


#de fato uma promoção; uma interface
#classe abstrata: o modo de como a classe será implementada
class Promocao(ABC):

    @abstractstaticmethod
    def calcular(self, valor):
        ...
class PromocaoMaisDeMil(Promocao):
   # def __init__(self, next=None):
    #    self.next = next

    def calcular(self, carrinho: Carrinho):
        if carrinho.valor >= 1_000:
            print("promoção Mais de Mil aplicada !")
            return carrinho.valor - (carrinho.valor * 0.2)
        return self.next.calcular(carrinho) #se não estiver mais de mil reais no carrinho, chama a próxima promoção


class Promocao5NoCarrinho(Promocao):
    #def __init__(self, next=None):
      #  self.next = next 

    def calcular(self, carrinho: Carrinho):
        if len(carrinho.itens) >= 5:
            print("promoção Mais de 5 aplicada !")
            return carrinho.valor - (carrinho.valor * 0.1)
        return self.next.calcular(carrinho) #se não tiver 5 itens, chama a próxima promoção


class SemPromocao(Promocao):
  def calcular(self,carrinho:Carrinho):
    print("Nenhuma promoção aplicada!")
    return carrinho.valor  #perceba que aqui não tem chamada para um próximo método, pois aqui é o ponto de parada

class CalculadoraDePromocoes:
      # a ideia não é ser cumulativo, mas se ele nao cair na promoção MaiDeMil, ele tem que retornar o próximo
    def calcular(self, valor):
      p1 = PromocaoMaisDeMil()
      p2 = Promocao5NoCarrinho()
      p3 = SemPromocao()

      p1.next = p2
      p2.next = p3
      return p1.calcular(valor)

carrinho = Carrinho()

#Para testar a promoção mais de 5
carrinho.adicionar_item(Item(nome='kitkat',valor=10))
carrinho.adicionar_item(Item(nome='kitkat',valor=10))
carrinho.adicionar_item(Item(nome='kitkat',valor=10))
carrinho.adicionar_item(Item(nome='kitkat',valor=10))
carrinho.adicionar_item(Item(nome='kitkat',valor=10))
# para testar a promoção mais de mil"
carrinho.adicionar_item(Item(nome='kindle',valor=1005))
# para testar o acionamento de nenhuma promoção
carrinho.adicionar_item(Item(nome='kiwi',valor=1)) 

calculadora = CalculadoraDePromocoes()

print(f'Valor sem promocao: {carrinho.valor}')
print(f'Valor com promocao: {calculadora.calcular(carrinho)}')
