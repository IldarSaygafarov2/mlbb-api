from ninja import NinjaAPI

from core.api.v1 import router as v1_router


api = NinjaAPI()

api.add_router('v1/', v1_router)
