# model.py
class User:
    def __init__(self, username, password, address, contact, is_admin=False, is_approved=False):
        self.username = username
        self.password = password
        self.address = address
        self.contact = contact
        self.is_admin = is_admin
        self.is_approved = is_approved

class Item:
    def __init__(self, name, description, address, contact_phone, contact_email, item_type, attributes):
        self.name = name
        self.description = description
        self.address = address
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.item_type = item_type
        self.attributes = attributes

class ItemType:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
