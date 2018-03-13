// jQuery script to display all the messages, and the map

var textInput = $('#textUser');
var address = $('#address');
var wikiHistory = $('#wikiHistory');
var map = $('#map');  
var button = $('#submit');
var loader = $('#loader');

button.on('click', function(event) {
  event.preventDefault();
  textInput.hide();
  textInput.empty();
  address.hide();
  // address.empty();
  wikiHistory.hide();
  // wikiHistory.empty();  
  map.hide();
  var text = $('input:text').val();
  textInput.append(text);
  textInput.show();
  $('input:text').val('');
  loader.fadeIn(3500).fadeOut('slow', function() {
    address.show();
    wikiHistory.show(); 
    map.show(); 
  });
});
