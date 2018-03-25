// jQuery script to display all the messages and the Google map.

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
var map = $('#map');
var button = $('#submit');
var loader = $('#loader');

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
  map.hide();
  
  $.ajax({
    url: '/_query',
    data: $('form').serialize(),
    dataType: 'json',
    type: 'GET',
    success: function(response) {
      textUser.append(response['userText']);
      textUserDiv.show();
      loader.fadeIn(3500).fadeOut('slow', function() {
        answerAddress.append(response['addressAnswer']);
        if (response['globalAddress'] != '') {
          	addressGlobal.append(response['globalAddress'] + '<br><br><span class="toMap" id="notIvory"><a href="#mapPlace">Regarde la jolie carte ci-dessous.</a></span>');
        
        //////////
			// // Sending the coordinates of the address to the Google Maps API JavaScript to design and 
	  //       // display the map with a marker and some other little things.
	  //       var latitude = response['lat'];
	  //       var longitude = response['lng'];
	  //       function initMap() {
	  //       // Create a map object and specify the DOM element for display.
	  //       // New map with map options.
	  //       var userPlace = {lat: latitude, lng: longitude};
	  //       var map = new google.maps.Map(document.getElementById('map'), {
	  //         center: userPlace,
	  //         zoom: 17,
	  //         mapTypeId: 'terrain',
	  //         scaleControl: true,
	  //         mapTypeControl: true,
	  //         mapTypeControlOptions: {
	  //           style: google.maps.MapTypeControlStyle.DROPDOWN_MENU, mapTypeIds: ['roadmap', 'hybrid'],
	  //         }
	  //       });
	  //       // Add a symbol (circle) as a marker and animation of the marker.
	  //         var marker = new google.maps.Marker({
	  //           position: userPlace,
	  //         map: map,
	  //         animation: google.maps.Animation.DROP,
	  //         icon: { 
	  //             path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
	  //             scale: 6
	  //           }
	  //         // icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"
	  //         });
	  //         // Add an info window that pop up when the mouse mover over.
	  //         var infoWindow = new google.maps.InfoWindow({
	  //           content: "<h4>C'est ici !</h4>"
	  //         });
	  //         marker.addListener('mouseover', function(){
	  //           infoWindow.open(map, marker);
	  //         });
	  //       }

        	map.show();
        }
        ////////////////////
        address.show();
        answerStory.append(response['storyAnswer']);
        if (response['wikiExtract'] != '') {
          extractWiki.append(response['wikiExtract']);
          linkWikipedia.append('<a href="https://fr.wikipedia.org/wiki/?curid=' + response['pageid'] + '">- En savoir plus sur Wikipedia.</a>');
          wikiHistory.show();
        } else {
          if (response['globalAddress'] != '') {
            wikiHistory.show();
          }
        }
        $('input:text').val('')


      });
    },
    error: function(error) {
      // console.log(error);    // A REVOIR
    }
  });

});
