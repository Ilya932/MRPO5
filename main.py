from dataclasses import dataclass
from typing import List
from classes import *
from repos import *






repo = Repository()

def c_bouquet(flow, shop):
    l = len(flow)
    c = 0
    price = 0
    for i in flow:
        for flower in repo.flowers:
            if flower.name == i[0] and flower.flower_count >= i[1] and flower.shop_id == shop:
                c += 1
    if l == c:
        for i in flow:
            for flower in repo.flowers:
                if flower.name == i[0] and flower.flower_count >= i[1] and flower.shop_id == shop:
                    price += i[1] * flower.price
    print(flow, price)


supplier1 = Supplier(1, "ИП Степанов")
supplier2 = Supplier(2, "ИП Бобров")
repo.add_supplier(supplier1)
repo.add_supplier(supplier2)


shop1 = Shop(1, "Красивый букет", "Калинина 1")
shop2 = Shop(2, "Красивый букет", "Ленини 20")
repo.add_shop(shop1)
repo.add_shop(shop2)


flower1 = Flower(1, "Роза", 10, 100, 1)
flower2 = Flower(2, "Тюльпан", 8, 200, 1)
flower3 = Flower(3, "Тюл", 8, 300, 1)
repo.add_flower(flower1)
repo.add_flower(flower2)


bouquet1 = Bouquet(1, [flower2, flower1], 20.0, 1)
bouquet2 = Bouquet(2, [flower2, flower1], 20.0, 1)
repo.add_bouquet(bouquet1)
repo.add_bouquet(bouquet2)


fl1 = ["Роза", 3]
fl2 = ["Тюльпан", 4]

c_bouquet([fl1, fl2], 1)

client1 = Client(1, "Андрей")
client2 = Client(2, "Иван")
repo.add_client(client1)
repo.add_client(client2)

purchase1 = Purchase(1, 1)
repo.purchase_bouquet(purchase1)

print("Поставщики:", repo.get_all_suppliers())
print("Магазины:", repo.get_all_shops())
print("Цветы:", repo.get_all_flowers())
print("Букеты:", repo.get_all_bouquets())
print("Покупатели:", repo.get_all_clients())
print("Покупки:", repo.get_all_purchase())
print("Доставки:", repo.get_all_delivery())




