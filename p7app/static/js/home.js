// jQuery and pure JavaScript script to display all the messages and the Google map of the wanted place.

// Creating jQuery objects with id from home.html.
var textUserDiv = $('#textUserDiv');
var textUser = $('#textUser');
var address = $('#address');
var answerAddress = $('#answerAddress');
var addressGlobal = $('#addressGlobal');
var wikiHistory = $('#wikiHistory');
var answerStory = $('#answerStory');
var extractWiki = $('#extractWiki');
var linkWikipedia = $('#linkWikipedia');
var maps = $('#map');
var button = $('#submit');
var loader = $('#loader');
// Creating variables for the Google Map. 
var userPlace;
var mapGoogle;

// JavaScript script to call the Google Maps API JavaScript and initiate a map.
function initMap() {
  // Create a map object and specify the DOM element for display.
  // New map initiated, with some options, waiting for data updating.
  mapGoogle = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 0.0, lng: 0.0},
    zoom: 17,
    mapTypeId: 'terrain',
    scaleControl: true,
    mapTypeControl: true,
    mapTypeControlOptions: {
      style: google.maps.MapTypeControlStyle.DROPDOWN_MENU, mapTypeIds: ['roadmap', 'hybrid'],
    }
  });
}
  
// Event listener (triggers when clicking the input submit button).
button.on('click', function(event) {
  event.preventDefault();  
  textUser.text('');
  address.hide();
  answerAddress.text('');
  addressGlobal.text('');
  wikiHistory.hide();
  answerStory.text('');
  extractWiki.text('');
  linkWikipedia.text('');
  maps.hide();
  
  $.ajax({
    url: '/_query',
    data: $('form').serialize(),
    dataType: 'json',
    type: 'GET',
    success: function(response) {
      textUser.append(response['userText']);
      textUserDiv.show();
      loader.delay(300).fadeIn(3000).fadeOut('slow', function() {
        answerAddress.append(response['addressAnswer']);
        if (response['globalAddress'] != '') {
          	addressGlobal.append(response['globalAddress'] + '<br><br><span class="toMap" id="notIvory"><a href="#mapPlace">Regarde la jolie carte ci-dessous.</a></span>');
            // Sending the coordinates of the address to the Google Maps API JavaScript 
            // to display the right map.
            userPlace = {lat: response['lat'], lng: response['lng']};
            mapGoogle.setCenter(userPlace); 
            // Add a symbol (arrow) as a marker and animation of the marker (drop).
            var marker = new google.maps.Marker({
              position: userPlace,
              map: mapGoogle,
              animation: google.maps.Animation.DROP,
              icon: { 
                path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
                scale: 6
              }
            });
            // Add an info window that pop up when the mouse mover over.
            var infoWindow = new google.maps.InfoWindow({
              content: "<h4>C'est ici !</h4>"
            });
            marker.addListener('mouseover', function(){
              infoWindow.open(map, marker);
            });
        	  maps.show();
        }
        address.show();
        answerStory.append(response['storyAnswer']); 
        // Giving the story from Wikipedia if there is any extract content.
        if (response['wikiExtract'] != '') {
          extractWiki.append(response['wikiExtract']);
          // Link to the right Wikipedia pageid.
          linkWikipedia.append('<a href="https://fr.wikipedia.org/wiki/?curid=' + response['pageid'] + '">- En savoir plus sur Wikipedia.</a>');
          wikiHistory.show();
        } else {
          if (response['globalAddress'] != '') {
            wikiHistory.show();
          }
        }
        // Cleaning the input from the previous user sentence.
        $('input:text').val('')
      });
    },
    error: function(error) {
      console.log(error);
    }
  });
});
