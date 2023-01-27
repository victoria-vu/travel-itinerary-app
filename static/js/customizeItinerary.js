'use strict';

function initMap() {
    let map = new google.maps.Map(document.querySelector("#map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}