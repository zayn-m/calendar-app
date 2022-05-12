console.log(window.eventsData);

const calendarEl = document.getElementById('calendar');
const myModal = document.getElementById('create-event-modal');
const eventForm = document.getElementById('event-form');
const eventSaveBtn = document.getElementById('event-save-btn');
const selectedDateInput = document.getElementById('selected-date-input');
const eventTitle = document.getElementById('event-input');
const invalidMeetingTitleError = document.getElementById('invalid-meeting-title');
let selectedDate = '';

const calendar = new FullCalendar.Calendar(calendarEl, {
    selectable: true,
    initialView: 'dayGridMonth',
    dateClick: function(info) {
        handleClick(info.dateStr);
    },
    events: window.eventsData
  });

calendar.render();

eventSaveBtn.addEventListener('click', function(e) {
  handleSaveEvent();  
})

function handleClick(date) {
    $(myModal).modal('show');
    selectedDate = date;
    selectedDateInput.value = date;
}

function handleSaveEvent() {
    console.log('save');

    if (!eventTitle.value) {
        invalidMeetingTitleError.classList.add('visible');
        invalidMeetingTitleError.classList.remove('hidden');
        invalidMeetingTitleError.innerText = 'Title can not be empty';
        return;
    }
    eventForm.submit();
}