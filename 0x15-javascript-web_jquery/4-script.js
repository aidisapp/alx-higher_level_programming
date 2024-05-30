// Script to toggle the class of the <header> element between 'green' and 'red'
// when the user clicks on the <div> element with the ID toggle_header
$('div#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').attr('class', 'red');
  } else {
    $('header').attr('class', 'green');
  }
});
