console.log("app.js working");


$(document).ready(function () {
  $("#addTaskButton").click(function () {
    let task = $("#taskInput").val();
    if (task != "") {
      $('#tasks').addClass('column');
      $('#tasks').append("<input name ='task-item' id='task-item' class='input is-rounded my-1' type='text' maxlength='30' value='" + task + "' />");
    }
  });
});

$(document).ready(function () {
  const events = JSON.parse(document.getElementById('events-data').textContent);

  updateEvents(events);

  $("#filter").on('input', function () {
    var inputVal = $(this).val();
    console.log(inputVal);
    $("#events").empty();
    var filtered_events = [];

    console.log(events)
    for (var i in events) {
      if (events[i].name.includes(inputVal) || events[i].description.includes(inputVal)) {
        filtered_events.push(events[i])
      }
    }
    updateEvents(filtered_events);
  });
});

function updateEvents(events) {
  for (var event of events) {
    var truncate;
    if (event.name.length < 26) {
      truncate = "truncate-with-ellipsis2"
    } else {
      truncate = "truncate-with-ellipsis"
    }
    var htmlContent = `
            <div class="column is-one-third">
                <a class="event" href="/event/${event.id}">
                    <div class="webSection box is-rounded closerCards">
                        <p class="title is-size-4 webSectionText">${event.name}</p>
                        <p class="m-1"> <i class="fas fa-user"></i> ${event.user}</p>
                        <p class="m-1"> <i class="fa-regular fa-calendar-days"></i> ${event.time} on ${event.date}</p>
                        <div class="webSectionText">
                                <p class="${truncate}">${event.description}</p>
                            <br>
                        </div>
                    </div>
                </a>
            </div>
        `;
    // Insert the HTML content into the element with ID "#events"
    $("#events").append(htmlContent);
  }
}



// document.addEventListener('DOMContentLoaded', () => {
//   var myForm = document.getElementById('filterEventForm');
//   var filter = document.getElementById('filter');
//   filter.addEventListener('input', () => {
//     document.getElementById('filterEventForm').submit();
//   });
// });


document.addEventListener('DOMContentLoaded', () => {


  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function openTaskModal($el, id) {
    $el.classList.add('is-active');
    console.log(id)
    document.getElementById('selector').value = id;
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);
    console.log($trigger)
    $trigger.addEventListener('click', () => {
      if ($trigger.id == "taskButton") {
        openTaskModal($target, $trigger.taskId)
      } else {
        openModal($target);
      }
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
      closeAllModals();
    }
  });
});


document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach(el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});

document.addEventListener('DOMContentLoaded', () => {
  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;

    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});
