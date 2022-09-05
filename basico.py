
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
    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))
        #para visualizar a soma no console : carrinho.valor


carrinho = Carrinho() 

carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))
carrinho.adicionar_item(Item('fritas', 5000))

