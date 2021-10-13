from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class OrderResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template):
        res = RDBService.find_by_template("order", "order", template, None)
        return res

    @classmethod
    def create(cls, data):
        new_order = dict()
        new_order['user_id'] = data['user_id']
        new_order['product_id'] = data['product_id']
        new_order['quantity'] = data['quantity']
        new_order['price'] = data['price']
        res = RDBService.create("order", "order", new_order)

    @classmethod
    def update(cls, template, row):
        res = RDBService.update("order", "order", template, row)
        return res

    @classmethod
    def delete(cls, template):
        res = RDBService.delete("order", "order", template)
        return res