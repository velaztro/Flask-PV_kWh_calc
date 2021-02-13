let x = document.getElementById("demo");
  let lat_form = document.getElementById("lat");
  let lon_form = document.getElementById("lon");

  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      x.innerHTML = "Geolocation is not supported by this browser.";
    }
  }

  function showPosition(position) {
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    lat_form.value = lat.toFixed(4);
    lon_form.value = long.toFixed(4);

    /*fetch('/sign-up', {
      headers: {
        'Content-Type': 'application/json'
      },
      method: 'POST',

      body: JSON.stringify({
          "lat": lat,
          "long": long
        })
      }).then(function (response) { // At this point, Flask has printed our JSON
        return response.text();
      });*/
}