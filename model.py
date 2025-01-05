# /model.py

class ItemType:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes if attributes else {}

class Item:
    def __init__(self, item_type, name, description, address, contact_phone, email, **kwargs):
        self.item_type = item_type
        self.name = name
        self.description = description
        self.address = address
        self.contact_phone = contact_phone
        self.email = email
        for key, value in kwargs.items():
            setattr(self, key, value)
