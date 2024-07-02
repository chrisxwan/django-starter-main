from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI

from brand.api import router as brand_router

api = NinjaAPI(docs_decorator=staff_member_required)

api.add_router("/brand/", brand_router)
