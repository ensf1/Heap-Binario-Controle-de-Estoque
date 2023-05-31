from icecream import ic

from BinaryHeap import BinaryHeap
from Product import Product


def add_product():
    print("Informe o nome do produto:")
    name = input()
    print("Informe a quantidade em estoque")
    available_amount = int(input())
    print("Informe o nível de estoque mínimo:")
    min_amount = int(input())
    return Product(name, available_amount, min_amount)


def restock_product(products):
    print("Dos produtos abaixo, qual deseja adicionar unidades ao estoque?")
    for item in products:
        print(f'Produto {products.index(item)}:{item.show_product()}')
    index = int(input())
    print("Quantos desse produto você deseja adicionar do estoque?")
    amount = int(input())
    products[index].available_amount += amount
    return products


def deduct_product(products:list):
    print("Dos produtos abaixo, qual deseja retirar unidades do estoque?")
    for item in products:
        print(f'Produto {products.index(item)}:{item.show_product()}')
    index = int(input())
    print("Quantos desse produto você deseja retirar do estoque?")
    amount = int(input())
    products[index].deduct_product_available_amount(amount)
    return products


def main():
    binary_heap = BinaryHeap()

    binary_heap.insert(Product("bolsa", 7, 0))
    binary_heap.insert(Product("relógio", 8, 0))
    binary_heap.insert(Product("escova", 9, 0))
    # binary_heap.insert(Product("xícara", 100, 95))
    # binary_heap.insert(Product("fosforo", 10, 1))
    # binary_heap.insert(Product("açaí", 20, 9))
    # binary_heap.insert(Product("moto cg", 15, 1))
    # binary_heap.insert(Product("agua", 20, 3))
    # binary_heap.insert(Product("gta IV", 20, 1))
    # binary_heap.insert(Product("dvd ao vivo", 40, 19))
    # binary_heap.insert(Product("dorflex", 66, 33))
    # binary_heap.insert(Product("gasolina", 20, 2))
    # binary_heap.insert(Product("peruca", 30, 3))
    # binary_heap.insert(Product("cortina", 1,2))
    # binary_heap.insert(Product("vassoura", 1,1))
    # binary_heap.insert(Product("caneta", 5,0))

    # binary_heap.build_heap(binary_heap.heap_list)
    # print([x for x in binary_heap.heap_list])
    op = 0
    while op != 9:
        print("1 - Adicionar produto")
        print("2 - Reabastecer produtos")
        print("3 - Retirar produto do estoque")
        op = int(input())
        if op == 1:
            binary_heap.insert(add_product())
        elif op == 2:
            binary_heap.build_heap(restock_product(binary_heap.heap_list))
        elif op == 3:
            binary_heap.build_heap(deduct_product(binary_heap.heap_list))
        else:
            print("opção inválida")


if __name__ == '__main__':
    main()
