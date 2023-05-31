class Product:
    def __init__(self, name, available_amount:int, min_amount:int):
        self.name = name
        self.available_amount = available_amount
        self.min_amount = min_amount

    def deduct_product_available_amount(self, amount: int):
        if self.available_amount == 0:
            print("O estoque desse produto está vazio, impossível retirar produto\n")
        elif amount > self.available_amount:
            print(f'Não há quantidade suficiente desse produto em estoque, serão retiradas apenas {(amount - self.available_amount) * -1} unidades\n')
            self.available_amount = 0
        else:
            self.available_amount -= amount
            print(f'Foram retiradas {amount} unidades, nova quantidade disponível {self.available_amount}')

    def factor(self):
        return self.available_amount - self.min_amount

    def __str__(self) -> str:
        return f'{self.factor()}'

    def __repr__(self) -> str:
        return f'{self.name}({self.factor()})'

    def show_product(self):
        return f''' {self.name}
           quantidade em estoque: {self.available_amount}
           nível de estoque mínimo: {self.min_amount}
        '''

    # def __eq__(self, other):
    #     return self.factor() == other.factor()
    #
    # def __lt__(self, other):
    #     return self.factor() < other.factor()
