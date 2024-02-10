function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var data = {
        location: $('#uiLocations').val(),
        house_type: $('input[name="house_type"]:checked').val(),
        distance: $('#distance').val(),
        bedroom: $('input[name="bedroom"]:checked').val(),
        bathroom: $('input[name="bathroom"]:checked').val(),
        car: $('input[name="car"]:checked').val(),
        landsize: $('#landsize').val(),
        buildingarea: $('#buildingarea').val(),
        yearbuilt: $('#yearbuilt').val(),
        lattitude: $('#lattitude').val(),
        longtitude: $('#longtitude').val()
    };


    var url = "http://127.0.0.1:5000/predict_home_price"; 

    var queryString = $.param(data); // Converts the data object to a query string suitable for application/x-www-form-urlencoded

    $.post('http://127.0.0.1:5000/predict_home_price', queryString, function(response) {
        $('#uiEstimatedPrice h2').html(response.estimated_price + " USD");
    }).fail(function() {
        $('#uiEstimatedPrice h2').html("Failed to get the estimated price. Please try again.");
    });
}
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; 
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
window.onload = onPageLoad;

