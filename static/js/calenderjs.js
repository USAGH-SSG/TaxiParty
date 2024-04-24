window.onload = function() {
    updateCalendar();
}

function getCurrentDate(){
    const cDate = new Date();
    return {
        currentYear: cDate.getFullYear(),
        currentMonth: cDate.getMonth(),
        currentDate: cDate.getDate(),
    };
}

// Initial day, month, year
let {currentYear, currentMonth, currentDate} = getCurrentDate();

//ex
let requestArray = new Array(new Date(currentYear, currentMonth + 1, 0)).fill("X");
//requestArray[23] = "0800, Wa mart -> Pyeongtaek St.";
//requestArray[27] = "2000, Pyeongtaek St. -> Wa mart";




// Function to update the calendar
function updateCalendar() {
    //For viewing party
    for (const requestTime in groupedData) {
        const dates = requestTime.date.parse("-")[0];
        console.log(dates);
    }

    const calendarBody = document.getElementById('calendar').getElementsByTagName('tbody')[0];
    const currentDate = new Date(currentYear, currentMonth, 1);
    //Date(year, month, day)
    //day before Next month -> last day in month
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    //day before this month -> last day in prev month
    const daysInPrvMonth = new Date(currentYear, currentMonth, 0).getDate();
    // Clear previous content
    calendarBody.innerHTML = '';

    let p_DayCounter = 0;
    // Populate the calendar
    let dayCounter = 1;
    //day counterfor nextmonth
    let n_DayCounter = 1;
    for (let i = 0; i < 6; i++) {
        //Row for day
        const dayRow = document.createElement('tr');
        //Row for content
        const contentRow = document.createElement('tr');

        for (let j = 0; j < 7; j++) {
            const dayCell = document.createElement('td');
            dayCell.classList.add('day_cell');
            const contentCell = document.createElement('td');
            contentCell.classList.add('content_cell');
            const n_dayCell = document.createElement('td');
            n_dayCell.classList.add('n_day_cell');
            const p_dayCell = document.createElement('td');
            p_dayCell.classList.add('p_day_cell');

            if (i === 0 && j < currentDate.getDay()) {
                // Add empty cells for previous month's days
                p_DayCounter = daysInPrvMonth - currentDate.getDay() + j + 1;
                p_dayCell.textContent = p_DayCounter;
                dayRow.appendChild(p_dayCell);
                contentRow.appendChild(contentCell);
            } else if (dayCounter <= daysInMonth) {
                // Add cells for the current month's days
                dayCell.textContent = dayCounter;
                contentCell.textContent = requestArray[dayCounter];
                dayRow.appendChild(dayCell);
                contentRow.appendChild(contentCell);
                dayCounter++;
            }
            else {
                n_dayCell.textContent = n_DayCounter;
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
    document.getElementById('currentMonthYear').textContent = new Intl.DateTimeFormat('en-EN', {
        year: 'numeric',
        month: 'long'
    }).format(currentDate);
}

// Function to navigate to the previous month
function prevMonth() {
currentMonth--;
if (currentMonth < 0) {
currentMonth = 11;
currentYear--;
}
updateCalendar();
}

// Function to navigate to the next month
function nextMonth() {
currentMonth++;
if (currentMonth > 11) {
currentMonth = 0;
currentYear++;
}
updateCalendar();
}

// Initial calendar rendering
updateCalendar();