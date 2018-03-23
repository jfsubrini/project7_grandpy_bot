// jQuery script to display all the messages and the Google map.

var textUser = $('#textUser');
var address = $('#address');
var answerAddress = $('#answerAddress');
var addressGlobal = $('#addressGlobal');
var wikiHistory = $('#wikiHistory');
var answerStory = $('#answerStory');
var extractWiki = $('#extractWiki');
var linkWikipedia = $('#linkWikipedia');
var map = $('#map');
var button = $('#submit');
var loader = $('#loader');

button.on('click', function(event) {
  event.preventDefault();
  // textUser.html('<img src="../static/images/user.png" alt="Icone de l\'utilisateur" title="Icone de l\'utilisateur" width="70" height="70" id="userPic">');
  address.hide();
  wikiHistory.hide();
  map.hide();
  
  $.ajax({
    url: '/_query',
    data: $('form').serialize(),
    dataType: 'json',
    type: 'GET',
    success: function(response) {
      textUser.append(response['userText']);
      textUser.show();
      loader.fadeIn(3500).fadeOut('slow', function() {
        answerAddress.append(response['addressAnswer']);
        addressGlobal.append(response['globalAddress']);
        addressGlobal.html('<br>Regarde la jolie carte ci-dessous.');
        address.show();
        answerStory.append(response['storyAnswer']);
        extractWiki.append(response['wikiExtract']); 
        linkWikipedia.html('<a href="https://fr.wikipedia.org/wiki/openclassrooms">- En savoir plus sur Wikipedia.</a>');
        wikiHistory.show();
        map.show();
      });
    },
    error: function(error) {
      // console.log(error);    // A REVOIR
    }
  });


  var latitude = 48.8599614;
  var longitude = 2.3265614;
// var latitude = response['lat'];
// var longitude = response['lng'];
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


});
