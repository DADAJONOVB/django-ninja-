from ninja import NinjaAPI
from .schemes import ProductIn, ProductOut
from .models import Product
from django.shortcuts import get_object_or_404
from typing import List
from ninja.pagination import paginate, PageNumberPagination

api = NinjaAPI()

@api.get('/products', response=List[ProductOut])
@paginate(PageNumberPagination, page_size=10)
def products(request):
    queryset = Product.objects.all()
    return queryset


@api.post("/product")
def create_product(request, payload: ProductIn):
    print(payload)
    product = Product.objects.create(**payload.dict())
    context_data = {
        "id":product.id,
        "name":product.name,
        "price":product.price
    }
    return context_data



@api.get("/product/{product_id}", response=ProductOut)
def get_product_detail(request, product_id: int):
    employee = get_object_or_404(Product, id=product_id)
    return employee


@api.put("/product/{product_id}")
def update_product(request, product_id: int, payload: ProductOut):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@api.delete("/product/{product_id}")
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}