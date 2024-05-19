function getCurrentDate() {
  const cDate = new Date();
  return [cDate.getFullYear(), cDate.getMonth(), cDate.getDate()];
}

// Initial day, month, year
var [currentYear, currentMonth, currentDate] = getCurrentDate();

function partyToString(obj) {
  return (
    obj["origin_name"] + " → " + obj["destination_name"] + " @ " + String(obj["time"]).slice(0,2)
  );
}

function createDateString(year, month, date) {
  if (month < 10) {
    month = "0" + String(month)
  } else {
    month = String(month)
  }

  if (date < 10) {
    date = "0" + String(date)
  } else {
    date = String(date)
  }

  return String(year) + "-" + month + "-" + date
}

// Function to update the calendar
function updateCalendar() {
  const calendarBody = document
    // .getElementById("calendar")
    .getElementsByTagName("tbody")[0];

  const currentDate = new Date(currentYear, currentMonth, 1);
  //Date(year, month, day)
  //day before Next month -> last day in month
  const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
  //day before this month -> last day in prev month
  const daysInPrvMonth = new Date(currentYear, currentMonth, 0).getDate();
  // Clear previous content
  calendarBody.innerHTML = "";

  var partyInDay = new Array( 
    // Store up to three party in each day
    // Index: Each date of month
    // Element: Array length of 3 holding taxi party string representations
    new Date(currentYear, currentMonth + 1, 0).getDate() + 1
  );

  var idPartyInDay = new Array(
    // Index: Each date of month
    // Element: id of each party corresponding to party in partyInDay array
    new Date(currentYear, currentMonth + 1, 0).getDate() + 1
  );

  for (var i = 0; i < partyInDay.length; i++) {
    partyInDay[i] = new Array(3);
    idPartyInDay[i] = new Array(3);
  }

  groupedData.forEach((daysParty, date) => {
    var i = 0;
    while (i < 3 && daysParty.length > i) { 
      // Include maximum of three parties per day
      partyInDay[Number(date.split("-")[2]) - 1][i] = partyToString(
        daysParty[i]
      );
      idPartyInDay[Number(date.split("-")[2]) - 1][i] = daysParty[i]["id"]
      i++;
    }
  });

  let p_DayCounter = 0;
  // Populate the calendar
  let dayCounter = 1;
  //day counterfor nextmonth
  let n_DayCounter = 1;
  for (let i = 0; i < 6; i++) {
    //Row for day
    const dayRow = document.createElement("tr");
    //Row for content
    const contentRow = document.createElement("tr");

    for (let j = 0; j < 7; j++) {
      const dayCell = document.createElement("td");
      dayCell.classList.add("day_cell");
      const contentCell = document.createElement("td");
      contentCell.classList.add("content_cell");
      const n_dayCell = document.createElement("td");
      n_dayCell.classList.add("n_day_cell");
      const p_dayCell = document.createElement("td");
      p_dayCell.classList.add("p_day_cell");
      const linkToDailyParty = document.createElement("a");
      linkToDailyParty.classList.add("calendar_anchor")
      const contentCellLinkToDailyParty = document.createElement("a");
      contentCellLinkToDailyParty.classList.add("calendar_anchor")

      if (i === 0 && j < currentDate.getDay()) {
        // Add empty cells for previous month's days
        p_DayCounter = daysInPrvMonth - currentDate.getDay() + j + 1;
        linkToDailyParty.href = "/taxiparty/daily/" + createDateString(currentYear, currentMonth, p_DayCounter);
        linkToDailyParty.textContent = p_DayCounter;
        p_dayCell.appendChild(linkToDailyParty);
        dayRow.appendChild(p_dayCell);
        contentRow.appendChild(contentCell);
      } else if (dayCounter <= daysInMonth) {
        // Add cells for the current month's days
        dayInDateString = createDateString(currentYear, currentMonth+1, dayCounter)
        linkToDailyParty.href = "/taxiparty/daily/" + dayInDateString;
        contentCellLinkToDailyParty.href = "/taxiparty/daily/" + dayInDateString;
        linkToDailyParty.textContent = dayCounter;
        dayCell.appendChild(linkToDailyParty);
        contentCell.appendChild(contentCellLinkToDailyParty)
        for (let k = 0; k < 3; k++) {
          if (partyInDay[dayCounter - 1][k]) {
              const partyElement = document.createElement("div");
              const linkToTaxiParty = document.createElement("a")
              linkToTaxiParty.href = "/taxiparty/" + String(idPartyInDay[dayCounter - 1][k]) + "/"
              linkToTaxiParty.textContent = partyInDay[dayCounter - 1][k];
              partyElement.appendChild(linkToTaxiParty);
              contentCellLinkToDailyParty.appendChild(partyElement);
          }
        }
        var numOfParty = 0
        if (groupedData.get(dayInDateString)) {
          numOfParty = groupedData.get(dayInDateString).length
        }
        if (numOfParty > 3) {
          const partyElement = document.createElement("div");
          partyElement.textContent = "..." + String(numOfParty - 3) + " more";
          contentCellLinkToDailyParty.appendChild(partyElement);
        }
        
        dayRow.appendChild(dayCell);
        contentRow.appendChild(contentCell);
        dayCounter++;
      } else {
        linkToDailyParty.href = "/taxiparty/daily/" + createDateString(currentYear, currentMonth+2, n_DayCounter);
        linkToDailyParty.textContent = n_DayCounter;
        n_dayCell.appendChild(linkToDailyParty);
        dayRow.appendChild(n_dayCell);
        contentRow.appendChild(contentCell);
        n_DayCounter++;
      }
    }
    calendarBody.appendChild(dayRow);

    calendarBody.appendChild(contentRow);
    if (dayCounter > daysInMonth) {
      break;
    }
  }

  // Update the displayed month and year
  document.getElementById("currentMonthYear").textContent =
    new Intl.DateTimeFormat("en-EN", {
      year: "numeric",
      month: "long",
    }).format(currentDate);
    console.log(document.getElementById("currentMonthYear").textContent)
}

// Function to navigate to the previous month
function prevMonth() {
  currentMonth--;
  if (currentMonth < 1) {
    currentMonth = 11;
    currentYear--;
  }
  get_monthinfo(currentYear, currentMonth + 1, updateCalendar);
}

// Function to navigate to the next month
function nextMonth() {
  currentMonth++;
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  get_monthinfo(currentYear, currentMonth + 1, updateCalendar);
}
