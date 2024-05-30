// Script to change the text color of the <header> element to red (#FF0000)
// when the user clicks on the <div> element with the ID red_header
$('div#red_header').click(function () {
  $('header').css('color', 'red');
});
