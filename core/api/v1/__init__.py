from ninja import Router

from .emblems.handlers import router as emblems_router
from .equipment.handlers import router as equipment_router
from .heroes.handlers import router as heroes_router
from .roles.handlers import router as roles_router

router = Router()

router.add_router('/equipment', equipment_router)
router.add_router('/roles', roles_router)
router.add_router('/emblems', emblems_router)
router.add_router('/heroes', heroes_router)
