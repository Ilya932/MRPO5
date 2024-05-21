class Repository:
    def __init__(self):
        self.suppliers = []
        self.shops = []
        self.flowers = []
        self.bouquets = []
        self.clients = []
        self.delivery = []
        self.purchases = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_shop(self, shop):
        self.shops.append(shop)

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_bouquet(self, bouquet):
        self.bouquets.append(bouquet)

    def add_client(self, client):
        self.clients.append(client)

    def add_delivery(self, delivery):
        self.delivery.append(delivery)

    def purchase_bouquet(self, purchase):
        self.purchases.append(purchase)

    def get_all_suppliers(self):
        return self.suppliers

    def get_all_shops(self):
        return self.shops

    def get_all_flowers(self):
        return self.flowers

    def get_all_bouquets(self):
        return self.bouquets

    def get_all_clients(self):
        return self.clients

    def get_all_delivery(self):
        return self.delivery

    def get_all_purchase(self):
        return self.purchases

