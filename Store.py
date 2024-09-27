class Store():
    def __init__(self, name, address,items):
        self.name = name
        self.address = address
        self.items = items

    def add(self,product,price):
        self.items[product] = price

    def delete_product(self, product):
        self.items.pop(product)
        return self.items

    def price(self, product):
        return self.items.get(product)

store1 = Store('Первый продуктовый', 'Кирпичный переулок 12а', {'яблоки': 100, 'бананы': 150})
store2 = Store('Все для сада и дачи', 'Улица Сосновая, дом 5', {'лопата': 78, 'тачка': 400})
store3 = Store('Мечта идиота', 'Проспект Пушкина Калатушкина, дом 18', {'электросамокат': 100500, 'волшебная палочка': 500})

# Добавим новый товар
store1.add('груши', 130)
print(store1.items)

# Для изменения цены товара, можно использовать тот же метод, что и для добавления нового товара
store1.add('яблоки', 75)
print(store1.items)

# Уберем товар
store1.delete_product('бананы')
print(store1.items)

# Запросим цену товара "яблоки"
print(store1.price("яблоки"))
