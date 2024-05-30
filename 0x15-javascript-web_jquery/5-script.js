// Script to add a <li> element to a list
// when the user clicks on the <div> element with the ID add_item
$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
