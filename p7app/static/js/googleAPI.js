// JavaScript script to call the Google Maps API JavaScript to display the right map.

var latitude = 48.8599614;
var longitude = 2.3265614;

function initMap() {
// Create a map object and specify the DOM element for display.
// New map with map options.
var userPlace = {lat: latitude, lng: longitude };
var map = new google.maps.Map(document.getElementById('map'), {
  center: userPlace,
  zoom: 17,
  mapTypeId: 'terrain',
  scaleControl: true,
  mapTypeControl: true,
  mapTypeControlOptions: {
  	style: google.maps.MapTypeControlStyle.DROPDOWN_MENU, mapTypeIds: ['roadmap', 'hybrid'],
  }
});
// Add a symbol (circle) as a marker and animation of the marker.
	var marker = new google.maps.Marker({
		position: userPlace,
	map: map,
	animation: google.maps.Animation.DROP,
	icon: {	
      path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
      scale: 6
    }
	// icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"
	});
	// Add an info window that pop up when the mouse mover over.
	var infoWindow = new google.maps.InfoWindow({
		content: "<h4>C'est ici !</h4>"
	});
	marker.addListener('mouseover', function(){
		infoWindow.open(map, marker);
	});
}
	 