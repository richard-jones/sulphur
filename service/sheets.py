from octopus.lib import clcsv

class TotalSulphurProd(object):
    IGNORE_ROWS = [
        "Europe",
        "Eastern Europe/Central Asia",
        "North America",
        "Latin America",
        "Africa",
        "Middle East",
        "South Asia",
        "East Asia",
        "Oceania",
        "Other",
        "World Total",
        "Check",
        "IFA Figure",
        "Difference",
        ""
    ]

    VALUE_MAP = {
        "" : 0
    }

    def __init__(self, path):
        self._sheet = clcsv.ClCsv(path, from_col=1, from_row=1, ignore_blank_rows=True)

    def triples(self):
        for t in self._sheet.triples():
            if t[1].strip() in self.IGNORE_ROWS:
                continue
            nv = self.VALUE_MAP.get(t[2], t[2])
            yield t[0], t[1], nv

class TotalSulphurConsumption(object):
    IGNORE_ROWS = [
        "Europe",
        "Eastern Europe/Central Asia",
        "North America",
        "Latin America",
        "Africa",
        "Middle East",
        "South Asia",
        "East Asia",
        "Oceania",
        "Other",
        "World Total",
        "Check",
        "IFA Figure",
        "Difference",
        "",
        "*Total sulphur consumption for sulphuric acid production for phosphoric acid, metals leaching and elemental sulphur fertilizer production"
    ]

    VALUE_MAP = {
        "" : 0
    }

    def __init__(self, path):
        self._sheet = clcsv.ClCsv(path, from_col=0, from_row=1, ignore_blank_rows=True)

    def triples(self):
        for t in self._sheet.triples():
            if t[1].strip() in self.IGNORE_ROWS:
                continue
            nv = self.VALUE_MAP.get(t[2], t[2])
            yield t[0], t[1], nv

class TradeMatrix(object):
    IGNORE_ROWS = [
        "Europe",
        "Eastern Europe/Central Asia",
        "North America",
        "Latin America",
        "Africa",
        "Middle East",
        "South Asia",
        "East Asia",
        "Oceania",
        "Other",
        "World Total"
    ]

    IGNORE_COLS = [
        "World Total",
        ""
    ]

    VALUE_MAP = {
        "" : 0
    }

    def __init__(self, path):
        self._sheet = clcsv.ClCsv(path, from_col=0, from_row=0, ignore_blank_rows=True)

    def triples(self):
        for t in self._sheet.triples():
            if t[0].strip() in self.IGNORE_COLS:
                continue
            if t[1].strip() in self.IGNORE_ROWS:
                continue
            nv = self.VALUE_MAP.get(t[2], t[2])
            yield t[0], t[1], nv