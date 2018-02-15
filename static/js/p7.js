/* INTERACTION AVEC LE CLIENT DANS LE BULLETIN D'INSCRIPTION
- AFFICHAGE DES DATES DE VOYAGE
- AFFICHAGE DES CHAMPS EN FONCTION DU NOMBRE DE PARTICIPANTS
- AFFICHAGE DE LA RUBRIQUE TARIFICATION
*/

$(function() {

//AFFICHAGE DES DATES EN FONCTION DU VOYAGE CHOISI
 
    var voyages = $('#voyages');
    voyages.on('change', function(){
    var typeVoyage = $(this).val();
    var clearOption = $('option.rien').val();
      $('select.dates').val(clearOption);
    switch (typeVoyage) {
  case "voy-culture":
    $('#datesVoyCulture').css('display', 'block');
    $('select.dateCulture').attr('required', 'required');
    $('#datesVoyNature').css('display', 'none');
    $('select.dateNature').removeAttr('required');
    $('#datesVoyCourt').css('display', 'none');
    $('select.dateCourt').removeAttr('required');
    break;
  case "voy-nature":
    $('#datesVoyCulture').css('display', 'none');
    $('select.dateCulture').removeAttr('required');
    $('#datesVoyNature').css('display', 'block');
    $('select.dateNature').attr('required', 'required');
    $('#datesVoyCourt').css('display', 'none');
    $('select.dateCourt').removeAttr('required');
    break;
  default :
    $('#datesVoyCulture').css('display', 'none');
    $('#datesVoyNature').css('display', 'none');
    $('#datesVoyCourt').css('display', 'none');
    break;
    };
  });


//AFFICHAGE DES CHAMPS PRENOM, NOM ET DATE DE NAISSANCE EN FONCTION DU NOMBRE DE PARTICIPANTS

  $('#nombreParticipants').on('change', function(){
    var valeur = $(this).val();
    $('input.clear').text(function(){
        $(this).val("");
    });
    var nbPart = "";
    switch (valeur) {
  case "p1":
    $('#part1').css('display', 'block');
    $('#part2').css('display', 'none');
    $('input#prenom2').removeAttr('required');
    $('input#nom2').removeAttr('required');
    $('input#naissance2').removeAttr('required');
    $('#part3').css('display', 'none');
    $('input#prenom3').removeAttr('required');
    $('input#nom3').removeAttr('required');
    $('input#naissance3').removeAttr('required');
    $('#part4').css('display', 'none');
    $('input#prenom4').removeAttr('required');
    $('input#nom4').removeAttr('required');
    $('input#naissance4').removeAttr('required');
    nbPart = 1; 
    break;
  case "p2":
    $('#part1').css('display', 'block');
    $('#part2').css('display', 'block');
    $('input#prenom2').attr('required', 'required');
    $('input#nom2').attr('required', 'required');
    $('input#naissance2').attr('required', 'required');
    $('#part3').css('display', 'none');
    $('input#prenom3').removeAttr('required');
    $('input#nom3').removeAttr('required');
    $('input#naissance3').removeAttr('required');
    $('#part4').css('display', 'none');
    $('input#prenom4').removeAttr('required');
    $('input#nom4').removeAttr('required');
    $('input#naissance4').removeAttr('required');
    nbPart = 2; 
    break;
  default :
    $('#part1').css('display', 'none');
    $('#part2').css('display', 'none');
    $('#part3').css('display', 'none');
    $('#part4').css('display', 'none');
    break;
    };


// AFFICHAGE DE LA RUBRIQUE TARIFICATION

// Affichage du nombre de participants dans TARIFICATION
    $('.participants').text(nbPart);

// Affichage du nom du voyage dans TARIFICATION
        var voyage =  $('#voyages').val();
        switch (voyage) {
        case "voy-culture":
            voyage = ["Patrimoines Culturels d'Andalousie",1496,1364,1122,968];
            break;
        case "voy-nature":
            voyage = ["L'Andalousie côté Nature",1650,1575,1275,1100];
            break;
        case "voy-court":
            voyage = ["Au Coeur de l'Andalousie",1065,990,795,675];
            break;
        default :
            voyage = "";
            break;
        };
        $('.voyageChoisi').text(voyage[0]);

// Affichage du tarif de référence par personne dans TARIFICATION
        var tarifRefPers = voyage[nbPart];
        $('.tarifReference').text(tarifRefPers+',00 €');

//Calcul et affichage du prix total du voyage dans TARIFICATION et input hidden pour gestion en PHP après l'envoi
        var total = nbPart * tarifRefPers;
        $('.totalVoyage').text(total+',00 €');
        $('#tarifTotal').attr('value', total);


// AFFICHAGE DU PRENOM 1 ET NOM 1 EN TANT QUE PRENOM ET NOM DU PARTICIPANT REFERENT
        
        $('#prenom1').on('change', function(){
            var prenom =  $(this).val();
            $('#prenomRef').attr('value', prenom);
        });
        $('#nom1').on('change', function(){
            var nom =  $(this).val();
            $('#nomRef').attr('value', nom);
        });
  });
});