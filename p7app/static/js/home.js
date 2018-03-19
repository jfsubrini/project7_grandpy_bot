// jQuery script to display all the messages and the Google map.

var textUser = $('#textUser');
var address = $('#address');
var wikiHistory = $('#wikiHistory');
var map = $('#map');
var button = $('#submit');
var loader = $('#loader');

button.on('click', function(event) {
  event.preventDefault();
  textUser.hide();
  textUser.html('<img src="../static/images/user.png" alt="Icone de l\'utilisateur" title="Icone de l\'utilisateur" width="70" height="70" id="userPic">');
  address.hide();
  wikiHistory.hide();
  map.hide();
  var text = $('input:text').val();
  
  $.ajax({
    url: '/_query',
    data: $('form').serialize(),
    type: 'POST',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });

  textUser.append(text);
  textUser.show();
  $('input:text').val('');
  loader.fadeIn(3500).fadeOut('slow', function() {
    address.show();
    wikiHistory.show(); 
    map.show(); 
  });
});
