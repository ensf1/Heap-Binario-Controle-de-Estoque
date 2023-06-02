from icecream import ic

from BinaryHeap import BinaryHeap
from Product import Product


def show_stock(stock: list):
    for product in stock:
        print(f'Produto {stock.index(product)}:{product.show_product()}')


def new_product():
    print("Informe o nome do produto:")
    name = input()
    print("Informe a quantidade em estoque")
    while (available_amount := int(input())) < 0:
        print('Valor inválido, informe outro valor:\n')
    print("Informe o nível de estoque mínimo:")
    while (min_amount := int(input())) < 0:
        print('Valor inválido, informe outro valor:\n')
    return Product(name, available_amount, min_amount)


def restock_product(products: list):
    show_stock(products)
    print("Dos produtos acima, a qual você deseja adicionar unidades ao estoque?")
    while len(products) - 1 > (index := int(input())) < 0:
        print('Esse produto não existe, informe um valor válido:\n')

    print("Quantos desse produto você deseja adicionar do estoque?")
    while products[index].insert_product(int(input())) != 0:
        print('Valor inválido\n')
    print(f'Produto atualizado:\n{products[index].show_product()}')


def deduct_product(products: list):
    show_stock(products)
    print("Dos produtos acima, a qual você deseja retirar unidades do estoque?")
    while len(products) - 1 > (index := int(input())) < 0:
        print('Esse produto não existe, informe um valor válido:\n')

    print("Quantos desse produto você deseja retirar do estoque?")
    amount = int(input())
    products[index].deduct_product_available_amount(amount)
    print(f'Produto atualizado:\n{products[index].show_product()}')


def menu_message():
    print("1 - Adicionar produto")
    print("2 - Reabastecer produtos")
    print("3 - Retirar unidades do produto do estoque")
    print("4 - Exibir estoque")
    print('Escolha uma opção acima ou aperte 9 para sair:\n')


def main():
    binary_heap = BinaryHeap()

    binary_heap.insert(Product("bolsa", 7, 0))
    binary_heap.insert(Product("escova", 9, 0))
    binary_heap.insert(Product("relógio", 8, 0))
    binary_heap.insert(Product("xícara", 100, 95))
    binary_heap.insert(Product("fosforo", 10, 1))
    binary_heap.insert(Product("açaí", 20, 9))
    binary_heap.insert(Product("moto cg", 15, 1))
    binary_heap.insert(Product("agua", 20, 3))
    binary_heap.insert(Product("gta IV", 20, 1))
    binary_heap.insert(Product("dvd ao vivo", 40, 19))
    binary_heap.insert(Product("dorflex", 66, 33))
    binary_heap.insert(Product("gasolina", 20, 2))
    binary_heap.insert(Product("peruca", 30, 3))
    binary_heap.insert(Product("cortina", 1, 2))
    binary_heap.insert(Product("vassoura", 1, 1))
    binary_heap.insert(Product("caneta", 5, 0))
    binary_heap.heap_sort_minor()
    print('Bem-vindo(a) ao controle de estoque!')
    menu_message()
    while (op := int(input())) != 9:
        if op == 1:
            product = new_product()
            binary_heap.insert(product)
            print(f' O produto abaixo foi inserido ao estoque:\n{product.show_product()}')
        elif op == 2:
            restock_product(binary_heap.heap_list)

        elif op == 3:
            deduct_product(binary_heap.heap_list)

        elif op == 4:
            show_stock(binary_heap.heap_list)

        else:
            if op != 9:
                print("Opção inválida!\n")
        binary_heap.heap_sort_minor()
        menu_message()


if __name__ == '__main__':
    main()
