'use strict';

// initMap() runs the JavaScript file once the API has finished loading
// initMap() will CREATE the Google Map
function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 37.601773,
      lng: -122.20287,
    },
    zoom: 11,
  });


// Ask user to enter a location. 
// Geocode the location to get its coordinates and drop a marker onto the map.
document.querySelector('#geocode-address').addEventListener('click', () => {
  const userAddress = prompt('Enter a location');

  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ address: userAddress }, (results, status) => {
    if (status === 'OK') {
      // Get the coordinates of the user's location
      const userLocation = results[0].geometry.location;

      // Create a marker
      new google.maps.Marker({
        position: userLocation,
        map,
      });

      // Zoom in on the geolocated location
      map.setCenter(userLocation);
      map.setZoom(18);
    } else {
      alert(`Geocode was unsuccessful for the following reason: ${status}`);
    }
  });
})

// Create an array filled with objects that contain names and coordinates of locations.
const locations = []


}