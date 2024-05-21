from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from classes_for_abs import *
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session



class AbstractRepository(ABC):

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass


class SQLAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session, model_class):
        self.session = session
        self.model_class = model_class

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def get(self, id):
        return self.session.query(self.model_class).filter_by(id=id).one_or_none()

    def list(self):
        query = self.session.query(self.model_class)
        return query.all()

    def update(self, entity):
        obj = self.get(entity.id)
        if obj:
            for key, value in vars(entity).items():
                setattr(obj, key, value)
            self.session.commit()
            return obj
        return None

    def delete(self, entity):
        obj = self.get(entity.id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False



class Business2:
    def __init__(self, supplier_repo, client_repo, shop_repo, flower_repo, bouquet_repo, purchase_repo, delivery_repo):
        self.supplier_repo = supplier_repo
        self.client_repo = client_repo
        self.shop_repo = shop_repo
        self.flower_repo = flower_repo
        self.bouquet_repo = bouquet_repo
        self.purchase_repo = purchase_repo
        self.delivery_repo = delivery_repo

    def delivery_flowers(self, supplier, shop, flower, flower_count, price, date):

        delivery = Delivery(
            supplier_id=supplier.id,
            shop_id=shop.id,
            flower_name=flower.name,
            flower_count=flower_count,
            price=price,
            date=datetime.strptime(date, '%Y-%m-%d')
        )
        self.delivery_repo.add(delivery)
        return delivery

    def create_bouquet(self, flowers, shop_id):
        price = 0

        for flower in flowers:
            flower_from_repo = self.flower_repo.get(flower.id)
            if flower_from_repo and flower_from_repo.flower_count >= flower.flower_count:
                price += flower.price * flower.flower_count
            else:
                return False

        bouquet = Bouquet(flower=','.join([f.name for f in flowers]), price=price, shop_id=shop_id)
        self.bouquet_repo.add(bouquet)
        for flower in flowers:
            flower_from_repo = self.flower_repo.get(flower.id)
            flower_from_repo.flower_count -= flower.flower_count
            self.flower_repo.update(flower_from_repo)

        return bouquet

    def purchase_bouquet(self, id, client: Client, bouquet: Bouquet):
        purchase = Purchase(id=id, bouquet_id=bouquet.id, client_id=client.id)
        self.purchase_repo.add(purchase)
        self.bouquet_repo.delete(bouquet)
        return purchase



engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session2 = sessionmaker(bind=engine)
session = Session2()


supplier_repo = SQLAlchemyRepository(session, Supplier)
client_repo = SQLAlchemyRepository(session, Client)
shop_repo = SQLAlchemyRepository(session, Shop)
flower_repo = SQLAlchemyRepository(session, Flower)
bouquet_repo = SQLAlchemyRepository(session, Bouquet)
purchase_repo = SQLAlchemyRepository(session, Purchase)
delivery_repo = SQLAlchemyRepository(session, Delivery)


business = Business2(supplier_repo, client_repo, shop_repo, flower_repo, bouquet_repo, purchase_repo, delivery_repo)


new_supplier = Supplier(name='Supplier1')
supplier_repo.add(new_supplier)

new_shop = Shop(name='Shop1', address='123 Street')
shop_repo.add(new_shop)

new_flower = Flower(name='Rose', price=10, flower_count=100, shop_id=new_shop.id)
flower_repo.add(new_flower)
new_flower = Flower(name='Тюльпан', price=8, flower_count=200, shop_id=new_shop.id)
flower_repo.add(new_flower)
new_flower = Flower(name='Тюл', price=8, flower_count=300, shop_id=new_shop.id)
flower_repo.add(new_flower)


client = Client(name='Client1')
client_repo.add(client)

client = Client(name='Client2')
client_repo.add(client)







