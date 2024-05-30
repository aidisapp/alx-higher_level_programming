// Script to add the class 'red' to the <header> element
// when the user clicks on the <div> element with the ID red_header
$('div#red_header').click(function () {
  $('header').addClass('red');
});
