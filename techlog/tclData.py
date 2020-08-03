"""
User friendly connection to server(db) through API
"""

class NoData(Exception):
    pass


class Connector():
    def __init__(self, address: str = None, port: int = None):
        if address is None:
            raise NoData('There is no host. Set the host.')

        if port is None:
            raise NoData('There is no port. Set the port.')

        self.address = address
        self.port = port

    @property
    def get_address(self):
        return self.address

    def get_customer(self, customer_id):
        pass

    def get_customers(self):
        pass

    def get_field(self, field_id):
        pass

    def get_fields(self):
        pass

    def get_customers(self):
        pass

    def get_customers(self):
        pass


c = Connector(port=10000)