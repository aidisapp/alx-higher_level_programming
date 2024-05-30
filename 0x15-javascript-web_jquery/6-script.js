// Script to update the text of the <header> element to "New Header!!!"
// when the user clicks on the <div> element with the ID update_header
$('div#update_header').click(function () {
  $('header').text('New Header!!!');
});
