from typing import List

from ninja import Schema


class BrandSchema(Schema):
    name: str


class BrandsResponse(Schema):
    brands: List[BrandSchema]
