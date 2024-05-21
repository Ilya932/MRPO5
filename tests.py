import unittest
from business import Business2
from classes import *



class Test(unittest.TestCase):

    def setUp(self):
        self.service = Business2()


    def test_purchase_bouquet(self):

        client = Client(1, "Александр")
        bouquet = Bouquet(1, [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1)], 20.0, 1)

        purchase = self.service.purchase_bouquet(client, bouquet)
        self.assertIsInstance(purchase, Purchase)
        self.assertEqual(purchase.client_id, client.id)
        self.assertEqual(purchase.bouquet_id, bouquet.id)

    def test_delivery_flowers(self):
        supplier = Supplier(1, "Александр")
        shop = Shop(1, "Александр", "fddffs")
        delivery = self.service.delivery_flowers(supplier, shop, "Роза", 100, 20000, "2024-03-24")
        self.assertIsInstance(delivery, Delivery)
        self.assertEqual(delivery.supplier_id, supplier.id)
        self.assertEqual(delivery.shop_id, shop.id)

    def test_create_bouquet(self):
        flowers =  [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1)]
        shop = Shop(1, "Александр", "fddffs")
        bouquet = self.service.create_bouquet(flowers, shop)
        self.assertIsInstance(bouquet, Bouquet)
        self.assertEqual(bouquet.flower, flowers)
        self.assertEqual(bouquet.shop_id.id, shop.id)