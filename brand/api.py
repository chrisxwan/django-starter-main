from typing import Optional

from django.http import HttpRequest
from ninja import Router

from .models import Brand
from .schemas import BrandSchema, BrandsResponse

router = Router()


@router.get("/brands", response=BrandsResponse)
def get_brand_runtime_config(
    request: HttpRequest,
    count: Optional[int] = None,
) -> BrandsResponse:
    brands = Brand.objects.all()
    if count:
        brands = brands[:count]
    return BrandsResponse(brands=[BrandSchema(name=brand.name) for brand in brands])
