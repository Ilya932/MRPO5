import dataclasses
from typing import List
from xml import etree
from classes import *
#from business import *
import xml.etree.ElementTree as ET




def add_supplier(supplier):
    Supplier.add_to_xml('data2.xml', supplier)

def add_client(client):
    Client.add_to_xml('data2.xml', client)

def add_shop(shop):
    Shop.add_to_xml('data2.xml', shop)

def add_flower(flower):
    Flower.add_to_xml('data2.xml', flower)

def add_bouquet(bouquet):
    Bouquet.add_to_xml('data2.xml', bouquet)

def add_purchase(purchase):
    Purchase.add_to_xml('data2.xml', purchase)

def add_delivery(delivery):
    Delivery.add_to_xml('data2.xml', delivery)



def get_all_suppliers():
# Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()
    # Проходим по каждому элементу <Supplier> в корне
    for supplier_element in root.findall('Supplier'):
        # Получаем значения атрибутов
        id = supplier_element.find('Id').text
        name = supplier_element.find('Name').text
        print(f"Supplier: Id={id}, Name={name}")

def get_all_clients():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for supplier_element in root.findall('Client'):
        # Получаем значения атрибутов
        id = supplier_element.find('Id').text
        name = supplier_element.find('Name').text
        print(f"Client: Id={id}, Name={name}")

def get_all_shops():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for shop_element in root.findall('Shop'):
        # Получаем значения атрибутов
        id = shop_element.find('Id').text
        name = shop_element.find('Name').text
        address = shop_element.find('Address').text
        print(f"Shop: Id={id}, Name={name}, Address={address}")

def get_all_flowers():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for shop_element in root.findall('Flower'):
        # Получаем значения атрибутов
        id = shop_element.find('Id').text
        name = shop_element.find('Name').text
        price = shop_element.find('Price').text
        flower_count = shop_element.find('Flower_count').text
        shop_id = shop_element.find('Shop_id').text
        print(f"Flower: Id={id}, Name={name}, Price={price}, Flower_count={flower_count}, Shop_id={shop_id}")

def get_all_bouquet():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for bouquet_element in root.findall('Bouquet'):
        # Получаем значения атрибутов
        id = bouquet_element.find('Id').text
        flower = bouquet_element.find('Flower').text
        price = bouquet_element.find('Price')
        shop_id = bouquet_element.find('Shop_id')
        print(f"Bouquet: Id={id}, Flower={flower}, Price={price}, Shop_id={shop_id}")

def get_all_purchase():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for purchase_element in root.findall('Purchase'):
        # Получаем значения атрибутов
        id = purchase_element.find('Id').text
        bouquet_id = purchase_element.find('Bouquet_id').text
        client_id = purchase_element.find('Client_id').text
        print(f"Purchase: Id={id}, Bouquet_id={bouquet_id}, Client_id={client_id}")

def get_all_delivery():
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Проходим по каждому элементу <Supplier> в корне
    for purchase_element in root.findall('Delivery'):
        # Получаем значения атрибутов
        id = purchase_element.find('Id').text
        supplier_id = purchase_element.find('Supplier_id').text
        shop_id = purchase_element.find('Shop_id').text
        flower = purchase_element.find('Flower').text
        flower_count = purchase_element.find('Flower_count').text
        price = purchase_element.find('Price').text
        data = purchase_element.find('Data').text
        print(f"Delivery: Id={id}, Supplier_id={supplier_id}, Shop_id={shop_id}, Flower={flower}"
              f", Flower_count={flower_count}, Price={price}, Data={data}")

def get_all():
    get_all_suppliers()
    get_all_clients()
    get_all_shops()
    get_all_flowers()
    get_all_bouquet()
    get_all_delivery()
    get_all_purchase()



def remove_suppliers(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Supplier')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_clients(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Client')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_shops(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Shop')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_flowers(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Flower')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_bouquets(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Bouquet')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_purchases(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Purchase')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_deliverys(file_path):
    # Открываем XML-файл для чтения
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Находим и удаляем все элементы Supplier
    suppliers = root.findall('Delivery')
    for supplier in suppliers:
        root.remove(supplier)

    # Сохраняем изменения в XML-файл
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def remove_all(file_path):
    remove_suppliers(file_path)
    remove_clients(file_path)
    remove_shops(file_path)
    remove_flowers(file_path)
    remove_bouquets(file_path)
    remove_purchases(file_path)
    remove_deliverys(file_path)



