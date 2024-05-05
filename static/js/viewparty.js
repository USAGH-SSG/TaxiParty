// Group objects by date
var groupedData = new Map();

function get_monthinfo(year, month, callback) {
  groupedData = new Map();
  if (year == 0 && month == 0) {
    var today = new Date();
    year = today.getFullYear();
    month = today.getMonth() + 1;
  }
  var partyUrl = "/taxiparty/month/" + String(year) + "-";
  if (month < 10) {
    month = "0" + String(month);
  } else {
    month = String(month);
  }
  console.log(partyUrl);
  partyUrl = partyUrl + month;
  console.log(partyUrl);

  $.ajax({
    type: "GET",
    url: partyUrl,
    dataType: "json",
    success: function (result) {
      result.forEach(function (item) {
        var date = item.date;
        if (!groupedData.has(date)) {
          groupedData.set(date, []);
        }
        groupedData.get(date).push(item);
      });

      console.log(groupedData); // Log the grouped data to inspect its structure
      if (callback && typeof callback === "function") {
        callback();
      } else {
        console.error("Invalid callback function provided.");
      }
    },
    error: function () {
      alert("Error occurred while fetching data.");
    },
  });
}
