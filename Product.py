class Product:
    def __init__(self, name, available_amount: int, min_amount: int):
        self.name = name
        self._available_amount = 0
        self.min_amount = min_amount
        self.insert_product(available_amount)

    def deduct_product_available_amount(self, amount: int):
        if self._available_amount == 0:
            print("O estoque desse produto está vazio, impossível retirar unidades do produto\n")

        elif amount > self._available_amount:
            print(
                f'Não há quantidade suficiente desse produto em estoque, serão retiradas apenas {self._available_amount} unidades\n')
            self._available_amount = 0

        else:
            self._available_amount -= amount
            print(f'Foram retiradas {amount} unidades, nova quantidade disponível {self._available_amount}\n')

    def factor(self):
        return self._available_amount - self.min_amount

    def insert_product(self, amount: int):
        if amount <= 0:
            return 1
        else:
            self._available_amount += amount
            return 0

    def __str__(self) -> str:
        return f'{self.factor()}'

    def __repr__(self) -> str:
        return f'{self.name}({self.factor()})'

    def show_product(self):
        return f''' {self.name}:
           quantidade em estoque: {self._available_amount}
           nível de estoque mínimo: {self.min_amount}
        '''
