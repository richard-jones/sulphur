jQuery(document).ready(function($) {

    /****************************************************************
     * Application Reportview Theme
     *****************************
     */

    function customReportViewClosure(height) {
        function theReportview(options) {
            /*****************************************
             * overrides must provide the following classes and ids
             *
             * class: reportview - main div in which the reportview functionality goes, which should contain an svg element directly
             *
             * Should respect the following configs
             *
             * options.debug - is this a debug enabled reportview.  If so, put a debug textarea somewhere
             */

            // the reportview object to be appended to the page
            var thereportview = '<div class="reportview" style="height: ' + height + 'px"><svg></svg>'
            if (options.debug) {
                thereportview += "<div class='reportview_debug'><textarea style='width: 100%; height: 200px'></textarea></div>"
            }
            thereportview += '</div>';
            return thereportview
        }
        return theReportview
    }

    function updateReport() {

        // get the filter from the country autocomplete box
        var filter = undefined;
        var vals = $("#ac_country").select2("val");
        if (vals.length > 0) {
            filter = {"terms": {"country.exact": vals}};
        }
        if (!filter) {
            $('#country-year').html("<strong>Start by choosing some countries in the box above</strong>");
            return;
        }

        // get the start and end years of the report
        var from = $("#from").select2("val");
        var to = $("#to").select2("val");

        function dataSeriesFunction(callback) {
            var query = {
                "query" : {
                    "bool" : {
                        "must" : [
                            {
                                "range" : {
                                    "year" : {
                                        "gte" : from,
                                        "lte" : to
                                    }
                                }
                            },
                            filter
                        ]
                    }
                },
                "size" : 0,
                "aggs": {
                    "by_country": {
                        "terms": {
                            "field": "country.exact"
                        },
                        "aggs": {
                            "con": {
                                "sum": {
                                    "field": "consumption"
                                }
                            },
                            "prod": {
                                "sum": {
                                    "field": "production"
                                }
                            }
                        }
                    }
                }
            };

            function convertToDataSeries(rawdata, results) {

                var prod_series = {key : "Production", values : []};
                var con_series = {key : "Consumption", values : []};

                var countries = rawdata.aggregations.by_country.buckets;
                for (var i = 0; i < countries.length; i++) {
                    var country = countries[i];
                    var country_name = country.key;
                    var production = country.prod.value;
                    var consumption = country.con.value;
                    prod_series.values.push({label : country_name, value: production});
                    con_series.values.push({label : country_name, value: consumption});
                }

                // finally, hit the callback
                callback([prod_series, con_series])
            }

            doElasticSearchQuery({
                success: convertToDataSeries,
                search_url: octopus.config.conprod_query_endpoint,
                queryobj: query,
                datatype: "jsonp"
            })
        }

        function adjustCss(options, context) {
            // how many years do we need to display?
            var country_count = options.data_series.length;
            var year_count = 0;
            for (var i = 0; i < options.data_series.length; i++) {
                var country = options.data_series[i];
                var years = country.values.length;
                if (years > year_count) { year_count = years }
            }

            // calculate the new graph heights
            var fixed_aspects = 70;
            var country_allowance = 20;

            var report_height = fixed_aspects + (year_count * (country_count * country_allowance));
            var container_height = report_height + 50;

            $("#country-year").css("height", container_height + "px");
            $("#country-year .reportview").css("height", report_height + "px");
        }

        // render the report itself
        $('#country-year').empty();
        $('#country-year').report({
            type: 'horizontal_multibar',
            data_function: dataSeriesFunction,
            render_the_reportview: customReportViewClosure(100),
            horizontal_multibar_margin_left: 100,
            pre_render_callback: adjustCss
        });
    }

    // first bind select2 to the publisher autocomplete

    octopus.esac.bindTermAutocomplete({
        selector : "#ac_country",
        minimumInputLength : 1,
        placeholder :"Choose countries to display",
        type : "country",
        allow_clear : true,
        multiple: true
    });

    // sort out the options to appear in each select box
    var options = "";
    for (var i = 2008; i <= 2030; i++) {
        options += '<option value="' + i + '">' + i + '</option>'
    }

    $("#from").html(options)
        .select2()
        .change(function (event) {
            updateReport()
        });

    $("#to").html(options)
        .select2()
        .change(function (event) {
            updateReport()
        });

    $("#ac_country").change(function (event) {
        updateReport()
    });
});
