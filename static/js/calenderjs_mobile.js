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

  // groupedData.forEach((daysParty, date) => {
  //   var i = 0;
  //   while (i < 3 && daysParty.length > i) { 
  //     // Include maximum of three parties per day
  //     partyInDay[Number(date.split("-")[2]) - 1][i] = partyToString(
  //       daysParty[i]
  //     );
  //     idPartyInDay[Number(date.split("-")[2]) - 1][i] = daysParty[i]["id"]
  //     i++;
  //   }
  // });

  let p_DayCounter = 0; // daycount of prev month
  let dayCounter = 1; // daycount of current month
  let n_DayCounter = 1; //daycount for next month

  for (let i = 0; i < 6; i++) {
    const dayRow = document.createElement("tr");

    for (let j = 0; j < 7; j++) {
      const dayCell = document.createElement("td");
      dayCell.classList.add("day_cell");
      const n_dayCell = document.createElement("td");
      n_dayCell.classList.add("n_day_cell");
      const p_dayCell = document.createElement("td");
      p_dayCell.classList.add("p_day_cell");
      const dateButton = document.createElement("button")
      dateButton.classList.add("date_button")
      dateButton.onclick = () => {
        console.log(dateButton.textContent)
      };

      if (i === 0 && j < currentDate.getDay()) {
        // Add empty cells for previous month's days
        p_DayCounter = daysInPrvMonth - currentDate.getDay() + j + 1;
        p_dayCell.textContent = p_DayCounter;
        dayRow.appendChild(p_dayCell);

      } else if (dayCounter <= daysInMonth) {
        // Add cells for the current month's days
        dayInDateString = createDateString(currentYear, currentMonth+1, dayCounter)
        dateButton.textContent = dayCounter;
        dayCell.appendChild(dateButton);
        dayRow.appendChild(dayCell);
        dayCounter++;

      } else {
        n_dayCell.textContent = n_DayCounter
        dayRow.appendChild(n_dayCell);
        n_DayCounter++;
      }
    }
    calendarBody.appendChild(dayRow);

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
