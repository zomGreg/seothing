/**
 *
 * Created by gmoselle on 6/18/15.
 */

$(function () {
    console.log('jquery is working!')
    discreteBar();
});

function discreteBar() {
    console.log('inside discrete bar')
    var width = 1260; // chart width
    var height = 400; // chart height

    d3.json("/discrete", function (error, data) {
        nv.addGraph(function () {
            var chart = nv.models.discreteBarChart()
                .x(function (d) {
                    return d.label
                })
                .y(function (d) {
                    return d.value
                })
                .staggerLabels(true)
                .tooltips(false)
                .showValues(true)

            d3.select('#discretebar svg')
                .datum(data)
                .transition().duration(500)
                .call(chart)
            ;

            nv.utils.windowResize(chart.update);

            return chart;
        });
    })
}
