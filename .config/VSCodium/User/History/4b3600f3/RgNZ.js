const dateElement = document.getElementById("date");

function showTime() {
  const date = new Date();

  const options = {
    weekday: "long",
    hour: "2-digit",
    minute: "2-digit",
    day: "2-digit",
    month: "2-digit",
    year: "2-digit",
  };


  // EN date :
  
  
  const formattedDate = date.toLocaleString("en-GB", options);
  const [dayOfWeek, dateStr, time] = formattedDate.split(", ");

  dateElement.innerHTML = `${dayOfWeek}, ${dateStr} - ${time}`;


  // FR date :
  /*
  const formattedDate = date.toLocaleString("fr-FR", options);
  const [dayOfWeek, dateStr, time] = formattedDate.split(" ");

  */

  dateElement.innerHTML = `${dayOfWeek.replace(dayOfWeek[0], dayOfWeek[0].toUpperCase())}, ${time} | ${dateStr}`;
  
}

setInterval(showTime, 1000);
showTime();
