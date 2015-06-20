/**
 *
 * Created by gmoselle on 6/19/15.
 */
$(function () {
    multibar();
});

function multibar() {
    d3.json("/bing_counts", function (error, data) {
        console.log('inside multi bar')
        nv.addGraph(function () {
            var chart = nv.models.multiBarHorizontalChart()
                .x(function (d) {
                    return d.label
                })
                .y(function (d) {
                    return d.value
                })
                .margin({top: 30, right: 20, bottom: 50, left: 175})
                .showValues(true)           //Show bar value next to each bar.
                .valueFormat(d3.format(',f'))
                .tooltips(true)             //Show tooltips on hover.
                .showControls(true);        //Allow user to switch between "Grouped" and "Stacked" mode.

            chart.yAxis
                .tickFormat(d3.format(',f'));

            //chart.xAxis
            //    .tickFormat(d3.format(',f'));

            d3.select('#multibar svg')
                .datum(data)
                .call(chart);

            nv.utils.windowResize(chart.update);

            return chart;
        });
    });
}