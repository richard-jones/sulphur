from octopus.core import initialise
initialise()

from service import sheets, models


tsp = sheets.TotalSulphurProd("/home/richard/Dropbox/Personal/Sulphur/TotalSulphurProd.csv")
for year, country, prod in tsp.triples():
    print "production", year, country, prod
    obj = models.Production()
    obj.year = year
    obj.country = country
    obj.production = prod
    obj.save()

tsc = sheets.TotalSulphurConsumption("/home/richard/Dropbox/Personal/Sulphur/TotalSulphurConsumption.csv")
for year, country, con in tsc.triples():
    print "consumption", year, country, con
    obj = models.Consumption()
    obj.year = year
    obj.country = country
    obj.consumption = con
    obj.save()

tm = sheets.TradeMatrix("/home/richard/Dropbox/Personal/Sulphur/TradeMatrix2009.csv")
for fr, to, amt in tm.triples():
    print "trade 2009", fr, to, amt
    obj = models.Trade()
    obj.year = 2009
    obj.origin = fr
    obj.target = to
    obj.amount = amt
    obj.save()

tm = sheets.TradeMatrix("/home/richard/Dropbox/Personal/Sulphur/TradeMatrix2010.csv")
for fr, to, amt in tm.triples():
    print "trade 2010", fr, to, amt
    obj = models.Trade()
    obj.year = 2010
    obj.origin = fr
    obj.target = to
    obj.amount = amt
    obj.save()

tm = sheets.TradeMatrix("/home/richard/Dropbox/Personal/Sulphur/TradeMatrix2011.csv")
for fr, to, amt in tm.triples():
    print "trade 2011", fr, to, amt
    obj = models.Trade()
    obj.year = 2011
    obj.origin = fr
    obj.target = to
    obj.amount = amt
    obj.save()


tm = sheets.TradeMatrix("/home/richard/Dropbox/Personal/Sulphur/TradeMatrix2012.csv")
for fr, to, amt in tm.triples():
    print "trade 2012", fr, to, amt
    obj = models.Trade()
    obj.year = 2012
    obj.origin = fr
    obj.target = to
    obj.amount = amt
    obj.save()

tm = sheets.TradeMatrix("/home/richard/Dropbox/Personal/Sulphur/TradeMatrix2013.csv")
for fr, to, amt in tm.triples():
    print "trade 2013", fr, to, amt
    obj = models.Trade()
    obj.year = 2013
    obj.origin = fr
    obj.target = to
    obj.amount = amt
    obj.save()
