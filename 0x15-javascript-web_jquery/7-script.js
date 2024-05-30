// Script to fetch and display the character name from the provided URL
// The name is displayed in the <div> element with the ID character
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
