// Group objects by date
var groupedData = {};

function get_monthinfo() {
    $.ajax({
        type: 'GET',
        url: '/taxiparty/month/2024-04',
        dataType: 'json',
        success: function(result) {

            result.forEach(function(item) {
                var date = item.date;
                if (!groupedData[date]) {
                    groupedData[date] = [];
                }
                groupedData[date].push(item);
            });

            console.log(groupedData); // Log the grouped data to inspect its structure
            // Display the grouped JSON response in HTML
            $("#data").html("<pre>" + JSON.stringify(groupedData, null, 2) + "</pre>");
            dataArr = JSON.stringify(groupedData, null, 2).slice();
        },
        error: function() {
            alert("Error occurred while fetching data.");
        }
    });
}