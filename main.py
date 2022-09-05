from abc import ABC, abstractstaticmethod

class Item:
    #metodo inicializador
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor
    #metodo de representação para visulização na manipulação
    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    #inicializa a lista de itens 
    def  __init__(self):
        self.itens = []
    #adiciona os itens numa lista
    def adicionar_item(self, item: Item):
        self.itens.append(item)
        #para visualizar a lista no console: carrinho.itens      
    #soma de todos os itens da lista
    #property para nã ficar chamando o metodo toda hora (aula 68 por ai)
    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))
        #para visualizar a soma no console : carrinho.valor

#aqui pode manipular todas as promoções como um todo        
class CalculadoraDePromocoes:
    def calcular(self,valor):
      return PromocaoMaisDeMil(Promocao5NoCarrinho().calcular(valor))

      
#de fato uma promoção; uma interface
#classe abstrata: o modo de como a classe será implementada
class Promocao(ABC):
  @abstractstaticmethod
  def calcular(self,valor):
    ...

class Promocao5NoCarrinho(Promocao):
  def __init__(self, next = None):
    self.next = next
  def calcular(self, carrinho: Carrinho):
    if len(carrinho) >= 5:
      return carrinho.valor - (carrinho.valor *0.1)
# a ideia não é ser cumulativo, mas se ele nao cair na promoção de 5, ele tem que retornar o próximo
    return self.next.calcular(carrinho)
carrinho = Carrinho() 

class PromocaoMaisDeMil(Promocao):
  def __init__(self, next = None):
    self.next = next
  def calcular(self, carrinho: Carrinho):
    if carrinho.valor >= 1.000:
      return carrinho.valor - (carrinho.valor *0.2)
# a ideia não é ser cumulativo, mas se ele nao cair na promoção de 5, ele tem que retornar o próximo
    return self.next.calcular(carrinho)
carrinho = Carrinho() 



carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))

calculadora = CalculadoraDePromocoes()

print(f'Valor sem promocao: {carrinho.valor}')
print(f'Valor com promocao: {calculadora.calcular(carrinho)}')

