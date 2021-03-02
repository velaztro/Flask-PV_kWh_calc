
///Get geolocation
let lat_form = document.getElementById("lat");
let lon_form = document.getElementById("lon");

const getLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition,error);
    lat_form.placeholder = "Locating...";
    lon_form.placeholder = "Locating...";
  } else {
    lat_form.placeholder = "Geolocation is not supported by this browser.";
    lon_form.placeholder = "Geolocation is not supported by this browser.";
  }
}

const showPosition = (position) => {
  lat_form.value = position.coords.latitude.toFixed(4);
  lon_form.value = position.coords.longitude.toFixed(4);
}

const error = () => {
  lat_form.placeholder = "Geolocation disabled";
  lon_form.placeholder = "Geolocation disabled";
}
///

function load() {
  console.log(Math.random());
};