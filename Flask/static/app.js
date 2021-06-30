function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(locationSucced, locationError);
  } else {
    alert("Your browser does not support location");
  }
}

function locationSucced(position) {
  console.log("Current location", position);
  let data = {
    lat: position.coords.latitude,
    lon: position.coords.longitude,
  };
  $.ajax({
    url: "/api/weather",
    type: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (res) {
      console.log("Server says: ", res);
      console.log("Currente temp: ", res.current.temp);
      console.log("Curres desc: ",res.current.weather[0].description);
      document.getElementById("regionWeather").innerHTML="Time zone: "+res.timezone;
      document.getElementById("tempWeather").innerHTML="Temperature: "+res.current.temp;
      document.getElementById("descWeather").innerHTML="Description: "+res.current.weather[0].description;

    },
    error: function (err) {
      console.error("Error getting weather", err);
    },
  });
}

function locationError() {
  console.error("Error getting location");
}

function init() {
  console.log("Weather page!");
  getLocation();
}

window.onload = init;
