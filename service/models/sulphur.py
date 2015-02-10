from octopus.lib import dataobj
from service import dao

class Production(dataobj.DataObj, dao.ProductionDAO):
    @property
    def year(self):
        return self._get_single("year", coerce=self._int())

    @year.setter
    def year(self, value):
        self._set_single("year", value, coerce=self._int())

    @property
    def country(self):
        return self._get_single("country", coerce=self._utf8_unicode())

    @country.setter
    def country(self, value):
        self._set_single("country", value, coerce=self._utf8_unicode())

    @property
    def production(self):
        return self._get_single("production", coerce=self._int())

    @production.setter
    def production(self, value):
        self._set_single("production", value, coerce=self._int())


class Consumption(dataobj.DataObj, dao.ConsumptionDAO):
    @property
    def year(self):
        return self._get_single("year", coerce=self._int())

    @year.setter
    def year(self, value):
        self._set_single("year", value, coerce=self._int())

    @property
    def country(self):
        return self._get_single("country", coerce=self._utf8_unicode())

    @country.setter
    def country(self, value):
        self._set_single("country", value, coerce=self._utf8_unicode())

    @property
    def consumption(self):
        return self._get_single("consumption", coerce=self._int())

    @consumption.setter
    def consumption(self, value):
        self._set_single("consumption", value, coerce=self._int())

class Trade(dataobj.DataObj, dao.TradeDAO):
    @property
    def year(self):
        return self._get_single("year", coerce=self._int())

    @year.setter
    def year(self, value):
        self._set_single("year", value, coerce=self._int())

    @property
    def origin(self):
        return self._get_single("origin", coerce=self._utf8_unicode())

    @origin.setter
    def origin(self, value):
        self._set_single("origin", value, coerce=self._utf8_unicode())

    @property
    def target(self):
        return self._get_single("target", coerce=self._utf8_unicode())

    @target.setter
    def target(self, value):
        self._set_single("target", value, coerce=self._utf8_unicode())

    @property
    def amount(self):
        return self._get_single("amount", coerce=self._float())

    @amount.setter
    def amount(self, value):
        self._set_single("amount", value, coerce=self._float())