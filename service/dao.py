from octopus.modules.es import dao
from octopus.core import app

class ProductionDAO(dao.ESDAO):
    __type__ = 'production'

class ConsumptionDAO(dao.ESDAO):
    __type__ = 'consumption'

class TradeDAO(dao.ESDAO):
    __type__ = 'trade'

class ConProdDAO(dao.ESDAO):
    __type__ = "production,consumption"