def remove_bouquet_by_id(bouquet_id):
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()


    for bouquet in root.findall('.//Bouquet'):
        id_element = bouquet.find('Id')
        if id_element is not None and id_element.text == str(bouquet_id):
            root.remove(bouquet)

    # Сохраняем изменения в XML-файл
    tree.write('data2.xml', encoding='utf-8', xml_declaration=True)

def remove_flower_by_id(flower_id):
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()


    for bouquet in root.findall('.//Flower'):
        id_element = bouquet.find('Id')
        if id_element is not None and id_element.text == str(flower_id):
            root.remove(bouquet)

    # Сохраняем изменения в XML-файл
    tree.write('data2.xml', encoding='utf-8', xml_declaration=True)

def find_purchase_by_id(purchase_id):
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    found_suppliers = []


    for purchase in root.findall('.//Purchase'):
        id_element = purchase.find('Id')
        if id_element is not None and id_element.text == str(purchase_id):
            found_suppliers.append(purchase)
    if len(found_suppliers) > 0:
        return found_suppliers
    else:
        result = 0
        return result

def find_flower_by_id(flower_name, shop_id):
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    found_flowers = []


    for purchase in root.findall('.//Flower'):
        name_element = purchase.find('Name')
        shop_id_element = purchase.find('Shop_id')

        if (shop_id_element is not None and shop_id_element.text == str(shop_id)) and \
                    (name_element is not None and name_element.text == str(flower_name)):
            found_flowers.append(purchase)
    if len(found_flowers) > 0:
        return found_flowers
    else:
        result = 0
        return result

def update_flower(flower_name, shop_id, flower_count):
    # Открываем XML-файл для чтения
    tree = ET.parse('data2.xml')
    root = tree.getroot()

    # Находим элемент Supplier с нужным id
    for flower in root.findall('.//Flower'):
        name_element = flower.find('Name')
        shop_id_element = flower.find('Shop_id')
        if (shop_id_element is not None and shop_id_element.text == str(shop_id)) and \
                (name_element is not None and name_element.text == str(flower_name)):
            # Обновляем имя поставщика
            flower_count_element = flower.find('Name')
            flower_count_element += flower_count

    # Сохраняем изменения в XML-файл
    tree.write('data2.xml', encoding='utf-8', xml_declaration=True)


class Business2:
    def delivery_flowers(self, supplier: Supplier,  shop : Shop, flower,  flower_count, price, data):

        flowers = [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1), Flower(3, "Тюл", 8, 300, 1)]

        resoult = Delivery(supplier.id, shop.id, flower,  flower_count, price, data)
        add_delivery(resoult)
        for i in flowers:
            if (find_flower_by_id(i.name, i.shop_id) > 0):
                update_flower(i.name, i.shop_id, i.flower_count)
            else:
                add_flower(i)

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
        for q in flowers:
            remove_flower_by_id(q.id)
        add_bouquet(resoult)
        return resoult

    def purchase_bouquet(self, id, client: Client,  bouquet : Bouquet):
        resoult = Purchase(id, bouquet.id, client.id)
        add_purchase(resoult)
        remove_bouquet_by_id(bouquet.id)
        return resoult






root = ET.Element('Data')# Создаем XML-дерево из корневого элемента
tree = ET.ElementTree(root)



#get_all_suppliers()
#get_all_clients()
#get_all_shops()
#get_all_flowers()

#get_all()

"""""
new_shop = Shop(5, 'New Supplier', 'dsdfsd')
Shop.add_to_xml('data2.xml', new_shop)

new_flower = Flower(5, 'New flower', 1000, 25, 1)
Flower.add_to_xml('data2.xml', new_flower)
"""


"""
remove_all('data2.xml')

new_client = Client(1, 'New Supplier')
add_client(new_client)

new_shop = Shop(1, 'New Supplier', 'dsdfsd')
add_shop(new_shop)

flowers = [Flower(1, "Роза", 10, 100, 1), Flower(2, "Тюльпан", 8, 200, 1), Flower(3, "Тюл", 8, 300, 1)]
new_bouquet = Bouquet(1, flowers, 1000, 1)
add_bouquet(new_bouquet)

get_all()

Business2.purchase_bouquet()
"""""

