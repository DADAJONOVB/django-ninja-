from ninja import ModelSchema, Schema
from .models import Category, Product


class ProductIn(Schema):
    name: str
    category_id: int
    price: int
    is_delivery: bool

class ProductOut(ModelSchema):
    class Config:
        model = Product
        model_fields = '__all__'