var jobsData = (function () {
    var jobsData = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "http://localhost:5000/api-Jobs",
        'dataType': "json",
        'success': function (data) {
            jobsData = data;
        }
    });
    return jobsData;
})();

// instantiate d3plus
var visualization = d3plus.viz()
  .container("#viz")  // container DIV to hold the visualization
  .data(jobsData)  // data to use with the visualization
  .type("tree_map")   // visualization type
  .id("initial")         // key for which our data is unique on
  .size("jobs")      // sizing of blocks
  .legend({"size": 40})  // change the size of the label in bottom of the visualization
  .time({
        "value": "year",
        "solo": 2012
      })
  .ui([
      {
        "method" : "size",
        "value"  : [ "jobs" , "totalEmployees", "avgSalary" ]
      },
      {
        "method" : "color",
        "value"  : [ "State" , "jobs" ]
      }
  ])
  .labels({"align": "left", "valign": "top"})  //Show percent label
  .title({"total": true})
  .footer({                                    // put a footer write
      "link": "http://dataviva.info/en/",
      "jobs": "Click here to go to DataViva and see much more."
    })
  .tooltip(["State", "jobs", "totalEmployees", "Total Salary", "avgSalary"])
  .draw();            // finally, draw the visualization!
