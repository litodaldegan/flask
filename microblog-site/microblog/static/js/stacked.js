var jobsData = (function () {
    var jobsData = null;
    $.ajax({
        async: false,
        type: "GET",
        url: "http://localhost:5000/api-Jobs",
        dataType: "json",
        'success': function (data) {
            jobsData = data;
        }
    });
    return jobsData;
})();

console.log(jobsData);

// instantiate d3plus
  var visualization = d3plus.viz()
    .container("#viz")  // container DIV to hold the visualization
    .data(jobsData)  // data to use with the visualization
    .type("stacked")    // visualization type
    .id("initial")         // key for which our data is unique on
    .text("initial")       // key to use for display text
    .y("jobs")         // key to use for y-axis
    .x("year")          // key to use for x-axis
    .time("year")       // key to use for time
    .draw()             // finally, draw the visualization!