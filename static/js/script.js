// 

// $(function() {

  var $textInput = $('.textInput');
  var $address = $('#address');
  var $history = $('#history');
  var $map = $('#map');  
  var $button = $('#submit');
  var $loader = $('#loader');

  $button.on('submit', function() {
    var text = $('input:text').val();
    $textInput.append(text);
    // $('input:text').val('');
    $loader.css('display', 'block').delay(3000).css('display', 'none');
    $address.delay(3000).css('display', 'block');
    $history.delay(300).css('display', 'block'); 
    $map.delay(300).css('display', 'block'); 
  });
// });


// $button.on('submit', function(event) {
//     event.preventDefault();