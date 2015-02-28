# overrides for the webapp deployment
DEBUG = True
PORT = 5021
SSL = False
THREADED = True

# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "sulphur"
ELASTIC_SEARCH_VERSION = "1.4.2"

# Classes from which to retrieve ES mappings to be used in this application
ELASTIC_SEARCH_MAPPINGS = [
    "service.dao.ProductionDAO",
    "service.dao.ConsumptionDAO",
    "service.dao.TradeDAO"
]

# Query route configuration
QUERY_ROUTE = {
    "query" : {                            # the URL route at which it is mounted
        "prod" : {                     # the URL name for the index type being queried
            "auth" : False,                     # whether the route requires authentication
            "role" : None,                      # if authenticated, what role is required to access the query endpoint
            "filters" : [],                     # names of the standard filters to apply to the query
            "dao" : "service.dao.ProductionDAO"       # classpath for DAO which accesses the underlying ES index
        },
        "consumption" : {                     # the URL name for the index type being queried
            "auth" : False,                     # whether the route requires authentication
            "role" : None,                      # if authenticated, what role is required to access the query endpoint
            "filters" : [],                     # names of the standard filters to apply to the query
            "dao" : "service.dao.ConsumptionDAO"       # classpath for DAO which accesses the underlying ES index
        }
    }
}

CLIENTJS_PROD_QUERY_ENDPOINT = "/query/prod"
CLIENTJS_CONSUMPTION_QUERY_ENDPOINT = "/query/consumption"

AUTOCOMPLETE_TERM = {
    "country" : {
        "filter" : {
            "country" : {
                "start_wildcard" : True,
                "end_wildcard" : True
            }
        },
        "facet" : "country.exact",
        "input_filter" : lambda x : x.strip().lower(),
        "default_size" : 10,
        "max_size" : 25,
        "dao" : "service.dao.ProductionDAO"
    }
}