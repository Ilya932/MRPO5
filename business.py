import dataclasses

from classes import *
from dataclasses import dataclass



class Business2:
    def delivery_flowers(self, supplier: Supplier,  shop : Shop, flower,  flower_count, price, data):

        flowers = [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1), Flower(3, "Тюл", 8, 300, 1)]

        resoult = Delivery(supplier.id, shop.id, flower,  flower_count, price, data)

        for i in flowers:

            if (flower == i.name and shop.id == i.shop_id):
                i = dataclasses.replace(i, flower_count=i.flower_count + flower_count)
        return resoult


    def create_bouquet(self, flow, shop_id):
        price = 0
        flowers = [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1), Flower(3, "Тюл", 8, 300, 1)]

        for i in flow:
            for j in flowers:
                if j.name == i.name and j.flower_count >= i.flower_count and j.shop_id == shop_id:
                    price = price + i[1] * Flower.price

                if j.name == i.name and j.flower_count < i.flower_count and j.shop_id == shop_id:
                    return False
        resoult = Bouquet(1, flow, price, shop_id)
        return resoult

    def purchase_bouquet(self, client: Client,  bouquet : Bouquet):
        resoult = Purchase(bouquet.id, client.id)
        return resoult

