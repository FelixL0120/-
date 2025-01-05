# /model.py

class User:
    """用户模型，包含用户的基本信息和状态。"""
    def __init__(self, username, email, address, phone, is_approved=False, is_admin=False):
        self.username = username  # 用户名
        self.email = email  # 邮箱
        self.address = address  # 地址
        self.phone = phone  # 电话
        self.is_approved = is_approved  # 是否通过审批
        self.is_admin = is_admin  # 是否为管理员

class ItemType:
    """物品类型模型，包含物品类型的名称和特定属性。"""
    def __init__(self, name, attributes=None):
        self.name = name  # 物品类型名称
        self.attributes = attributes if attributes else {}  # 物品类型特定属性

class Item:
    """物品模型，包含物品的公共信息和类型特定属性。"""
    def __init__(self, item_type, name, description, address, contact_phone, email, **kwargs):
        self.item_type = item_type  # 物品类型
        self.name = name  # 物品名称
        self.description = description  # 物品描述
        self.address = address  # 物品所在地址
        self.contact_phone = contact_phone  # 联系人手机
        self.email = email  # 联系人邮箱
        for key, value in kwargs.items():
            setattr(self, key, value)  # 设置物品类型特定属性

    def to_dict(self):
        """将物品对象转换为字典，便于存储和传输。"""
        item_dict = {
            'item_type': self.item_type.name,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'contact_phone': self.contact_phone,
            'email': self.email
        }
        item_dict.update(self.__dict__.copy().items() | kwargs.items())  # 合并特定属性
        return item_dict
