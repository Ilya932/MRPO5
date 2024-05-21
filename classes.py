from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

@dataclass(frozen=True)
class Supplier:
    id: int
    name: str

    def Supplier_to_xml(self):
        supplier_element = ET.Element('Supplier')
        id_element = ET.SubElement(supplier_element, 'Id')
        id_element.text = str(self.id)
        name_element = ET.SubElement(supplier_element, 'Name')
        name_element.text = self.name
        return supplier_element

    @staticmethod
    def add_to_xml(file_path, supplier):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        supplier_element = supplier.Supplier_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(supplier_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

@dataclass(frozen=True)
class Shop:
    id: int
    name: str
    address: str

    def Shop_to_xml(self):
        shop_element = ET.Element('Shop')
        id_element = ET.SubElement(shop_element, 'Id')
        id_element.text = str(self.id)
        name_element = ET.SubElement(shop_element, 'Name')
        name_element.text = self.name
        address_element = ET.SubElement(shop_element, 'Address')
        address_element.text = self.address
        return shop_element

    @staticmethod
    def add_to_xml(file_path, shop):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        shop_element = shop.Shop_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(shop_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)


@dataclass(frozen=True)
class Flower:
    id: int
    name: str
    price: float
    flower_count: int
    shop_id: int


    def Flower_to_xml(self):
        flower_element = ET.Element('Flower')
        id_element = ET.SubElement(flower_element, 'Id')
        id_element.text = str(self.id)
        name_element = ET.SubElement(flower_element, 'Name')
        name_element.text = self.name
        price_element = ET.SubElement(flower_element, 'Price')
        price_element.text = str(self.price)
        flower_count_element = ET.SubElement(flower_element, 'Flower_count')
        flower_count_element.text = str(self.flower_count)
        shop_id_element = ET.SubElement(flower_element, 'Shop_id')
        shop_id_element.text = str(self.shop_id)
        return flower_element

    @staticmethod
    def add_to_xml(file_path, flower):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        flower_element = flower.Flower_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(flower_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

@dataclass(frozen=True)
class Client:
    id: int
    name: str

    def Client_to_xml(self):
        client_element = ET.Element('Client')
        id_element = ET.SubElement(client_element, 'Id')
        id_element.text = str(self.id)
        name_element = ET.SubElement(client_element, 'Name')
        name_element.text = self.name
        return client_element

    @staticmethod
    def add_to_xml(file_path, client):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        client_element = client.Client_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(client_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)


class Bouquet:
    def __init__(self, id, flower, price, shop_id):
        self.id = id
        self.flower = flower
        self.price = price
        self.shop_id = shop_id

    def Bouquet_to_xml(self):
        bouquet_element = ET.Element('Bouquet')
        id_element = ET.SubElement(bouquet_element, 'Id')
        id_element.text = str(self.id)
        flower_element = ET.SubElement(bouquet_element, 'Flower')
        flower_element.text = str(self.flower)
        price_element = ET.SubElement(flower_element, 'Price')
        price_element.text = str(self.price)
        shop_id_element = ET.SubElement(flower_element, 'Shop_id')
        shop_id_element.text = str(self.shop_id)
        return bouquet_element

    @staticmethod
    def add_to_xml(file_path, bouquet):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        bouquet_element = bouquet.Bouquet_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(bouquet_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

class Delivery:
    def __init__(self, id, supplier_id, shop_id, flower, flower_count, price, data):
        self.id = id
        self.supplier_id = supplier_id
        self.shop_id = shop_id
        self.flower = flower
        self.flower_count = flower_count
        self.price = price
        self.data = data

    def Delivery_to_xml(self):
        delivery_element = ET.Element('Delivery')
        id_element = ET.SubElement(delivery_element, 'Id')
        id_element.text = str(self.id)
        supplier_id_element = ET.SubElement(delivery_element, 'Supplier_id')
        supplier_id_element.text = str(self.supplier_id)
        shop_id_element = ET.SubElement(delivery_element, 'Shop_id')
        shop_id_element.text = str(self.shop_id)
        flower_element = ET.SubElement(delivery_element, 'Flower')
        flower_element.text = self.flower
        flower_count_element = ET.SubElement(flower_element, 'Flower_count')
        flower_count_element.text = str(self.flower_count)
        price_element = ET.SubElement(flower_element, 'Price')
        price_element.text = str(self.price)
        data_element = ET.SubElement(delivery_element, 'Data')
        data_element.text = str(self.data)
        return delivery_element

    @staticmethod
    def add_to_xml(file_path, delivery):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        delivery_element = delivery.Delivery_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(delivery_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

class Purchase:
    def __init__(self, id, bouquet_id, client_id):
        self.id = id
        self.bouquet_id = bouquet_id
        self.client_id = client_id

    def Purchase_to_xml(self):
        purchase_element = ET.Element('Purchase')
        id_element = ET.SubElement(purchase_element, 'Id')
        id_element.text = str(self.id)
        bouquet_id_element = ET.SubElement(purchase_element, 'Bouquet_id')
        bouquet_id_element.text = str(self.bouquet_id)
        client_id_element = ET.SubElement(purchase_element, 'Client_id')
        client_id_element.text = str(self.client_id)
        return purchase_element

    @staticmethod
    def add_to_xml(file_path, purchase):
        # Открываем существующий XML-файл для чтения
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Преобразуем экземпляр класса в XML-элемент
        purchase_element = purchase.Purchase_to_xml()
        # Добавляем новый элемент к корневому элементу
        root.append(purchase_element)
        # Сохраняем изменения в XML-файл
        tree.write(file_path, encoding='utf-8', xml_declaration=True)



